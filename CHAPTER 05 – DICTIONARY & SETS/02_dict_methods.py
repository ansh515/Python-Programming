marks={
    "Kunal":72,
    "Ansh":100,
    "Nikhil":80,
    "Vinod":85,
    0:"Harry"
}

print(marks.items())

print(marks.keys())
print(marks.values())

marks.update({"Ansh":98})
print(marks)

print(marks.get("Ansh"))

print(marks.get("ansh1"))  #Prints None
print(marks["ansh1"])  #Returns an error 

d={0:1,1:"G:ONE"}
print(len(d))