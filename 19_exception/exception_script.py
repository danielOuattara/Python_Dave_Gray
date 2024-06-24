print('--------------------------- 0')
#  ------------- (00: 43) What is an Exception?

print('print first exception: no control over it')
# print(x)

#  ------------- (01: 32) Python Built-in Exceptions
print('--------------------------- 1')

print('print list of some Exception in Python')
# path = 'exception_table.md'
# file = open(path)

# for item in file:
#     print(item.strip())


#  ------------- (02: 10) try & except

# generic cath


print('--------------------------- 2')

try:
    print(x)

except:
    print('There is an error')

print('--------------------------- 3')

#  ------------- (03: 19) Handling specific exceptions


try:
    print(x)

except NameError:
    print('NameError: value is undefined')


try:
    print(10 / 0)

except ZeroDivisionError as e:
    print('ZeroDivisionError: division by zero is not allowed here')

print('--------------------------- 4')

#  ------------- (05: 10) else & finally

try:
    print(x)

except NameError:
    print('NamError')


finally:
    print('# Finally : Watching for NameError completed')

value = 2
result = 0
try:
    result = value / 2

except ZeroDivisionError:
    print('ZeroDivisionError: division by zero')

else:
    print(f'Else : No error\nresult = {result}')


finally:
    print('# Finally : Watching for ZeroDivisionError completed')

print('--------------------------- 5')


#  ------------- (07: 13) except Exception as error

try:
    x = None
    print(x)

    value = 2
    result = 0
    result = value / 2
except NameError:
    print('NamError')

except ZeroDivisionError:
    print('ZeroDivisionError: division by zero')

except Exception as e:
    print(f'An Exception raised: {e}')

else:
    print(f'Else : No error\nresult = {result}')


finally:
    print('# Finally : Watching for ZeroDivisionError completed')

print('--------------------------- 6')
#  ------------- (09: 16) Custom Exceptions


class CustomException(Exception):
    pass


try:
    raise CustomException('I am a build in custom exception')

    raise Exception('I am a custom exception')
    x = None
    print(x)

    if type(x) is not int:
        raise TypeError('x is not an integer')
    value = 2
    result = 0
    result = value / 2
except NameError:
    print('NamError')

except ZeroDivisionError:
    print('ZeroDivisionError: division by zero')

except Exception as e:
    print(f'An Exception raised: {e}')

else:
    print(f'Else : No error\nresult = {result}')


finally:
    print('# Finally : Watching for ZeroDivisionError completed')

print('--------------------------- 7')
