def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error: Division by zero is not allowed."

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def get_number(prompt):
    """Gets a valid number from the user."""
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

# Part 1: Add and Subtract
def addnsub():
    print("\nThis program will add and subtract two numbers.\n")

    first_number = get_number("Enter the first number: ")
    second_number = get_number("Enter the second number: ")

    print("\nResults:")
    print("Sum:", add(first_number, second_number))
    print("Difference:", subtract(first_number, second_number))

# Part 2: Multiply and Divide
def mulndiv():
    print("\nThis program will multiply and divide two numbers.\n")

    first_number = get_number("Enter the first number: ")
    second_number = get_number("Enter the second number: ")

    print("\nResults:")
    print("Product:", multiply(first_number, second_number))
    print("Quotient:", divide(first_number, second_number))

# Test Cases Function 
def run_tests():
    print("\nRunning Test Cases...\n")

    test_cases = [
        (10, 5),
        (-8, 2),
        (5.5, 2.2),
        (0, 7),
        (10, 0)
    ]

    for num1, num2 in test_cases:
        print("Testing with:", num1, "and", num2)

        print("Sum:", add(num1, num2))
        print("Difference:", subtract(num1, num2))
        print("Product:", multiply(num1, num2))
        print("Quotient:", divide(num1, num2))
        print("-" * 30)

# Main function (Top-down design)
def main():
    print("Welcome to the Simple Calculator")
    print("1. Add and Subtract")
    print("2. Multiply and Divide")
    print("3. Run Test Cases")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        addnsub()
    elif choice == "2":
        mulndiv()
    elif choice == "3":
        run_tests()
    else:
        print("Invalid choice.")

# Program start
main()