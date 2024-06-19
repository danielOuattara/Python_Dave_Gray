# int literal assignment

import math

my_int = 34
print(my_int)  # True
print(type(my_int))

# int constructor function

my_int_2 = int(23)
print(my_int_2)  # False
print(type(my_int_2))  # <class 'int'>
print(isinstance(my_int_2, int))  # True


# float literal assignment

my_float = 34.0
print(my_float)  # True
print(type(my_float))

# float constructor function

my_float_2 = float(23)
print(my_float_2)  # False
print(type(my_float_2))  # <class 'float'>
print(isinstance(my_float_2, float))  # True


# complex literal assignment

my_complex = 2 + 4.0j
print(my_complex)  #
print(type(my_complex))

# complex constructor function

my_complex_2 = complex(1-5j)
print(my_complex_2)  #
print(type(my_complex_2))  # <class 'complex'>
print(isinstance(my_complex_2, complex))  # True
print(my_complex_2.real)  # 1.0
print(my_complex_2.imag)  # -5.0
print(my_complex_2.conjugate())  # (1+5j)


# built-in method for number

"""
abs(), 
round(),
etc...
"""

print(math.pi)  # 3.14159....
print(math.sqrt(64))  # 8.0
print(math.ceil(3.67))  # 4
print(math.floor(3.67))  # 3


# casting a string to a number

zip_value = "77340"
print(zip_value)

zip_code = int(zip_value)
print(zip_code)

# Error if you cast incorrect data
