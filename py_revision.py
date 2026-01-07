# TYPE CASTING
name=input("What is your name?:")
age=int(input("How yold are you?:"))
height=float(input("How tall are you?:"))

print("Hello"+name)
print("you're "+str(age)+"years old")
print("You are " +str(height)+"cm tall")

# MATH FUNCTIONS
import math 
pi=3.14
x=1
y=2
z=3

print(round(pi))
print(math.ceil(pi))
print(math.floor(pi))
print(abs(pi))
print(pow(pi,2))
print(math.sqrt(420))
print(max(x,y,z))


# slicing = create a substring by extracting elements from 
# another string indexing[] or slice()
# [start:stop:step]

name="Bro Code"

first_name= name[:3]
last_name=name[4:]
funky_name=name[::2]#//it will start from zero to end of string and skiping 2 characters
reversed_name=name[::-1]

print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)