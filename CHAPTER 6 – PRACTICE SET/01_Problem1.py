# Write a program to find the greatest of four numbers entered by the user.

a1=int(input("Enter first number: "))
a2=int(input("Enter second number: "))
a3=int(input("Enter third number: "))
a4=int(input("Enter fourth number: "))


if(a1>a2 and a1>a3 and a1>a4):
    print("a1 is greatest")

elif(a2>a1 and a2>a3 and a2>a4):
    print("a2 is greatest")

elif(a3>a1 and a3>a2 and a3>a4):
    print("a3 is greatest")

elif(a4>a1 and a4>a2 and a4>a3):
    print("a4 is greatest")