n = int((input("Enter the how many numbers to be added in the list: ")))
mylist = []
for x in range(0,n):
    mylist.append(int(input("Enter the number:")))
    print("Your updated list is :",mylist)
print("The maximum number of list is :",max(mylist))