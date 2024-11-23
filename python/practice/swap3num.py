# swap two number using 3rd variable
num1=int(input("Enter first number : " ))
num2=int(input("Enter second number : " ))
num3=int(input("Enter third number : " ))

print("You entered first number second number is ",num1,num2,num3)

num1,num2,num3= num2, num3, num1

print("after swapping the value of first number and second number is ",num1,num2,num3)