#Question 1
input_string = "Python is a case sensitive language"
#a
length=len(input_string)
print(length)
#b
reverse = input_string[::-1]
print(reverse)
#c
new_string = input_string[10:26]
print(new_string)
#d
replacement = input_string.replace("a case sensitive", "an object oriented")
print(replacement)
#e
index = input_string.find("a")
print("The index of 'a' is: {}".format(index))
#f
remove_whitespaces = input_string.replace(" ", "")
print(remove_whitespaces)

#Question 2
name = "Faraz Rahman"
sid = 21104024
department = "EE"
cgpa = 10
print("Hey, {} here!".format(name))
print("My SID is {}".format(sid))
print("I am from {} department and my CGPA is {}".format(department, cgpa))

#Question 3
a = 56
b = 10
#a
a_and_b = a&b
print("Result of the AND operation on a and b: {}".format(a_and_b))
#b
a_or_b = a|b
print("Result of the OR operation on a and b: {}".format(a_or_b))
#c
a_xor_b = a^b
print("Result of the XOR operation on a and b: {}".format(a_xor_b))
#d
left_shift_a = a<<2
left_shift_b = b<<2
print("Result of left shifting a: {}".format(left_shift_a))
print("Result of left shifting b: {}".format(left_shift_b))
#e
right_shift_a = a>>2
right_shift_b = b>>4
print("Result of right shifting a: {}".format(right_shift_a))
print("Result of right shifting b: {}".format(right_shift_b))

#Question 4
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))
if(x>y and x>z):
    print("{} is the greatest number".format(x))
elif(y>x and y>z):
    print("{} is the greatest number".format(y))
else:
    print("{} is the greatest number".format(z))

#Question 5
input_string = str(input("Enter a string: "))
if(input_string.find("name")>-1):
    print("Yes")
else:
    print("No")

#Question 6
x = int(input("Enter first side: "))
y = int(input("Enter second side: "))
z = int(input("Enter third side: "))
if(x<y+z and y<x+z and z<x+y):
    print("{}, {} and {} are possible sides of a triangle".format(x, y, z))
else:
    print("{}, {} and {} are not possible sides of a triangle".format(x,y,z))
