# count the digit of a number
num=int(input("Enter a Value : "))
count=0
while(num>0):
    count = count + 1
    num = num // 10
print(f"Entered number has {count} digits")
