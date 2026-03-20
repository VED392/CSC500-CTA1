def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error: Division by zero is not allowed."
#part 1 adding and subtracting
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2
#make sure it only accepts numbers and not letters or symbols
def get_number(prompt):
    """Gets a valid number from the user."""
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
#part1
def addnsub():
    print("This program will add and subtract two numbers.\n")

    # Get user input
    first_number = get_number("Enter the first number: ")
    second_number = get_number("Enter the second number: ")

    # Perform calculations
    sum_result = add(first_number, second_number)
    difference_result = subtract(first_number, second_number)

    # Display results
    print("\nResults:")
    print("Sum:", sum_result)
    print("Difference:", difference_result,"\n")
#part2
def mulndiv():
    print("This program will multiply and divide two numbers.\n")

    # Get user input
    first_number = get_number("Enter the first number: ")
    second_number = get_number("Enter the second number: ")

    # Perform calculations
    product_result = multiply(first_number, second_number)
    quotient_result = divide(first_number, second_number)

    # Display results
    print("\nResults:")
    print("Product:", product_result)
    print("Quotient:", quotient_result)

# Call the main funct
addnsub()
mulndiv()

