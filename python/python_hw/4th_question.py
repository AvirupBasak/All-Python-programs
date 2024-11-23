num=int(input("Enter the Value of N : "))
sum=1
add=0
for i in range(0,num):
    sum+=i
    add+=sum
    print(sum,end="+")
print(f"\b = {add}")