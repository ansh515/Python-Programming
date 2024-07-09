# Write a program to find the greatest of four numbers entered by the user.

a1=int(input("Enter first number: "))
a2=int(input("Enter second number: "))
a3=int(input("Enter third number: "))
a4=int(input("Enter fourth number: "))


greatest=a1
if(a2>a1):
    greatest = a2

if(a3>a2):
    greatest=a3


if(a4>a3):
    greatest=a4

print("The greatest number is ", greatest)