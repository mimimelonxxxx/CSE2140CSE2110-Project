# main.py

import math
import sys

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

def checkFloat(VALUE):
    """
    validates whether a value is a float
    :param VALUE: str
    :return: float
    """
    try: 
        float(VALUE)
        return float(VALUE)
    except ValueError:
        print("Please enter a valid number! ")
        NEW_NUM = input("> ")
        return checkFloat(NEW_NUM)
def intro(): 
    print("Welcome to the Official Navy Cannon Distance Calculator! Find the total distance the cannonball travels from the cannon! ")

def menu():
    """
    display different scenarios and asks user to make a selection
    :return: int
    """
    print("""
1. Horizontal to the water 
2. Parabolic to a level boat 
3. Parabolic to a smaller boat far away
4. Parabolic to a larger boat far away
""")
    SCENARIONUMBER = input("What is the scenario number? ")
    SCENARIONUMBER = checkInt(SCENARIONUMBER)
    if not (SCENARIONUMBER == 1 or SCENARIONUMBER == 2 or SCENARIONUMBER == 3 or SCENARIONUMBER == 4): 
        print("Please enter a valid number! ")
        return menu() 
    return SCENARIONUMBER

def getSpeed(): 
    """
    asks user to input speed in m/s
    :return: float 
    """
    SPEED = input("What is the speed of the cannonball? (m/s): ")
    SPEED = checkFloat(SPEED)
    return SPEED 

def getAngle(): 
    """
    asks user to input the angle above the horizontal in degrees
    :return: float
    """
    ANGLE = input("What is the angle above the horizontal? (degrees): ")
    ANGLE = checkFloat(ANGLE)
    return ANGLE 

def getHeight(): 
    """
    asks user to input the initial height of the cannonball above the water in meters
    :return: float
    """
    HEIGHT = input("What is the height of the cannonball above the water? (m): ")
    HEIGHT = checkFloat(HEIGHT)
    return HEIGHT

def getHeight3():
    """
    asks the user to input the inital height of the cannonball above or below the enenmy ship in meters
    :return: float 
    """
    HEIGHT = input("What is the initial height of the cannonball above or below the enemy ship? (m): ")
    HEIGHT = checkFloat(HEIGHT)
    return HEIGHT 

def repeatProcess():
    """
    asks user to repeat process 
    :return: boolean
    """
    CHOICE = input("Would you like to repeat this process with new numbers? (y/N): ")
    if CHOICE == "y" or CHOICE == "Y": 
        return True
    else: 
        return False

# Processing # 
def calculateTime1(HEIGHT): 
    """
    calculate time (s)  in scenario 1 when given height (m)
    :param HEIGHT: float
    :return: float 
    """
    TIME = math.sqrt((2 * HEIGHT) / 9.81)
    return TIME 

def calculateHorizontalSpeed(SPEED, ANGLE):
    """
    calculate horizontal speed (m/s) when given cannonball speed (m/s) and angle (degrees)
    :param SPEED: float
    :param ANGLE: float
    :return: float
    """
    RADANGLE = ANGLE * (math.pi / 180) # angle in radians
    COSINEANGLE = math.cos(RADANGLE) # cosine of angle  
    HORIZONTALSPEED = SPEED * COSINEANGLE
    return HORIZONTALSPEED

def calculateVerticalSpeed(SPEED, ANGLE):
    """
    calculate vertical speed (m/s) when given cannonball speed (m/s) and angle (degrees)
    :param SPEED: float 
    :param ANGLE: float 
    :return: float 
    """
    ANGLE = ANGLE * (math.pi / 180) 
    SINEANGLE = math.sin(ANGLE)
    VERTICALSPEED = SPEED * SINEANGLE
    return VERTICALSPEED

def calculateTimePeak(VERTICALSPEED):
    """
    calculates the time (s) it takes for a cannonball to reach its peak when given vertical speed in m/s
    :param VERTICALSPEED: float
    :return: float 
    """
    TIME = VERTICALSPEED / 9.81
    return TIME

def calculateTotalTime(VERTICALSPEED):
    """
    calculate the total time (s) when given vertical speed in m/s
    :param VERTICALSPEED: float
    :return: float
    """
    TIME = VERTICALSPEED / 9.81
    TOTALTIME = TIME * 2
    return TOTALTIME

def calculateDistance(HORIZONTALSPEED, TOTALTIME):
    """
    calculate distance (m) from horizontal speed (m/s) and total time (s)
    :param HORIZONTALSPEED: float
    :param TOTALTIME: float
    :return: float
    """
    DISTANCE = HORIZONTALSPEED * TOTALTIME
    return DISTANCE 

def calculateDistance3(VERTICALSPEED, HEIGHT):
    """
    calculate total distance (m) from vertical speed and difference in height of the ships
    :param VERTICALSPEED: float
    :param HEIGHT: float
    :return: float
    """
    DISTANCEPEAK = VERTICALSPEED ** 2 / (2 * 9.81)
    TOTALHEIGHT = DISTANCEPEAK + HEIGHT 
    return TOTALHEIGHT

def finalVelocity(INITIALYSPEED, HEIGHT):
    """
    calculates the final velocity of the cannonball when given the initial y-speed and the difference in height between the ships
    :param INITIALYSPEED: float
    :param HEIGHT: float
    :return: float
    """
    FINALVELOCITY = math.sqrt(INITIALYSPEED ** 2 + 2 * -9.81 * HEIGHT)
    return -FINALVELOCITY, FINALVELOCITY

def calculateTime4(FINALVELOCITY, INITIALVELOCITY, HEIGHT): 
    """
    calculates time from the initial and final x-speed and the difference in height
    :param FINALVELOCITY: float 
    :param INITIALVELOCITY: float 
    :param HEIGHT: float 
    :return: float 
    """
    TIME = HEIGHT / ((FINALVELOCITY + INITIALVELOCITY) / 2)
    return TIME

# Outputs # 
def displayDistance(DISTANCE):
    """
    displays the total distance (m) the cannonball travels to 3 sig digs
    :param DISTANCE: float
    :return: None
    """
    print(f"The total distance the cannonball travelled is {DISTANCE}m. ")

def displayDistance4(DISTANCEUP, DISTANCEDOWN):
    """
    displays the total distance (m) the cannonball travels in both the upwards portion of the parabola and the downwards portion of the parabola
    :param DISTANCEUP: float
    :param DISTANCEDOWN: float
    :return: None
    """
    print(f"The total distance the cannonball travelled to hit in the upward parabola is {DISTANCEUP}m, and the total distance the cannonball travelled to hit in the downward parabola is {DISTANCEDOWN}m. ")
### MAIN PROGRAM CODE ### 
if __name__ == "__main__":
    while True:
        intro()
# Inputs # 
        SCENARIO = menu()
        if SCENARIO == 1: 
            # Inputs # 
            SPEED = getSpeed()
            HEIGHT = getHeight()
            # Processing # 
            TIME = calculateTime1(HEIGHT)
            DISTANCE = calculateDistance(SPEED, TIME)
            # Outputs # 
            displayDistance(DISTANCE)
        elif SCENARIO == 2:
            # Inputs # 
            SPEED = getSpeed()
            ANGLE = getAngle()
            # Processing # 
            HORIZONTALSPEED = calculateHorizontalSpeed(SPEED, ANGLE)
            VERTICALSPEED = calculateVerticalSpeed(SPEED, ANGLE)
            TIME = calculateTotalTime(VERTICALSPEED)
            DISTANCE = calculateDistance(HORIZONTALSPEED, TIME)
            # Outputs # 
            displayDistance(DISTANCE)
        elif SCENARIO == 3:
            # Inputs # 
            SPEED = getSpeed()
            ANGLE = getAngle()
            HEIGHT = getHeight3() 
            # Processing # 
            HORIZONTALSPEED = calculateHorizontalSpeed(SPEED, ANGLE)
            VERTICALSPEED = calculateVerticalSpeed(SPEED, ANGLE)
            TIMEPEAK = calculateTimePeak(VERTICALSPEED)
            TOTALHEIGHT = calculateDistance3(VERTICALSPEED, HEIGHT)
            TIME = calculateTime1(TOTALHEIGHT)
            TOTALTIME = TIMEPEAK + TIME
            DISTANCE = calculateDistance(HORIZONTALSPEED, TOTALTIME)
            # Outputs # 
            displayDistance(DISTANCE)
        elif SCENARIO == 4: 
            # Inputs # 
            SPEED = getSpeed()
            ANGLE = getAngle() 
            HEIGHT = getHeight3()
            # Processing # 
            HORIZONTALSPEED = calculateHorizontalSpeed(SPEED, ANGLE)
            VERTICALSPEED = calculateVerticalSpeed(SPEED, ANGLE)
            FARFINALVELOCITY, CLOSEFINALVELOCITY = finalVelocity(HORIZONTALSPEED, HEIGHT)
            TOTALTIMEFAR = calculateTime4(FARFINALVELOCITY, VERTICALSPEED, HEIGHT)
            TOTALTIMECLOSE = calculateTime4(CLOSEFINALVELOCITY, VERTICALSPEED, HEIGHT)
            DISTANCEFAR = calculateDistance(HORIZONTALSPEED, TOTALTIMEFAR)
            DISTANCECLOSE = calculateDistance(HORIZONTALSPEED, TOTALTIMECLOSE)
            # Outputs # 
            displayDistance4(DISTANCECLOSE, DISTANCEFAR)
        if repeatProcess() == False: 
            sys.exit()