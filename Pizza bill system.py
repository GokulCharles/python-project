#PIZZA BILL SYSTEM
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

#prices of pizzas
small=15
medium=20
large=25

pepperoni_for_small=2
pepperoni_for_other=3
cheese=1
# sizes with cheese and pepperoni
small_pep_cheese=int(small)+int(pepperoni_for_small)+int(cheese)
medium_pep_cheese=int(medium)+int(pepperoni_for_other)+int(cheese)
large_pep_cheese=int(large)+int(pepperoni_for_other)+int(cheese)
#sizes with only pepperoni
small_pep=int(small)+int(pepperoni_for_small)
medium_pep=int(medium)+int(pepperoni_for_other)
large_pep=int(large)+int(pepperoni_for_other)
#sizes with only cheese:
small_cheese=int(small)+int(cheese)
medium_cheese=int(medium)+int(cheese)
large_cheese=int(large)+int(cheese)

if size=="S":
    if add_pepperoni=="Y":
        if extra_cheese=="Y":
            print(f"Your final bill is: ${small_pep_cheese}.")
        else:
            print(f"Your final bill is: ${small_pep}.")
    else:
        if extra_cheese=="Y":
            print(f"Your final bill is: ${small_cheese}.")
        else:
            print(f"Your final bill is: ${small}.")
        
elif size=="M":
    if add_pepperoni=="Y":
        if extra_cheese=="Y":
            print(f"Your final bill is: ${medium_pep_cheese}.")
        else:
            print(f"Your final bill is: ${medium_pep}.")
    else:
        if extra_cheese=="Y":
            print(f"Your final bill is: ${medium_cheese}.")
        else:
            print(f"Your final bill is: ${medium}.")            
        
elif size=="L":
    if add_pepperoni=="Y":
        if extra_cheese=="Y":
            print(f"Your final bill is: ${large_pep_cheese}.")
        else:
            print(f"Your final bill is: ${large_pep}.")
    else:
         if extra_cheese=="Y":
            print(f"Your final bill is: ${large_cheese}.")
         else:
            print(f"Your final bill is: ${large}.")

else:
    print("Please enter correct size")    


#Write your code below this line 👇
