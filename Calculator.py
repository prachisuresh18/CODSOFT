# CALCULATOR CODSOFT TASK
number1 = int(input("Enter 1st number:\n"))
number2 = int(input("Enter 2nd number:\n"))
operator = input("Select: +, -, *,/  : \n")
result = None
if operator == "+":
    result = number1 + number2


elif operator == "-":
    result = number1 - number2

elif operator == "*":
    result = number1 * number2

elif operator == "/":
    if number2 == 0:
        print("Division by zero is not possible")
    else:
        result = number1 / number2

else:
    print("Wrong input ")


if result is not None:
    print("Result: \n", result)
