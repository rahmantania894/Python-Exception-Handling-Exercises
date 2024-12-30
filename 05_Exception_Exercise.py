#5
try:
    user_input = input("Enter a string: ")
    if len(user_input) < 6:
        raise ValueError("String must have at least 6 characters.")
except ValueError as ve:
    print("Caught an exception:", ve)
finally:
    print("Execution done!")

