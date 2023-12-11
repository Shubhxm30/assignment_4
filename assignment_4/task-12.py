# task - Write a Python program to copy the contents of a file to another file.

f1 = open('read.txt','r')
f2 = open('hii.txt','w')

for line in f1:

    f2.writelines(line)

print(f2)