weight= int(input('Weight: '))
unit=input('(L)bs or (K)gs: ')
if unit.upper()=="L":
    converted=weight*0.45
    print(f"You are {converted}Kilos")
elif unit.upper()=="K":
    converted = weight/0.45
    print(f"You are {converted} Lbs")
else:
    print("Please enter your weight")