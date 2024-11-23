# swap two number without using 3rd variable
num1=int(input("Enter first number : " ))
num2=int(input("Enter first number : " ))

print("You entered first number second number is ",num1,num2)

num1=num1+num2
num2=num1-num2
num1=num1-num2

print("after swapping the value of first number and second number is ",num1,num2)