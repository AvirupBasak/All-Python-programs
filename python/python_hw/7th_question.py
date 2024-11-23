# sum of digits input 256 output will be 2+5+6=13
num=int(input("Enter a Value"))
sum=0
r=0
while(num>0):
    r = num % 10
    sum += r
    num = num // 10
print(f"The sum of digit is {sum}")