"""
x : create
r : read
a : append
w : write

"""

import os


file = open('names.txt')
print(f'{file.read()}\n')
file.close()


file = open('names.txt')
print(f'{file.read(9)}\n')
file.close()


file = open('names.txt')
print(f'{file.readline()}')
print(f'{file.readline()}\n')
file.close()


file = open('names.txt')
print(f'{file.readlines()}')
file.close()


file = open('names.txt')
for line in file:
    print(f'{line}')
file.close()

# -----------------------------------------

try:
    file = open('not_exist.txt')
    print(file.read())
    file.close()
except:
    print('\nFileNotFoundError: file requested does not exists\n')


try:
    file = open('names.txt')
    print(file.read())
    file.close()
except:
    print('\nfile requested does not exists')


# -------------------------------------------

# Appending: creating the file if not exists

file = open('names.txt', 'a')
file.write('\nJerry Rowlinks')
file.close()

file = open('names.txt')
for line in file:
    print(f'{line}')
file.close()


# -------------------- Write / Overwrite files

# write: creating the file if not exists, overwrite existing content

file = open('content.txt', 'w')
file.write('\nThe content of this file is always overwritten with this new')
file.close()

file = open('content.txt')
for line in file:
    print(f'{line}')
file.close()


# ---------------------- Two Ways to Create Files
file = open('name_list.txt', "w")
file.close()


path = 'john_doe.txt'
if not os.path.exists(path):
    file = open(path, "x")
    file.close()

# 1
if os.path.exists(path):
    os.remove(path)

else:
    print(f'\nFile {path} Not Found\n')

# 2
if os.path.exists(path):
    os.remove(path)

else:
    print(f'\nFile {path} Not Found\n')

# ----------------------- with keyword


with open('names.txt') as file:
    new_content = file.read()

with open('name_list.txt', "w") as file:
    file.write(new_content)
