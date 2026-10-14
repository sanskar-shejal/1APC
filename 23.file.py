filename = input("enter file name: ")
old = input("enter word to replace: ")
new = input("enter new word: ")
choice = input("case insensitive? yes/no: ")

file = open(filename,"r")
s = file.read()
file.close()

if choice == "yes":
    import re
    s = re.sub(re.escape(old),new,s,flags=re.IGNORECASE)
else:
    s = s.replace(old,new)

newfile = input("enter new file name: ")

file = open(newfile,"w")
file.write(s)
file.close()

print("file saved")