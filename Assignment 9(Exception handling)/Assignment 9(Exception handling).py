"""
Assignment 9: Division with exception handling (zero division and invalid input).
This assignment has no data files—only this script.
"""
try:
    dividend = int(input("Enter first number: "))
    divisor = int(input("Enter second number: "))
    quotient = dividend / divisor
    print(quotient)

except ZeroDivisionError:
    print("The second number cannot be zero.")

except ValueError:
    print("Please enter valid integer values.")

else:
    print("Division completed for the given numbers.")

finally:
    print("Program execution finished.")
