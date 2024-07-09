# If the names of 2 friends are same; what will happen to the program in problem 
# 6?

dict={}

name=input("Enter friend's name: ")
lang= input("Enter language name: ")
dict.update({name:lang})

name=input("Enter friend's name: ")
lang= input("Enter language name: ")
dict.update({name:lang})

name=input("Enter friend's name: ")
lang= input("Enter language name: ")
dict.update({name:lang})

name=input("Enter friend's name: ")
lang= input("Enter language name: ")
dict.update({name:lang})

print(dict)
# Enter friend's name: Ansh
# Enter language name: Python 
# Enter friend's name: Vyom
# Enter language name: C++
# Enter friend's name: Arunav
# Enter language name: JS
# Enter friend's name: Vyom
# Enter language name: Java
# {'Ansh': 'Python', 'Vyom': 'Java', 'Arunav': 'JS'}