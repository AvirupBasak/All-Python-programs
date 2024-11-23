# print all 3 digit armstrong number
for i in range(100,1000):
    dig1 = i // 100
    dig2 = (i // 10 ) % 10
    dig3 = i % 10

    sum = dig1**3 + dig2**3 + dig3**3
    if sum==i:
        print(i,end=" ")