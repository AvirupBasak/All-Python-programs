num1=int(input("Enter first number "))
num2=int(input("Enter second number "))
num3=int(input("Enter third number "))

# greater number logic

if(num1>num2 and num1>num3):
    print(f"{num1} is greater")
elif(num2>num3):
    print(f"{num2} is greater")
else:
    print(f"{num3} is greater")

# smaller number logic

if(num1<num2 and num1<num3):
    print(f"{num1} is smaller")
elif(num2<num3):
    print(f"{num2} is smaller")
else:
    print(f"{num3} is smaller")