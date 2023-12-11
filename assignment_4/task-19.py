# task - How Do You Handle Exceptions With Try/Except/Finally In Python?
#        Explain with coding snippets.


#a = 5
#b = 0
#print(a/b)

# its giving the zero division error so lets solve this.

a = 10
b = int(input("Enter the num:"))

try:
    division = a / b
    print(division)

except ZeroDivisionError:
    print("enter the num more than 0")

finally:
    print("this always executed.")