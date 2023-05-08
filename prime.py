#To find a prime number 
list1 = [1,2,3,4,5,6]
pr =[]
for x in range (1,len(list1)):
    if x%2==1:
        pr.append(x)
print("The prime numbers in the list is",pr)        
