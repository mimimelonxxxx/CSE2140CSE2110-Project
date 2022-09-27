# main.py

import math
from tkinter import VERTICAL 

### SUBROUTINES ### 

# Inputs # 
def checkInt(VALUE): 
    """
    Validate whether a string is an integer 
    :param VALUE: string 
    :return: int 
    """
    if VALUE.isnumeric(): 
        VALUE = int(VALUE) 
        return VALUE
    else: 
        print("Please enter a valid number! ")
        NEW_NUM = input("> ")
        return checkInt(NEW_NUM)

def menu():
    """
    display different scenarios and asks user to make a selection
    :return: int
    """
    print("Welcome to the Official Navy Cannon Distance Calculator! Find the total distance the cannonball travels from the cannon! ")
    print("""
1. Horizontal to the water 
2. Parabolic to a level boat 
3. Parabolic to a smaller boat far away
""")
    SCENARIONUMBER = input("What is the scenario number? ")
    SCENARIONUMBER = checkInt(SCENARIONUMBER)
    return SCENARIONUMBER

def getSpeed(): 
    """
    asks user to input speed in m/s
    :return: int 
    """
    SPEED = input("What is the speed of the cannonball? (m/s): ")
    SPEED = checkInt(SPEED)
    return SPEED 

def getAngle(): 
    """
    asks user to input the angle above the horizontal in degrees
    :return: int
    """
    ANGLE = input("What is the angle above the horizontal? (degrees): ")
    ANGLE = checkInt(ANGLE)
    return ANGLE 

def getHeight(): 
    """
    asks user to input the initial height of the cannonball above the water in meters
    :return: int
    """
    HEIGHT = input("What is the height of the cannonball above the water? (m): ")
    HEIGHT = checkInt(HEIGHT)
    return HEIGHT

def getHeight3():
    """
    asks the user to input the inital height of the cannonball above the enenmy ship in meters
    :return: int 
    """
    HEIGHT = input("What is the initial height of the cannonball above the enemy ship? (m): ")
    HEIGHT = checkInt(HEIGHT)
    return HEIGHT 

# Processing # 
def calculateTime1(HEIGHT): 
    """
    calculate time in scenario 1 when given height (m)
    :param HEIGHT: int
    :return: int 
    """
    TIME = math.sqrt((2 * HEIGHT) / 9.81)
    return TIME 

def calculateHorizontalSpeed(SPEED, ANGLE):
    """
    calculate horizontal speed when given cannonball speed (m/s) and angle (degrees)
    :param SPEED: int
    :param ANGLE: int
    :return: int
    """
    HORIZONTALSPEED = SPEED * math.cos(ANGLE)
    return HORIZONTALSPEED

def calculateVerticalSpeed(SPEED, ANGLE):
    """
    calculate vertical speed when given cannonball speed (m/s) and angle (degrees)
    :param SPEED: int 
    :param ANGLE: int 
    :return: int 
    """
    VERTICALSPEED = SPEED * math.sin(ANGLE)
    return VERTICALSPEED

def calculateTotalTime(VERTICALSPEED):
    """
    calculate the total time when given vertical speed in m/s
    :param VERTICALSPEED: int
    :return: int
    """
    TIME = VERTICALSPEED / 9.81
    TOTALTIME = TIME * 2
    return TOTALTIME

def calculateDistance(HORIZONTALSPEED, TOTALTIME):
    """
    calculate distance from horizontal speed (m/s) and total time (s)
    :param HORIZONTALSPEED: int
    :param TOTALTIME: int
    :return: int
    """
    DISTANCE = HORIZONTALSPEED * TOTALTIME
    return DISTANCE 

def calculateDistance3(VERTICALSPEED, HEIGHT):
    """
    calculate total distance from vertical speed and height above ship
    :param VERTICALSPEED: int
    :param HEIGHT: int
    :return: int
    """
    DISTANCEPEAK = VERTICALSPEED ** 2 / (2 * 9.81)

# Outputs # 

### MAIN PROGRAM CODE ### 
if __name__ == "__main__":
    menu()
# Inputs # 

# Processing # 

# Outputs # 