# Name: Sakshi Ganesh Ambavane
# Python Assignment-3

----------------------------------------------------------------------------------------------------------

#  Q.1)Write a Python program that takes a number as input and prints "Even" if the number is even and "Odd" if it's odd.

num =int(input("Enter a number: "))

if num % 2 == 0 :
	print("Even Number")
else:
	print("Odd Number")

Output:

Enter a number: 2
Even Number

Enter a number: 5
Odd Number

----------------------------------------------------------------------------------------------------------

# Q.2) Create a Python program that checks whether a person is eligible to vote (18 years or older) based on their age.

num = int(input("Enter age: "))

if num >= 18:
	print("The person is eligible to vote")
else:
	print("Person is not eligible for vote")

Output:
Enter age: 22
The person is eligible to vote

----------------------------------------------------------------------------------------------------------

# Q.3) Write a Python program that determines if a given year is a leap year or not.

year = int(input("Enter Year: "))

if year % 4 == 0:
	print("It is a leap year")
else:
	print("It is not a leap year")

Output:
Enter Year: 2024
It is a leap year

----------------------------------------------------------------------------------------------------------

# Q.4)  Create a Python program that checks if a user-given number is positive, negative, or zero.

data = int(input("Enter a number: "))
if data > 0:
	print("Number is Positive")
elif data < 0:
	print("Number is negative")
else:
	print("The number is zero")

Output:

Enter a number: 8
Number is Positive

Enter a number: -5
Number is negative

Enter a number: 0
The number is zero
