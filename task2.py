#accept 5 numbers from the users and store even numbers in even list and store odd numbers in odd list.
even_list = []
odd_list =[]
for i in range(1,6):
    num = int(input("enter a number:"))
    if num%2==0:
        even_list.append(num)
    else:
        odd_list.append(num)
        print(even_list)
        print(odd_list)
