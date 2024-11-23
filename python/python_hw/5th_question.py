# display Fibonacci series 0 1 1 2 3 5 8 13 21...up to n
num=int(input("Enter the range of fibonacci : "))
fibo=0
n=0
r=1
print(n,end=" ")
for i in range(0,num):
    fibo = n + r
    r=n
    n=fibo
    print(fibo,end=" ")
