# Name: Sakshi Ganesh Ambavane
# Python Assignment-1

----------------------------------------------------------------------------------------------------------

Q.1) WAPP to print hellow world

print("Hello World")

Output: Hellow World
----------------------------------------------------------------------------------------------------------

Q.2) WAPP that describe local variable and global variable code

x = 10

def my_function():
    # Local variable
    y = 5
    print("Local variable y:", y)
    print("Global variable x:", x)

my_function()
print("Global variable x outside function:", x)

Output:
Local variable y: 5
Global variable x: 10
Global variable x outside function: 10
----------------------------------------------------------------------------------------------------------

Q.3) WAPP that describe Indentation error

def my_function():
print("Hello, World!")  # This will cause an indentation error

my_function()

output:
print("Hello, World!")  # This will cause an indentation error
    ^
IndentationError: expected an indented block after function definition on line 3
----------------------------------------------------------------------------------------------------------------------------------------

Q.4) WAPP that describe local and global variable with same name

# Global Variables: Python Global variables are those which are not defined inside any function and have a global scope
#Local Variables: Local variables in Python are those which are initialized inside a function and belong only to that particular function. 
It cannot be accessed anywhere outside the function.

x = 10  # Global variable

def my_function():
    x = 5  # Local variable with the same name
    print("Local x:", x)

my_function()
print("Global x:", x)

Output:
Local x: 5
Global x: 10
----------------------------------------------------------------------------------------------------------------------------------------
Q.5)  WAPP to print Write a code for string, int and float input.

string = input("Enter a string: ")
integer = int(input("Enter an Integer: "))
float = float(input("Enter a floating number: "))

print("String Input: ", string)
print("Integer Input: ", integer)
print("float Input: ", float)

Output:
Enter a string: Sakshi
Enter an Integer: 1
Enter a floating number: 90
String Input:  Sakshi
Integer Input:  1
float Input:  90.0
