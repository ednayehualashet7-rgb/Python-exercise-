def convert():
    CT= input("What is the conversion type, C2F or F2C: ")
    Value= int(input("Insert value: "))
    if CT.upper() == "C2F":
        result=(Value * 9/5) + 32
        print(f"{result} Degree Farheniet")
        
    elif CT.upper() == "F2C":
        result=(Value - 32) * 5/9
        print(f"Your value equals {result}")
    
convert()