f=open("file.txt")

# lines=f.readlines()
# print(lines, type(lines))

# line1=f.readline()
# print(line1, type(line1))

# lines=f.readline()
# print(lines, type(lines))

# lines=f.readline()
# print(lines, type(lines))

# lines=f.readline()
# print(lines, type(lines))

line=f.readline()
while(line!=""):
    print(line)
    line=f.readline()

f.close()