#task - Write a Python program to count the frequency of words in a file.

count = 0

f = open('read.txt','r')

for line in f:

    word = line.split(' ')
    count += len(word)

print(str(count))