# area pere of a traingle
# peri = a+b+c
# s=pere/2
# area = s*(s-a)*(s-b)*(s-c)**0.5

a=int(input("Enter first side of traingle : "))
b=int(input("Enter second side of traingle : "))
c=int(input("Enter third side of traingle : "))

peri=a+b+c
s=peri/2
area=(s*(s-a)*(s-b)*(s-c)**0.5)

print(f"the perimeter of the traingle is {peri} and area is {area}")