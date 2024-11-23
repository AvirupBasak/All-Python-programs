# reverse the number input 536 output 635
num=int(input("Enter a Value : "))
pre=num
rev=0
while(num>0):
    n = num % 10
    rev = rev*10 + n
    num = num // 10
print(f"The previous number is {pre}")
print(f"The reverse number is {rev}")