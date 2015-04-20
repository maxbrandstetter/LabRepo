"""
Round 1: Meant to simulate an Orc defense system, as well as classes for necessary objects

To keep it simple, a lot of functions are self guided, despite alluding to otherwise.
If this is an issue, I can redo those portions to allow for user input.
"""
import sys

def orc_defense_system(s = 10, d = 300, selection = 0, orc = 1, u = 'metric'):

    global units
    units = u

    def display_menu():
        print ("Welcome to the ODI (Orc Defense Interface)")
        print ("Please select an action")
        print (" ")
        
    def display_options():
        print ("D (Display only distances of current orcs)")
        print ("S (Display only speeds of current orcs)")
        print ("X (Exits the interface)")

    if units == 'imperial':
        s *= 3.28
        d *= 3.28
    if units == 'parsec':
        s *= (3.24 * 10**-17)
        d *= (3.24 * 10**-17)
    if units == 'nautical':
        s *= 1.94
        d *= 0.00054

    """
    orc_type is implemented with modulo to restrict the number
    of types to 8 without defining those types explicitly
    """
    class Orc():
        class_counter = 0
        def __init__(self, speed, distance, orc_type):
            self.speed = speed
            self.distance = distance
            self.orc_type = orc_type % 8
            self.orc_id = str(Orc.class_counter)
            self.priority = None
            Orc.class_counter += 1
    
    trial_orc = Orc(s, d, orc)
    choice = selection

    orcList = []
    orcList.append(trial_orc)
    orcList.append(Orc(20, 500, 6))

    if choice == 'X':
        sys.exit(1)

    if choice == 'D':
        return trial_orc.distance

    if choice == 'S':
        return trial_orc.speed

    if choice == 'T':
        return trial_orc.orc_type

    if choice == 'R':
        for Orc in orcList:
            if '0' in Orc.orc_id:
                orcList.remove(Orc)
                return "Target Removed"

    if choice == 'P':
        print [Orc.speed for Orc in orcList]
        print [Orc.distance for Orc in orcList]
        print [Orc.orc_type for Orc in orcList]
        print [Orc.orc_id for Orc in orcList]
        print (" ")
        print ("Select targeting priority.")
        target = '0'
        priority = 2
        for Orc in orcList:
            if target in Orc.orc_id:
                Orc.priority = priority
                return Orc.priority
            
    if choice == '?':
        display_options()
        return True
        
    if trial_orc.distance <= 200:
        return "Perimeter Breach"
    
    

    
