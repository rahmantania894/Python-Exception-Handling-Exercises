#4
try:
    num = int(input("Enter a number in the range from 1 to 70: "))
    if not (1 <= num <= 70):
        raise ValueError("The number must be between 1 and 70.")
except ValueError as ve:
    print("Caught an exception:", ve)
finally:
    print("Execution done!")