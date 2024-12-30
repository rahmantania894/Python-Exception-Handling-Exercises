#3
try:
    age = int(input("Enter your age: "))
    if age < 18 or age > 45:
        raise ValueError("Age must be between 18 and 45.")
except ValueError as ve:
    print("Caught an exception:", ve)
finally:
    print("Execution done!")
