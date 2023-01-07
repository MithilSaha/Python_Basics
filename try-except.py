'''
The try block will be first executed and if there is an error in try block then it will move to except
block and if the error in try block is handled in except block then it will print the user friendly
error or pass if mentioned.
try-except blocks are used to run the code even if in the code there is an error. Without the use of 
try-except block the code will stop to run when python faces an error.
try-except blocks are used not to show the traceback errors, filename,  line number of the code in the
terminal or to the user.
'''
try:
    print(5/0)
except ZeroDivisionError:
    print("A number can't be divided by zero")
try:
    print(5/a)
except NameError:
    print("Define the varibale a")
try:
    print(5/"c")
except TypeError:
    print("A number can be divided by another number")
x = [1,2]
try:
    print(x[2])
except IndexError:
    print(f"The length of x is {len(x)}")
'''
The else block will be executed if the try is executed without any kind of error. The else block is used
to execute the rest of the code if the expected error is not encountered in try block.
'''
try:
    a = 5/2
except ZeroDivisionError:
    print("A number can't be divided by zero")
except TypeError:
    print("A number can be divided by another number")
else:
    print(a)
print(3*1)