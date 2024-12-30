#1
try:
    num = int(input("Enter a positive number: "))
    if num < 0:
        raise ValueError("The integer cannot be a negative number.")
except ValueError as ve:
    print("Caught an exception:", ve)
finally:
    print("Execution done!")