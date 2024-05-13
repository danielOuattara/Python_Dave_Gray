"""
Python divides the operators in the following groups:
     > Arithmetic operators
     > Assignment operators
     > Comparison operators
     > Logical operators
     > Identity operators
     > Membership operators
     > Bitwise operators
"""

quantity = 42
print("")

if quantity > 10:
    print("Greater")
else:
    print("Lower")

# ternary equivalent
print("Greater than 10") if quantity > 10 else print("Lower than 10")