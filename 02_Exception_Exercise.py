#2
try:
    num = int(input("Enter an odd number: "))
    if num % 2 == 0:  # Check if the number is even
        raise ValueError("The integer cannot be an even number.")
except ValueError as ve:
    print("Caught an exception:", ve)
finally:
    print("Execution done!")