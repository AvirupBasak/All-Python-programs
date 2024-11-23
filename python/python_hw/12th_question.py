# display 1 10 101 1010 10101 ....up to n
num=int(input("Enter Value : "))
n=1
for i in range(1,num+1):
    print(n)
    n = n*10
    if(i % 2 == 0):
        n+=1