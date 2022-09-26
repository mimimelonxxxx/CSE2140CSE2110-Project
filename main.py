# main.py

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
    print("""1. Horizontal to the water 
2. Parabolic to a level boat 
3. Parabolic to a smaller boat far away""")
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
# Processing # 

# Outputs # 

### MAIN PROGRAM CODE ### 
if __name__ == "__main__":
    menu()
# Inputs # 

# Processing # 

# Outputs # 