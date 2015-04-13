"""
Round 1: Meant to simulate an Orc defense system, as well as classes for necessary objects
"""
import sys

def orc_defense_system(s = 10, d = 300, selection = 0):

    def display_menu():
        print ("Welcome to the ODI (Orc Defense Interface)")
        print ("Please select an action")
        print (" ")
        print ("D (Display only distances of current orcs)")
        print ("S (Display only speeds of current orcs)")
        print ("X (Exits the interface)")
        
    class Orc():
        speed = s
        distance = d
    
    trial_orc = Orc()
    choice = selection

    if choice == 'X':
        sys.exit(1)

    if choice == 'D':
        print (trial_orc.distance)

    if choice == 'S':
        print (trial_orc.speed)
        
    if trial_orc.distance <= 200:
        return "Perimeter Breach"
    """
    if isinstance(trial_orc.distance, (int, float)):
        return trial_orc.distance

    if isinstance(trial_orc.speed, (int, float)):
        return trail_orc.speed
    """
    
    

    
