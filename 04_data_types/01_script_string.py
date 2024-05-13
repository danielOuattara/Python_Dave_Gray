# string literal assignment
first_name = "John"
last_name = "Doe"

print(type(first_name))  #  <class 'str'>
print(type(first_name) == str)  # True
print(isinstance(first_name, str))  # True

# string constructor function
pizza_name = str("Pepperoni")
print(type(pizza_name))  #  <class 'str'>
print(type(pizza_name) == str)  # True
print(isinstance(pizza_name, str))  # True

# string concatenation
fullname = first_name + " " + last_name
print(fullname)

fullname += " Spencer"
print(fullname)


# casting to string
decade = str(70)
print(decade)
print(type(decade))

# concatenation
statement = "I like rock music from the " + decade + "'s."
print(statement)


# multi lines
multi_line = '''
hello my name is :
John Doe
How are you ?

'''

print(multi_line)


# escaping special characters
sentence = 'I\'m a man \\ I\'m a woman.\n\tNOTHING ELSE'
print(sentence)


# method on string
print(first_name)
print(first_name.lower())
print(first_name.upper())
print(first_name)

print(multi_line.title())
print(multi_line.replace("John", "Max"))
print(multi_line)

print(len(multi_line))
multi_line += "                   "

multi_line = "                   " + multi_line
print(multi_line)
print(len(multi_line))

print(len(multi_line.strip()))
print(len(multi_line.lstrip()))
print(len(multi_line.rstrip()))

# read the officials documentation about 'string' methods to learn more

print("-" * 80)
print(" ")

# built a menu
title = " menu ".upper()
print(title.center(20, "="))
print("Coffee".ljust(16, ".") + "$1" . rjust(4))
print("Muffin".ljust(16, ".") + "$2" . rjust(4))
print("Cheese Cake".ljust(16, ".") + "$4" . rjust(4))

'''
======= MENU =======
Coffee..........  $1
Muffin..........  $2
Cheese Cake.....  $4
'''


# string index value

print(first_name[1])  # 2nd value
print(first_name[-1])  # last value
print(first_name[-1: 5])  # range

# string method that return boolean data

print(first_name.startswith("J"))  # True
print(first_name.startswith("W"))  # False
print(first_name.endswith("W"))  # False
