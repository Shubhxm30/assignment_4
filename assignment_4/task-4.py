# task - Write a Python program to read first n lines of a file.

file = "read.txt"

line = int(input("enter the line num:"))

with open(file,'r') as filedata:
    list = filedata.readlines()
    print(f"the following are the first",line,"lines of a text file:")

    for textline in (list[:line]):
        print(textline, end = '')

filedata.close()