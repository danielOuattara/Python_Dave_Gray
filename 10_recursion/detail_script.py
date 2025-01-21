value = True

while value:
    print(value)
    value = False

while value:
    print(value)
    value = 0


value = "y"
count = 0

while value:
    count += 1
    print(count)
    if count == 5:
        break
    else:
        value = 0
        continue
