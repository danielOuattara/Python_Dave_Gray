
# square = lambda number: number ** 2
from functools import reduce
def square(number): return number ** 2


numbers_list = [3, 7, 12, 18, 20, 21]


#  ----------------  map

square_numbers = map(lambda number: number ** 2, numbers_list)
print(list(square_numbers))  # [9, 49, 144, 324, 400, 441]


# ----------------- filter

# lambda number: number % 2 != 0
lambda number: number % 2 != 0


check_odds = filter(lambda number: number % 2 != 0, numbers_list)
print(list(check_odds))  # [3, 7, 21]


#  ---------------- reduce


total = reduce(lambda acc, curr: acc + curr, numbers_list, 0)
print(total)  # 81


lambda acc, curr: acc + len(curr)

names_list = ['Dave Gray', 'Mike Tyson Robinson',
              'Moroango Issouf Talba Joseph']

print([len(item) for item in names_list])

total_chars_in_list = reduce(lambda acc, curr: acc + len(curr), names_list, 0)
print(total_chars_in_list)
