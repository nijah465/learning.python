num1 = float(input(" Enter your number: "))
op = input(" Enter operator: ")
num2 = float(input(" enter a second number: "))


def numbers():
    if op == "+":
     print(num1 + num2)
    elif op == "*":
     print(num1*num2)
    elif op == "-":
      print(num1-num2)
    elif op== "/":
      print(num1/num2)
    else:
      print("syntax error")
numbers()



