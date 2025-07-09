num1 = float(input("Insert the first number: "))
num2 = float(input("Insert the second number: "))
print("Availible Operators: *, /, -, +")
operator = input("Insert the operator: ")
Average = input("Do you want the average? If Yes say 'Yes' if No say 'No'. ")


sub = num1 - num2
mul = num1 * num2
Div = num1 / num2
Ad = num1 + num2

AverageR = (num1 + num2)/2

if operator == '-' :
  print("The result is:", sub)

if operator == '+' :
  print("The result is:", Ad)

if operator == '/' :
  print("The result is:", Div)


if operator == '*' :
  print("The result is:", mul)

if Average == 'Yes' :
  print("The average is:", AverageR)