#accept 5 numbers from the users and store positive numbers in positive list and store negative numbers in negative list.
positive_numbers = []
negative_numbers= []
for i in range(1,6):
    num = int(input("enter a number:"))
    if num>0:
        positive_numbers.append(num)
    else:
        negative_numbers.append(num)
        print(positive_numbers)
        print(negative_numbers)