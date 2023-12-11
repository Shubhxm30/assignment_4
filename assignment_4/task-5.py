# task- Write a Python program to read last n lines of a file.

n = int(input("Enter the lines:"))

with open('read.txt') as r:

    print(''.join(r.readlines()[-n:]))