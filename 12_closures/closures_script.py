#  (00:58) What is Closure?

"""
Closure is a function having access to the scope of
its parent function after the parent function has return

ChatGPT:

A closure is a feature in programming languages where
an inner function has access to the outer (enclosing)
function's variables, even after the outer function
has finished executing.

Closures are often used to create private variables or
to remember the state between function calls.

Closures are powerful tools for maintaining state and
creating functions with private variables.
"""


#  (01:47) An Example of Closure


def parent_func(person):
    coins = 3

    def play_game():
        nonlocal coins
        coins -= 1

        if coins > 1:
            print(f"{person} has {coins} coins left")
        elif coins == 1:
            print(f"{person} has {coins} coin left")
        else:
            print(f"{person} is out of coin")

    return play_game


tommy = parent_func('Tommy')
tommy()
tommy()

jenny = parent_func('Jenny')
jenny()

tommy()

#  (08:47) Revisiting the Closure Definition

""" done """
print("\n------------------------------------")


#  (09:37) Using a parameter value

def parent_func_2(person, coins):
    def play_game():
        nonlocal coins
        coins -= 1

        if coins > 1:
            print(f"{person} has {coins} coins left")
        elif coins == 1:
            print(f"{person} has {coins} coin left")
        else:
            print(f"{person} is out of coin")

    return play_game


tommy = parent_func_2('Tommy', 3)
tommy()
tommy()
tommy()

jenny = parent_func_2('Jenny', 3)
jenny()


print("\n------------------------------------")


def outer_function():
    outer_variable = 'I am outside!'

    def inner_function():
        print(outer_variable)  # inner_function has access to outer_variable

    return inner_function


my_inner_function = outer_function()
my_inner_function()  # prints: I am outside!

print("\n------------------------------------")

#  (10:43) Closures help you avoid globals

""" Done """

#  (11:09) Applying closures to Rock-Paper-Scissors

""" Done """