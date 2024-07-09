# Write a program to find whether a given number is prime or not.

n=int(input("Enter a number: "))

for i in range(2,n):
   if(n%i)==0:
        print("Composite number")
        break
else:
        print("Prime")
