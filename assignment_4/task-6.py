# task- Write a Python program to read a file line by line and store it into a list

lines = []

with open('read.txt','r') as r:
    for line in r:
        lines.append(line.strip()) 

print(lines)