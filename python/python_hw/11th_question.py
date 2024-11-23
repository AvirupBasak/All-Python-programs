# display all 3 digit number which divisible by 3 not by 9
for i in range(100,1000):
    if ((i % 3 == 0) and (i % 9 != 0)):
        print(i,end=" ")