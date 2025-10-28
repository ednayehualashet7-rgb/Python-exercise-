# Created on iPad
def classify_age():
    x= int(input("How old are you?"))
    if x<= 12:
        print("You're a child.")
    elif x<=17:
        print("You're a teenager.")
    elif x<= 65:
        print("You're an adult.")
    elif x>65:
        print("You're a senior")
    
classify_age()