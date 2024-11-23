# write a program to find the sum of the following series:-
# 1+11+111+1111......upto n
num=int(input("Enter the Value of N : "))
n=0
sum=0
for i in range(1,num+1):
    n=n*10+1
    sum+=n
    print(n, end="+")
print(f"\b = {sum}")