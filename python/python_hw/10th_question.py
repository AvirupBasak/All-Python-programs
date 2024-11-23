# perfect number
num=int(input("Enter a Value : "))
div=0
for i in range(1,num):
    if num % i == 0:
        div += i
if div == num:
    print(f"The number {num} is a perfect number")
else:
    print(f"The number {num} is not a perfect number")
