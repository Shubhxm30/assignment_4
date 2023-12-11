# task - Write a Python program to write a list to a file

list = ['hii','this','is the','list.']

file = open('read.txt','w')

file.writelines(list)

print(file)

file.close()
