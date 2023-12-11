#task - Write a Python program to count the number of lines in a text file.

with open ("read.txt",'r') as file:
    count = 0

    for line in file:
        count += 1

print(count)