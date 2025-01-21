""" Python for loops """

print('----------------------------')

names = ['Dave', 'Sara', 'John']

for person in names:
    print(person)

print('----------------------------')

for x in 'Mississippi':
    print(x)

print('----------------------------')

for name in names:
    if name == 'Sara':
        break
    print(name)

print('----------------------------')

for name in names:
    if name == 'Sara':
        continue
    print(name)

print('----------------------------')

#  Range

for x in range(5):
    print(x)

print('-----')

for x in range(1, 5):
    print(x)

print('----------------------------')

#  Range: initial, final, increment

for x in range(0, 50, 5):
    print(x)

print('-----')

for x in range(0, 30, 3):
    print(x)

print('loop completed')

print('----------------------------')

#  Nested loop

names = ['Dave', 'Sara', 'John']
actions = ['code', 'talk', 'lead']

for name in names:
    for act in actions:
        print(f"{name} {act}")

print('-------')  # flipped nested loop

for act in actions:
    for name in names:
        print(f"{name} {act}")
