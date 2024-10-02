print("Calculator Program\n")
print("====================")

number1 = float(input("Enter a number: "))
number2 = float(input("Enter a number: "))
operator = input("Enter.. add, subtract, divide, multiply ")

if operator.lower() == "add":
    result = (number1 + number2)
    print(result)
elif operator.lower() == "subtract":
    result = (number1 - number2)
    print(result)
elif operator.lower() == "divide":
    result = (number1 / number2)
    print(result)
elif operator.lower() == "multiply":
    result = (number1 * number2)
    print(result)
else:
    print("An error has occurred.")
    