data="""
                MENU
            1. PRESS 1 FOR ADD ITEMS.
            2. PRESS 2 FOR CHECK ITEMS.
            3. PRESS 3 FOR REMOVE ITEMS.
            4. PRESS 4 FOR VIEW ITEMS.
        
    """
amazon_store =  []
print("WELCOME TO AMAZON STORE")
status = True
while status :
    print(data)
    choice = int(input("enter your choice:"))
    if choice==1:
        item_name = input("enter item:")
        amazon_store.append(item_name)
    elif choice==2:
        print("Available")
    elif choice==3:
        item_name = input("enter item:")
        if item_name in amazon_store:
            amazon_store.remove(item_name)
        else:
            print("Not Available")
    elif choice==4:
        # loop through list
        print("total no.of item in amazon_store:",len(amazon_store))
        print("------------------------")
        for item in amazon_store:
            print(item)
            print("---------------------------")
        else:
            print("invalid input")
    else:
        print("sorry item dose not exist")
user_choice = input("do you want to perform more operation press'y' for yes and no for 'n'")
if user_choice=='n' or user_choice=='no' or user_choice=='N':
            status = False
else:
            status = True




