# Write a program to find whether a given username contains less than 10 
# characters or not.

a=input("Enter username: ")
if(len(a)<10):
    print("Username contains less than 10 characters")
    
else:
    print("Username exceeds or equal to 10 characters")