#  ----- (00:14) How We've Been Inserting Values into Strings

person = 'Dave'
coins = 3
print('1. ' + person + " has " + str(coins) + " coins left.")


#  ----- (01:21) Formatting with percent signs

message = '2. %s has %s coins left' % (person, coins)
print(message)


#  ----- (03:44) The .format() method

message = '3. {} has {} coins left' .format(person, coins)
print(message)

message = '4. {0} has {1} coins left' .format(person, coins)
print(message)

message = '5. {1} has {0} coins left' .format(coins, person)
print(message)

message = '6. {person} has {coins} coins left' .format(person=person, coins=coins)
print(message)

player = {'person': 'Dave', 'coins': 3}
message = '7. {person} has {coins} coins left' .format(**player)
print(message)

#  ----- (04:30) Why move on to f-Strings?

""" Done """

#  ----- (10:06) f-Strings examples

print(f'8. {person} has {coins} coins left in game.')

print(f'9. {person} has {2 * 3} coins left in game.')

print(f'10. {person.upper()} has {2 * 3} coins left in game.')

player = {'person': 'Dave', 'coins': 3}
print(f'11. {player["person"].upper()} has {2 * 3} coins left in game.')

#  ----- (13:38) Passing format options

num = 10
print(f"2.25 times {num} is {2.25 * num:.2f}")

for num in range(1, 11):
    print(f"2.25 times {num} is {2.25 * num:.2f}")

for num in range(1, 11):
    print(f"{num} divided by 4.52 is {num/4.52:.2%}")
#  ----- (18:43) Updating Rock Paper Scissors with f-Strings

