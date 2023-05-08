#To find a prime number
def prime(): 
    num =int(input("Enter the number: "))
    if num >1:
        for i in range(2,num):
            if(num % i)==0:
                print(num,"is not a prime")
        else:
            print(num,"is a prime number")
    else:
        print(num,"is not a prime number")
        
 
# 	Check if given string is palindrome.
def palindrome():
    x = str(input("Enter the string:"))
    if x ==x[::-1]:
        print(x,"is a palindrome")
    else:
        print(x,"is not a palindrome")
        
def biggest():
    n = int((input("Enter the how many numbers to be added in the list: ")))
    mylist = []
    for x in range(0,n):
        mylist.append(int(input("Enter the number:")))
        print("Your updated list is :",mylist)
    print("The maximum number of list is :",max(mylist)) 
    
#main progarm

print("What operation you want to perfrom ? ")
print("1) prime ")
print("2) palindrome ")
print("3) Biggest in five ")

choice =int(input("Enter your choice between(1-3): "))

if choice==1:
    prime()
elif choice==2:
    palindrome()
elif choice==3:
    biggest()
else:
    print("Please choose the correct choice: ")
    
      
                   
