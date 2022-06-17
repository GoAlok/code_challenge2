"""
    Write a program that check whether the input number is odd or even.
    -- For doing so we have to use " MODULO OPERATOR = % it gives remainder."
"""

user_number = int(input("Please enter your number: "))

if (user_number % 2) != 1:
    print(f"You entered {user_number}, and it is an even number.")
else:
    print(f"You entered {user_number}, and it is an odd number.")
