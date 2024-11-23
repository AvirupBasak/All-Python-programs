# display all 3 digits peterson number
for i in range(100,1000):
    s = 0
    n = i
    while n>0 :
        r = n % 10
        f=1
        for j in range(1, r+1):
            f = f * j
        s += f
        n = n//10
    if s == i:
        print(s,end=" ")
