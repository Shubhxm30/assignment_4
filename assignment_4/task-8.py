#task - Write a python program to find the longest words.

file = open("read.txt")

a = file.read()

a = a.split()
maxword= ""

for word in a:
    if len(word)>len(maxword):
        maxword = word
print(maxword)