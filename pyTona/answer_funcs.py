import getpass
import random
import socket
import subprocess
import threading
import time
import Queue

seq_finder = None
fact_finder = None

def feet_to_miles(feet):
    return "{0} miles".format(float(feet) / 5280)

def hal_20():
    return "I'm afraid I can't do that {0}".format(getpass.getuser())

def get_git_branch():
    try:
        process = subprocess.Popen(['git', 'rev-parse', '--abbrev-ref', 'HEAD'], stdout=subprocess.PIPE)
        output = process.communicate()[0]
    except:
        return "Unknown"

    if not output:
        return "Unknown"
    return output.strip()

def get_git_url():
    try:
        process = subprocess.Popen(['git', 'config', '--get', 'remote.origin.url'], stdout=subprocess.PIPE)
        output = process.communicate()[0]
    except:
        return "Unknown"

    if not output:
        return "Unknown"
    return output.strip()

def get_other_users():
    try:
        host = '192.168.64.3'
        port = 1337

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        s.send('Who?')
        data = s.recv(255)
        s.close()
        return data.split('$')

    except:
        return "IT'S A TRAAAPPPP"


class FibSeqFinder(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(FibSeqFinder, self).__init__(*args, **kwargs)
        self.sequence = [0, 1]
        self._stop = threading.Event()
        self.num_indexes = 0

    def stop(self):
        self._stop.set()

    def run(self):
        self.num_indexes = 0
        while not self._stop.isSet() and self.num_indexes < 1000:
            self.sequence.append(self.sequence[-1] + self.sequence[-2])
            self.num_indexes += 1
            time.sleep(.04)

def get_fibonacci_seq(index):
    index = int(index)
    global seq_finder
    if seq_finder is None:

        seq_finder = FibSeqFinder()
        seq_finder.start()

    if index > seq_finder.num_indexes:
        value = random.randint(0, 9)
        if value >= 4:
            return "Thinking..."
        elif value > 1:
            return "One second"
        else:
            return "cool your jets"
    else:
        return seq_finder.sequence[index]

class FactSeqFinder(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(FactSeqFinder, self).__init__(*args, **kwargs)
        self.fact_list = [1]
        self._stop = threading.Event()
        self.num_facts = 0

    def stop(self):
        self._stop.set()

    def run(self):
        self.num_facts = 0
        while not self._stop.isSet() and self.num_facts <= 50:
            self.num_facts += 1
            self.fact_list.append(self.fact_list[-1] * self.num_facts)
            time.sleep(.04)


def get_factorial_seq(index):
    index = int(index)
    global fact_finder
    if fact_finder is None:
        fact_finder = FactSeqFinder()
        fact_finder.start()

    if index > 50:
        return "I can't count that high"
    elif index > fact_finder.num_facts:
        return "Working"
    else:
        return fact_finder.fact_list[index]

def calculate_square(val, queue):
    val = int(val)
    new = val ** 2
    queue.put(new)

def get_square(val):
    answer_value = Queue.Queue()

    if val <= 1000:
        root_thread = threading.Thread(target=calculate_square, args=(val, answer_value))
        root_thread.start()
        root_thread.join(timeout=2)

        if root_thread.isAlive():
            raise Exception("The thread {} is still alive".format(root_thread.name))

        return answer_value.get()
    else:
        return "I can't count that high"

def calculate_cube_root(num, queue):
    num = int(num)
    new = round(num**(1.0/3.0))
    print new
    queue.put(new)

def get_cube_root(num):
    answer_value = Queue.Queue()
    if num <= 1000000:
        root_thread = threading.Thread(target=calculate_cube_root, args=(num, answer_value))
        root_thread.daemon = True
        root_thread.start()
        root_thread.join(timeout=2)

        if root_thread.isAlive():
            raise Exception("The thread {} is still alive".format(root_thread.name))

        return answer_value.get()
    else:
        return "I can't count that high"

def get_file():
    filename = '.\\pyTona\\read_test.txt'
    try:
        with open(filename) as f:
            num_bytes = f.read()
            return len(num_bytes)
    except:
        return "File not found"


