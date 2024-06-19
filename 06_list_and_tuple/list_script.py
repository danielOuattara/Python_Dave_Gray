#  What are lists ?

users = ['Dave', 'John', 'Sara']
data = ['Dave', 42, True]  # mixed data type
empty_list = []

#  Check for a value in a list

print("'Dave' in users : ", 'Dave' in users)  # True
print("'Dave' in data : ", 'Dave' in data)  # True
print("'Dave' in empty_list : ", 'Dave' in empty_list)  # False

#  Retrieve a list value by index

print(users[0])  # 'Dave'
print(users[-1])  # 'Sara'
print(users[-2])  # 'John'
print(users[-3])  # 'Dave'
# print(users[-4])  # 'Dave' # IndexError: list index out of range
print(users.index('Sara'))  # 2
#  print(users.index('sara')) # ValueError: 'sara' is not in list

#  Retrieve a range of list index

print(users[0: 2])  # ['Dave', 'John']
print(users[1:])  # ['John', 'Sara']
print(users[-3: -1])  # ['Dave', 'John']

#  Get the length of a list

print('len(data) = ', len(data))

# Appending items to a list

users.append('Elsa')
print('users = ', users)

users += ['Jason']  # caution: appending/extending element MUST be a list
print('users = ', users)

users.extend(['Robert', 'Jimmy'])  # extends by a new list
print('users = ', users)

# users.extend(data)  # extends by a predefined list
# print('users = ', users)

#  inserting values in a list at specified  index

users.insert(0, 'Bob')
print('users = ', users)

# insert without replacement

users[2:2] = ['Eddie', 'Alex']
print('users = ', users)

# insert by replacing

users[1:3] = ['Robert', 'JPJ']
print('users = ', users)

#  removing, deleting, clearing

users.remove('Bob')
print('users = ', users)

# users.remove('Dinosaur') #  ValueError: list.remove(x): x not in list
# print('users = ', users)

# Remove and return item at index (default last)
print(users.pop())
print('users = ', users)

# delete

del users[0]
print('users = ', users)

#  del data
#  print(data)  # NameError: name 'data' is not defined

data.clear()
print('data = ', data)  # []

#  Sorting list

users.sort()
print('users = ', users)

users[1:2] = ['dave']
print('users = ', users)

users.sort()
print('users')

users.sort(key=str.lower)
print('users = ', users)

numbers = [4, 43, 78, 1, 5]
numbers.reverse()
print('numbers = ', numbers)

numbers.sort()
print('numbers = ', numbers)

# numbers.sort(reverse=True)
# print('numbers = ', numbers)

print(sorted(numbers, reverse=True))

#  copying list

numbers_copy = numbers.copy()
print(numbers_copy)

numbers_copy_2 = list(numbers)
print(numbers_copy_2)

numbers_copy_3 = numbers[:]
print(numbers_copy_3)

#  List constructor and data type

print('type(numbers) = ', type(numbers))

new_list = list((1, 'Neil', True))
print('new_list = ', new_list)

new_list_2 = list([1, 'Neil', True])
print('new_list_2 = ', new_list_2)

#  Using dot notation to find methods available

# users.
