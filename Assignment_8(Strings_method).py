#1. Write a Python program to Count all letters, digits, and special symbols from the given string
# Output: Chars = 8 Digits = 3 Symbol = 4 

Input = "P@#yn26at^&i5ve"

l , d, sy= 0, 0, 0
 

for i in Input:
	if i.isalpha():
		l= l + 1
	elif i.isdigit():
		d= d + 1
	else:
		sy = sy + 1
print("Chars = ",l, "Digit = ",d,"Symbol = ", sy)

Output
Chars =  8 Digit =  3 Symbol =  4
-------------------------------------------------------------------------------------------------------------------------

#2. Write a Python program to remove duplicate characters of a given string.
# Output: String and Function 


def remove_duplicates(Input):
	seen = set()
	final_list = []
	for char in Input:
		if char not in seen:
			final_list.append(char)
			seen.add(char)
	return ''.join(final_list)

Input = "String and String Function"
output = remove_duplicates(Input)
print("Duplicates are: ", output)

Output:
Duplicates are:  String adFuco
-------------------------------------------------------------------------------------------------------------------------

# 3. Write a Python program to count Uppercase, Lowercase, special character and numeric values in a given string
# Output: UpperCase : 5 LowerCase : 18 NumberCase : 5 SpecialCase : 11 


Input = "Hell0 W0rld ! 123 * # welcome to pYtHoN"

u, l, sc, n = 0,0,0,0

for i in Input:
	if i.isupper():
		u = u + 1
	elif i.islower():
		l = l + 1
	elif i.isdigit():
		n = n + 1
	else:
		sc = sc + 1
print("Uppercase: ", u, "Lowercase: ", l, "Numbercase: ", n, "Specialcase: ", sc)

Output:
Uppercase:  5 Lowercase:  18 Numbercase:  5 Specialcase:  11
-------------------------------------------------------------------------------------------------------------------------

# 4. Write a Python Count vowels in a string 
#Output: Total vowels are: 8


Input= "Welcome to Python Assignment"

vowels = 'aeiouAEIOU'
count = 0

for char in Input:
	if char in vowels:
		count = count + 1

print("Total Vowels: ", count)

Output:
Total Vowels:  8
-------------------------------------------------------------------------------------------------------------------------
