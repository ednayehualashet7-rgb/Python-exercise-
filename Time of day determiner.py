# Created on iPad.
def time_of_day():
    x=int(input("What time is it?"))
    if 5<=x<=11:
        print("Good morning!")
        
    elif 11<x<=16:
        print("Good afternoon!")
        
    elif 16<x<=20:
        print("Good evening!")
        
    elif 20<x<=24:
        print("Good night!")
        
    elif 0<=x<5:
        print("Good night!")


time_of_day()