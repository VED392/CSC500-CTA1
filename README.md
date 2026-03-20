CTA1
DISPLAY "This program will add and subtract two numbers"

FUNCTION get_number(prompt)
    REPEAT
        DISPLAY prompt
        INPUT user_value
        IF user_value is a valid number THEN
            RETURN user_value
        ELSE
            DISPLAY "Invalid input. Please enter a numeric value."
        ENDIF
    UNTIL valid input is received
END FUNCTION

FUNCTION add(num1, num2)
    RETURN num1 + num2
END FUNCTION

FUNCTION subtract(num1, num2)
    RETURN num1 - num2
END FUNCTION

MAIN PROGRAM
    SET first_number = get_number("Enter the first number: ")
    SET second_number = get_number("Enter the second number: ")

    SET sum_result = add(first_number, second_number)
    SET difference_result = subtract(first_number, second_number)

    DISPLAY "Results:"
    DISPLAY "Sum: ", sum_result
    DISPLAY "Difference: ", difference_result

END PROGRAM

STOP