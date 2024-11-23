# write a program to find the sum of the following series
# 2+5+8+11+14+.....upto N
num=int(input("Enter the Value of N : "))
i=2
sum=0
while(i<=num):
    print(i,end="+")
    sum+=i
    i+=3
print(f"\b = {sum}")

# same in for loop

for i in range(2, num+1 , 3):
    print(i,end="+")
print(f"\b = {sum}")