#  ----------00:25) global scope vs local scope

name = 'Dave'  # global 'name' variable


def greeting(name):
    #  'name' is defined in the local scope
    print(f" Hello {name}")


greeting('Dave')


def greeting_2():
    # it is the global scope 'name' that is called
    print(f" Good morning {name}")


greeting_2()

#  ----------03:37) Parameters override globals of the same name

first_name = 'Dave'


def greeting_3(first_name):
    print(f" Good morning {first_name}")


greeting_3('Andreïa')

#  ----------04:45) Review of global vs local scope

""" done """


#  ----------05:13) Scope applies to functions, too

def my_func():
    x = 300

    def my_inner_func():
        print(x)

    my_inner_func()


my_func()
#  ----------06:14) Nested Functions

""" done """

#  ----------08:19) Why create Nested Functions?

""" done """

#  ----------09:42) The global keyword

x = 300


def my_func():
    global x
    x = 200


my_func()

print(x)

#  ----------13:09) The nonlocal keyword

x = 300


def my_func():
    color = "blue"
    global x
    x = 200

    def my_func_son():
        nonlocal color
        print(color)
        color = "red"
        print(color)

    my_func_son()


my_func()

print(x)

#  ----------14:23) Applying what we've learned


