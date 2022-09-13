from secrets import choice
from views import*

name = input("Enter your name:")

menu = """
                MENU

            1)LAPTOP
            2)MOBILE
"""

print(menu)

choice = int(input("Enter you choice:"))
if choice == 1:
    viewLaptop()
    laptop_name = input("enter laptop name which you want to purchase:")
    qty = int(input("Enter no. of qty do you want to purchase:"))
    total_price = purchaseLaptop(laptop_name,qty)
    choice = input("do you want to purchase it press 'y' for yes:")
    if choice=='y' or choice=='yes':
        addTocart(name,"laptop",laptop_name,qty,total_price)

elif choice==2:
    viewMobile()

else:
    print("invalid input")