#  (00:14) An Example of a Built-In Module

import math
from math import pi
import sys
import random
import random as rand
import kansas_module
from rps_script import rock_paper_scissors

print(math.pi)
print(f'pi = {math.pi}')

#  (01:55) Modules We Have Used
random_numb = random.choice('12345')
print(f'random_num = {random_numb}')

#  (02:33) Import from

from enum import Enum

print(f'pi = {pi}')

#  (03:35) Creating Aliases

random_str = rand.choice('abcde')
print(f'random_str = {random_str}')

#  (03:57) Module Contents with dir()

print(f"{dir(random)}")

print('----------------------------------------')

for item in dir(random):
    print(item)
#  (05:21) Module Contents with dot notation

# random.  # to see all available elements
#  (05:39) Python Module Index

"""
visit : 
https://docs.python.org/3.11/index.html

https://docs.python.org/3.11/py-modindex.html 

https://docs.python.org/3.11/library/enum.html#module-enum

"""

print('----------------------------------------')

#  (06:35) Custom Modules

print(kansas_module.capital)
kansas_module.random_funfact()

#  (09:36) if _name_ == "__main__"

""" 
Every module has a __name__ variable
"""
print(__name__)  # __main__
print(kansas_module.__name__)  # kansas_module

#  (15:10) Making a Rock Paper Scissors module

rock_paper_scissors()
