#Q.1) Arithmetic Operators i.e. +, -, , /, %, *(exponent), //(floor division)
#==========================================================================

def ex1():
	a = 10
	b = 3
	print(a+b)
	print(a-b)
	print(a*b)
    
	#print(a/b)
	#print(b/a)
	#print(a//b)
	#print(b//a)
    
	print(a%b)
	print(b%a)
	print(a**b)
    
ex1();

Output:
1
3
1000
#==========================================================================
# Q.2) Assignment operators i.e. =, +=, -=

def ex2():	
    c = 10
    #c+=1
    print(c)
    c += 3 #c = c + 3
    print(c)
    c -= 2 #c = c - 2
    print(c)
    
ex2(); 

Output:
10
13
11

#==========================================================================
# Q.3) Bitwise Operators->  &, |, ^
#==========================================================================

def ex7():
    a = 9  #1001
    b = 8  #1000
    print(bin(9))
    print(bin(8))
    print(a & b, bin(a & b))
    print(a | b, bin(a | b))
    print(a ^ b, bin(a ^ b))

ex7()

Output:

0b1001
0b1000
8 0b1000
9 0b1001
1 0b1

#==========================================================================
# Q.4 Write a program to calculate greatest of three numbers.

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
num3 = int(input("Enter 3rd number: "))

if num1 > num2 and num1> num3:
	print(num1, "Is Greatest number")
elif num2 > num1 and num2 > num3:
	print(num2, "Is greatest number")

else:
	print(num3, "Is greatest number")

Output:
Enter 1st number: 50
Enter 2nd number: 25
Enter 3rd number: 18
50 Is Greatest number

#==========================================================================
# Q.5 Calculate the area of a circle.


def area_circle(radius):
	area = 3.14 * radius ** 2
	print("Area of circle = ", area)

radius = float(input("Enter the radius: "))

if radius > 0.0:
	area_circle(radius)
else:
	print("Invalid radius")

Output:

Enter the radius: 12
Area of circle =  452.16

#==========================================================================
# Q.6)Calculate the area of a triangle.

def area_triangle(base,height):

	# calculate the semi-perimeter
	area = 1/2 * base * height
	return area

base = float(input("Enter base: "))
height = float(input("Enter height: "))


if base <=0 or height <=0:
	print("Invalid input: All sides must be positive numbers.")
else:
	area = area_triangle(base,height)
	print("The area of the triangle is ", round(area,2))

Output:

Enter base: 8
Enter height: 15
The area of the triangle is  60.0

#==========================================================================
# Q.7)Calculate the area of a rectangle.

def rectangle(width,height):
	area = width * height
	return area

width = float(input("enter width: "))
height = float(input("Enter height: "))

area = rectangle(width,height)
print("Area of rectangle is", round(area,2))

Output:

enter width: 20
Enter height: 30
Area of rectangle is 600.0

#==========================================================================
# Q.8)Calculate the area of a square.


def square(side):
	area = side * side
	return area

side = float(input("enter side: "))

area = square(side)
print("Area of Square is", round(area,2))

Output:
enter side: 6
Area of Square is 36.0