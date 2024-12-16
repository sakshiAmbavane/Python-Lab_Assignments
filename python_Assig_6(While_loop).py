----------------------------------------------------------------------------------------------------------
# Name: Sakshi Ganesh Ambavane
# Python Assignment-6 (While Loop)

----------------------------------------------------------------------------------------------------------

# Q.1) Print the reverse order series  using a while loop

numbers = [1,2,3,4,5,6,7]
index = 6

while index >=1:
	print("The reversed series is:", numbers[index])
	index = index -1

Output:

The reversed series is: 7
The reversed series is: 6
The reversed series is: 5
The reversed series is: 4
The reversed series is: 3
The reversed series is: 2

----------------------------------------------------------------------------------------------------------

# Q.2) Create a code that describe the use of break statement in while loop


numbers = 1

while numbers < 6:
	print(numbers)
	if numbers == 4:
		break
	numbers = numbers + 1

Output:
1
2
3
4

----------------------------------------------------------------------------------------------------------

# Q.3) Write a Python program using a while loop to iterate through each character of the string "Python" and print each character on a new line. Additionally, calculate and print the length of the string.

str = "Python"

index = 0
while index < len(str):
	print(str[index])
	index = index + 1

print("The length of string is: ", len(str))


Output:

P
y
t
h
o
n
The length of string is:  6

----------------------------------------------------------------------------------------------------------

# Q.4) Write a Python program that takes an integer input from the user and calculates its factorial using a while loop. Display the result as the factorial of the entered number.

number = int(input("enter a number: "))

factorial = 1
i = 1
while i <= number:
	factorial = factorial * i
	i = i + 1
print("The factorial of", number, "is:",factorial)

Output:

enter a number: 5
The factorial of 5 is: 120

----------------------------------------------------------------------------------------------------------


# Q.5) 2. Write a python program to check whether a number is palindrome or not? 

name = input("Enter a string: ")

s2 = ""

for s in name:
	s2 = s + s2

# comapare original vs reverse

if name == s2:
	print("String is palindrome")
else:
	print("It is not a palindrome")

Output:

Enter a string: Mom
It is not a palindrome

Enter a string: sakshi
It is not a palindrome

----------------------------------------------------------------------------------------------------------

# Q.6) Accept numbers using input() function until the user enters 0. If user input 0 then break the while loop and display the sum of all the numbers.


total_sum = 0

while True:

	num = int(input("Enter a number: "))
	
	# Break the loop if the input is 0
	if num == 0:
		break

	total_sum = total_sum + num

print("The sum of all numbers is: ", total_sum)

Output:

Enter a number: 153
Enter a number: 5
Enter a number: 9
Enter a number: 24
Enter a number: 6
Enter a number: 0
The sum of all numbers is:  197

----------------------------------------------------------------------------------------------------------

# Q.7) Program to check whether the given number is Armstrong or not.


# Function to check if a number is an Armstrong number
def is_armstrong(number):
    # Initialize variables
    num_digits = len(number)
    armstrong_sum = 0
    i = 0  # Index to iterate over the string

    # While loop to calculate the sum of powers of each digit
    while i < num_digits:
        digit = int(number[i])  # Get the current digit
        armstrong_sum += digit ** num_digits  # Add digit^num_digits to the sum
        i += 1  # Move to the next digit

    # Compare the calculated sum with the original number
    return int(number) == armstrong_sum

# Input two strings
number1 = input("Enter the first number: ")
number2 = input("Enter the second number: ")

# Check for the first number
if is_armstrong(number1):
    print(f"{number1} is an Armstrong number.")
else:
    print(f"{number1} is not an Armstrong number.")

# Check for the second number
if is_armstrong(number2):
    print(f"{number2} is an Armstrong number.")
else:
    print(f"{number2} is not an Armstrong number.")

Output:

Enter the first number: 457
Enter the second number: 153
457 is not an Armstrong number.
153 is an Armstrong number.