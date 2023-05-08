
# 	Check if given string is palindrome.
x = str(input("Enter the string:"))
y = ""
for i in x:
    y = i+y
if x == y:
    print("Given string is palindrome:")
else:
    print("Given string is not palindrome:")
