# Created on iPad.
def calculated_tax():
    income = int(input("How much is your income?"))
    if 0<= income<= 2000 :
        tax = 0
        print(tax)
    elif 2000 < income <= 4000:
        tax = income * 0.15
        print(f"{tax} is the tax amount you must pay. ")
    elif 4000< income <= 7000:
        tax = income * 0.2
        print(f"{tax} is the tax amount you must pay. ")
    elif 7000< income <=10000:
        tax = income * 0.25
        print(f"{tax} is the tax amount you must pay. ")
    elif 10000< income <= 14000:
        tax = income * 0.3
        print(f"{tax} is the tax amount you must pay. ")
    elif income > 14000:
        tax = income * 0.35
        print(f"{tax} is the tax amount you must pay. ")
    
calculated_tax()
