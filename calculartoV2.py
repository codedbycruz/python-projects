print("Welcome to the ultra mega max calculator 3000")
print("Here you will be able to use the calculator")
num1 = float(input("Insert the first number: "))
num2 = float(input("Insert the second number: "))

print("Available Operators: *, /, -, +")
operator = input("Insert the operator: ")

average_choice = input("Do you want the average? If Yes say 'Yes' if No say 'No': ")
power_choice = input("Would you like to get the squared of the result? If Yes say 'Yes': ")
Cubic_choice = input("Would you like to get the cubic of the result? If Yes say 'Yes': ")

# Perform operations
sub = num1 - num2
mul = num1 * num2
div = num1 / num2 if num2 != 0 else "Cannot divide by zero"
add = num1 + num2
average_result = (num1 + num2) / 2

# Determine result based on operator
if operator == '-':
    result = sub
elif operator == '+':
    result = add
elif operator == '/':
    result = div
elif operator == '*':
    result = mul
else:
    result = "Invalid operator"

# Show main result
print("The result is:", result)

# Optional: show average
if average_choice.lower() == 'yes':
    print("The average is:", average_result)

# Optional: show result squared
if power_choice.lower() == 'yes':
    if isinstance(result, (int, float)):  # Avoid squaring error message string
        print("The square of the result is:", result ** 2)
    else:
        print("Cannot compute the power because the result is not a number.")

if Cubic_choice.lower() == 'yes':
    if isinstance(result, (int, float)):  # Avoid squaring error message string
        print("The cube of the result is:", result ** 3)
    else:
        print("Cannot compute the power because the result is not a number.")