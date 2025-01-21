""" Function in Python """

#  -----  Defining function

#  -----  Naming fun

#  -----  (00:13) What are functions?


def hello():
    print('Hello World of Python')


hello()


#  -----  (01:35) Naming functions

def hello_world():
    print('Hello World of Python')


hello_world()


#  -----  (02:20) Parameters vs Arguments


def sum_1(number1, number2):
    print(number1 + number2)


sum_1(3, 5)  # 8
sum_1(1, 7)  # 8
sum_1(100, 3)  # 103


#  -----  (04:28) Return keyword

def sum_2(number1, number2):
    return number1 + number2


print(sum_2(3, 5))  # 8
print(sum_2(1, 7))  # 8
print(sum_2(100, 3))  # 103


#  -----  (05:27) Checking Argument types

def sum_3(number1, number2):
    if type(number1) is not int or type(number2) is not int:
        return
    return number1 + number2


# Better than above
def sum_3_2(number1, number2):
    if not isinstance(number1, int) or not isinstance(number2, int):
        return
    return number1 + number2


print(sum_3('3', 5))  # None
print(sum_3(1, 7))  # 8
print(sum_3(100, 3))  # 103


#  -----  (07:25) Default Parameter Values

def sum_4(number1=0, number2=0):
    if not isinstance(number1, int) or not isinstance(number2, int):
        return
    return number1 + number2


print(sum_4())  # No argument provided

#  -----  (09:06) Reviewing the Sum Function

# DONE


#  -----  (10:16) Receiving an Unknown Number of args

def multiple_items(*args):
    print(args)
    print(type(args))  # <class 'tuple'>


multiple_items('Dave', 'John', 'Sara', 1, True)


#  -----  (12:26) Receiving an Unknown Number of kwargs

def multiple_items_2(**kwargs):
    print(kwargs)
    print(type(kwargs))  # <class 'dict'>


multiple_items_2(dave='Dave', john='John', sara='Sara',
                 quantity=1, isFather=True)
