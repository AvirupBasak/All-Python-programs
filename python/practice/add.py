# def sum(a,b):
#     return a+b

# sum_num = sum(1,2)
# print(sum_num)


# def sort_list(lst,isascending=True):
#     return sorted(lst, reverse=not isascending)

# numbers = [5, 2, 9, 1, 5, 6]
# sorted_asc = sort_list(numbers)
# sorted_desc = sort_list(numbers, isascending=False)
# print("Ascending Order:", sorted_asc)
# print("Descending Order:",sorted_desc)


def add(n):
    if(n==0):
        return 0
    print(n,end=" ")
    return add(n-1)+n

sum=add(5)
print("=",sum)


def prnt(list,idx=0):
    if(idx==len(list)):
        return
    print(list[idx])
    prnt(list,idx+1)

list = ["Avirup",29,"Krishnendu",54,"Abhirup",1]
prnt(list)