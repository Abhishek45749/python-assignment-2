# even_or_odd.py

def check_even_odd():
    try:
        number = int(input("Please enter a number: "))
        if number % 2 == 0:
            print(f"The number {number} is even.")
        else:
            print(f"The number {number} is odd.")
    except ValueError:
        print("Oops! That doesn't look like a valid number. Please try again.")

check_even_odd()
