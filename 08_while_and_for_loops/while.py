""" While loops in Python"""

print('--------------------------')

value_1 = 1
while value_1 < 10:
    print(value_1)
    value_1 += 1

print('--------------------------')

value_2 = 1
while value_2 < 10:
    print(value_2)
    if value_2 == 5:
        break
    value_2 += 1

print('--------------------------')

value_3 = 1
while value_3 < 10:
    value_3 += 1
    if value_3 == 5:
        continue
    print(value_3)

print('--------------------------')

value_4 = 1
while value_4 < 10:
    value_4 += 1
    if value_4 == 5:
        continue
    print(value_4)
else:
    print("Out of while loop")

print('--------------------------')
