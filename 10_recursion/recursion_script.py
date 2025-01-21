#  (00:13) What is Recursion ?

""" It happens when a function calls itself """


#  (00:34) Create a Recursive Function

def add_one(num):
    if num >= 9:
        return num + 1

    total = num + 1
    print(f"num = {num}, total = {total}")
    return add_one(total)


my_total = add_one(0)
print(f'\nmy_total = {my_total}\n')

print('-----------')  # (02:45) Return the Recursive Function Call


def add_one_2(num):
    if num >= 9:
        return num

    total = num + 1
    return add_one_2(total)


total_2 = add_one_2(0)
print(total_2)

#  ---------  (04:23) Recursion vs Loops

""" tyr if necessary """

#  ---------  (04:57) Review of While Loop Conditions

""" see detail_script.py"""

#  --------- (09:13) Refactor RPS to a function

""" see rps_script_15.py """

#  --------- (11:03) Refactor RPS to a recursive function

""" see rps_script_15.py """
