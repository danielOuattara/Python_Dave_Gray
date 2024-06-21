import argparse

#  (00:26) argparse module

"""
https://docs.python.org/3.11/library/argparse.html#module-argparse

https://docs.python.org/3.11/library/allos.html

https://docs.python.org/3.11/library/argparse.html


The argparse module makes it easy to write user-friendly 
command-line interfaces. The program defines what arguments 
it requires, and argparse will figure out how to parse those 
out of sys.argv. 

The argparse module also automatically generates help and 
usage messages. The module will also issue errors when users 
give the program invalid arguments.

Core Functionality

The argparse module's support for command-line interfaces is 
built around an instance of argparse.ArgumentParser. 

It is a container for argument specifications and has options 
that apply the parser as whole:

parser = argparse.ArgumentParser(
                    prog='ProgramName',
                    description='What the program does',
                    epilog='Text at the bottom of help')

The ArgumentParser.add_argument() method attaches individual 
argument specifications to the parser. It supports positional 
arguments, options that accept values, and on/off flags:

parser.add_argument('filename')           # positional argument
parser.add_argument('-c', '--count')      # option that takes a value
parser.add_argument('-v', '--verbose',
                    action='store_true')  # on/off flag


The ArgumentParser.parse_args() method runs the parser and places 
the extracted data in a argparse.Namespace object:

args = parser.parse_args()
print(args.filename, args.count, args.verbose)

...etc...
"""

#  (01:25) Example 1

parser = argparse.ArgumentParser(description="Provide a personal greeting.")

parser.add_argument(
    "-n",
    "--name",
    metavar="name",
    required=True,
    help="The name of the person to great"
)

args = parser.parse_args()
message = f"Hello {args.name} !"
print(message)

#  (04:22) Passing an argument at the command line

"""
python3 cla_1_script.py -h
python3 cla_1_script.py -n John
"""


#  (05:57) Example 2

""" See cla_2_script.py"""

#  (11:30) Personalizing Rock Paper Scissors


#  (12:09) Quick f-String update


#  (13:48) Applying command line arguments to RPS


#  (15:29) Refactoring to personalize output


#  (19:45) Playing the game
