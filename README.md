START

FUNCTION multiply(num1, num2)
    RETURN num1 * num2
END FUNCTION

FUNCTION divide(num1, num2)
    IF num2 is not equal to 0 THEN
        RETURN num1 / num2
    ELSE
        RETURN "Error: Division by zero is not allowed."
    ENDIF
END FUNCTION

FUNCTION add(num1, num2)
    RETURN num1 + num2
END FUNCTION

FUNCTION subtract(num1, num2)
    RETURN num1 - num2
END FUNCTION

FUNCTION get_number(prompt)
    REPEAT
        DISPLAY prompt
        INPUT value
        IF value is a valid number THEN
            RETURN value
        ELSE
            DISPLAY "Invalid input. Please enter a numeric value."
        ENDIF
    UNTIL valid input is received
END FUNCTION

FUNCTION addnsub()
    DISPLAY "This program will add and subtract two numbers"

    SET first_number = get_number("Enter the first number: ")
    SET second_number = get_number("Enter the second number: ")

    DISPLAY "Sum:", add(first_number, second_number)
    DISPLAY "Difference:", subtract(first_number, second_number)
END FUNCTION

FUNCTION mulndiv()
    DISPLAY "This program will multiply and divide two numbers"

    SET first_number = get_number("Enter the first number: ")
    SET second_number = get_number("Enter the second number: ")

    DISPLAY "Product:", multiply(first_number, second_number)
    DISPLAY "Quotient:", divide(first_number, second_number)
END FUNCTION

FUNCTION run_tests()
    SET test_cases = [(10,5), (-8,2), (5.5,2.2), (0,7), (10,0)]

    FOR each pair (num1, num2) in test_cases
        DISPLAY "Testing with:", num1, "and", num2

        DISPLAY "Sum:", add(num1, num2)
        DISPLAY "Difference:", subtract(num1, num2)
        DISPLAY "Product:", multiply(num1, num2)
        DISPLAY "Quotient:", divide(num1, num2)

        DISPLAY "----------------------"
    ENDFOR
END FUNCTION

FUNCTION main()
    DISPLAY "Welcome to the Simple Calculator"
    DISPLAY "1. Add and Subtract"
    DISPLAY "2. Multiply and Divide"
    DISPLAY "3. Run Test Cases"

    INPUT choice

    IF choice = "1" THEN
        CALL addnsub()
    ELSE IF choice = "2" THEN
        CALL mulndiv()
    ELSE IF choice = "3" THEN
        CALL run_tests()
    ELSE
        DISPLAY "Invalid choice"
    ENDIF
END FUNCTION

CALL main()

STOP