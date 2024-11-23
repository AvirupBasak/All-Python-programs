name = input("Enter your name :- ")
print("Length of your name is -",len(name))
Name = input("Enter your sername :- ")
print("Length of your name is -",len(Name))
new_name = name + " " +Name
print(new_name)

# index-ing
ch = new_name[1] # here '1' denotes the index number of new_name variable
print(ch)

# slising
print(new_name[0:6])