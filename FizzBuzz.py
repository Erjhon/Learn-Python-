

# FizzBuzz
num1= int(input("Enter a number: "))
num2= int(input("Enter a number: "))
for i in range(num1,num2):
    if i % 3 == 0  and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# Odd and Even numbers
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))

for i in range(num1,num2):
    if i % 2 == 0:
        print("Even")
    else:
        print("Odd")


# varriable
num1 = input("Enter: ")
rep = "Repeat"
# if num1 % 2 == 0:
#     print("even")
# else:
#     print("odd")
print(frozenset(num1))