"""
https://docs.python.org/3.11/library/argparse.html#module-argparse
https://docs.python.org/3.11/library/allos.html
https://docs.python.org/3.11/library/argparse.html
"""
greetings = {
    "English": "Hello",
    "Spanish": "Hola",
    "Germain": "Hallo",
}

# For testing


def hello_func(name, lang):
    msg = f"{greetings[lang]} {name} ! ;)"
    print(msg)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description="Provide a personal greeting.")
    parser.add_argument(
        "-n", "--name",
        metavar="name",
        required=True,
        help="The name of the person to great"
    )
    parser.add_argument(
        "-l", "--lang",
        metavar="language",
        required=True,
        choices=greetings.keys(),
        help="The language in which to greet"
    )
    args = parser.parse_args()
    hello_func(args.name, args.lang)

#  (04:22) Passing an argument at the command line

"""
python3 cla_1_script.py -h
python3 cla_1_script.py -n John
"""

#  (11:30) Personalizing Rock Paper Scissors

""" Done """

#  (12:09) Quick f-String update

""" Done """

#  (13:48) Applying command line arguments to RPS

""" Done """

#  (15:29) Refactoring to personalize output

""" Done """

#  (19:45) Playing the game

""" Done """