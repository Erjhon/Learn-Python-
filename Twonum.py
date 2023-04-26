num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

op = input("Choose an operator you want: ")

result = 0
if op == '+':
    result = num1 + num2
elif op == '-':
    result = num1 - num2
elif op == '*':
    result = num1 * num2
elif op == '/':
    result = num1 * num2
else:
    print("operator not recognized")
print(num1,op,num2, "=",result)

