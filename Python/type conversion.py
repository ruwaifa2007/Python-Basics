# Type conversion is a concept in python that allows you to convert one data type into another.
 
# There are two types of type conversion in python: implicit and explicit type conversion.

#implicit type conversion is done by python automatically when you perform operations on different data types.

# 1. implicit type conversion

a=3.45798 # this is a float variable
b=35 # this is an integer variable
print(a+b) # displays the sum of a and b, which is 38.45798

#explicit type conversion is done by the programmer using built-in functions like int(), float(), str(), etc.

# 2. explicit type conversion

x="10" # this is a string variable
print(type(x)) #displays the type of variable x
y=int(x) # changing the type of variable x from string to integer
print(type(y)) #displays the type of variable y
print(y) # displays the value of variable y
