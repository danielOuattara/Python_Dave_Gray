
def func_builder(x):
    return lambda num: num + x


add_10 = func_builder(10)
print(add_10(11))

add_20 = func_builder(20)
print(add_20(-15))
