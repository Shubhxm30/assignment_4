# task - Write python program that user to enter only odd numbers, else will
#        raise an exception.



try:
    num = int(input("enter the num:"))
    assert num % 2 != 0

except:
        print('please enter the odd num') 