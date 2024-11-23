#count odd digit of a inpted number
num=int(input("Enter Value : "))
count=0
n=0
while(num>0):
    n=num%10
    if n%2 != 0:
        count+=1
    num=num//10
print(f"There were {count} odd digits in the number")