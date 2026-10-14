import string

filename = input("enter file name: ")

file = open(filename,"r")
s = file.read()
file.close()

s = s.lower()

for i in string.punctuation:
    s = s.replace(i," ")

words = s.split()

print("total words =",len(words))

frequency = {}

for i in words:
    if i in frequency:
        frequency[i] +=1
    else:
        frequency[i] =1

sorted_words = sorted(frequency.items(),key=lambda x:x[1],reverse=True)

print("top 10 words:")

for i in range(min(10,len(sorted_words))):
    print(sorted_words[i][0],"=",sorted_words[i][1])