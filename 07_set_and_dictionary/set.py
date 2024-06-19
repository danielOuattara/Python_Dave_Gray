nums = {1, 2, 3, 4}
nums_2 = set((1, 2, 3, 4))

print('nums = ', nums)
print('nums_2 = ', nums_2)

print('type(nums) = ', type(nums))  # <class 'set'>
print('len(nums) = ', len(nums))  # 4

#  No duplicate

nums = {1, 2, 3, 4, 2}
print('nums = ', nums)  # {1, 2, 3, 4}

#  True is a dupe of 1, False is a dupe of 0
nums = {1, True, 2, False, 3, 4, 0}
print('nums = ', nums)  # {False, 1, 2, 3, 4}

#  Check if a value is in a set

print(2 in nums)  # True

#  NOTE: No indexed
#  cannot refer to an element in the
#  set with an index position or a key


#  Add a new element

nums.add(5)
print('nums = ', nums)

#  Update the set with the union of this set and others.

more_nums = {6, 7, 8}
nums.update(more_nums)
print('nums = ', nums)  # {False, 1, 2, 3, 4, 5, 6, 7, 8}

#  Update with lists, tuples and dictionaries

nums.update((7, 8, 9, 10))
print('nums = ', nums)
nums.update({'A': 'a', 'B': 'b'})
print('nums = ', nums)
nums.update([11, 12, 12, 13, 14])
print('nums = ', nums)

#  Union of sets

one = {1, 2, 3}
print(one)
two = {4, 5, 6}
print(two)

union_1 = one.union(two)
print("union_1 = ", union_1)

print(one)
print(two)

#  Intersection of sets: keep only duplicates

one = {1, 2, 3, 7}
print(one)
two = {2, 4, 5, 7}
print(two)

intersect_1 = one.intersection(two)
print("intersect_1 = ", intersect_1)  # {2, 7}

print(one)
print(two)

#  Keep everything except the duplicates

one = {1, 2, 3, 7}
print(one)
two = {2, 4, 5, 7}
print(two)

one.symmetric_difference_update(two)
print(one)
