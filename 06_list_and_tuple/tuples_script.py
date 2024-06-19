# Tuples

my_tuple = tuple(('Dave', 42, True))
print('my_tuple = ', my_tuple)
print('type(my_tuple', type(my_tuple))  # <class 'tuple'>

my_tuple_2 = ('Dave', 42, True)
print('my_tuple_2 = ', my_tuple_2)
print('type(my_tuple_2', type(my_tuple_2))  # <class 'tuple'>

#  If you do need to change a tuple

my_list = list(my_tuple)
my_list.append('Cheese')
my_tuple = tuple(my_list)
print('my_tuple = ', my_tuple)

#  Unpacking a tuple

(one, two, *hey) = my_tuple
print(one, '\n', two, '\n', hey)

(one, *two, hey) = my_tuple
print(one, '\n', two, '\n', hey)

(*one, two, hey) = my_tuple
print(one, '\n', two, '\n', hey)

#  Using dot notation to find methods available

# my_tuple.
