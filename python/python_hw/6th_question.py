# find the sum 1^1+3^2+5^3+7^4+....up to n
num=int(input('''Enter the value of N (odd number) : '''))
if(num%2 != 0):
    pow=1
    sum=0
    for i in range(1, num+1,2):
        sum += i**pow
        print(f"{i}^{pow}+",end="")
        pow = pow+1
    print(f"\b = {sum}")
else:
    print("Enter a valid number. Enter a odd number....")