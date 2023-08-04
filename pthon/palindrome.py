string=input('enter your string:')

rev=string[::-1]

if string == rev:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")