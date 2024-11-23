class Student:
    def __init__(self):
        self.stu_name = []
        self.roll = []

s1 = Student()

no = int(input("how many Data of Student you should Enter->\n"))

for data in range(no):
    name = input("Enter the name-> ").strip()
    nmb = int(input("Enter the roll-> "))
    s1.stu_name.append(name)
    s1.roll.append(nmb)

print("\nPrintig the Student's data's...")
print("Student Name".ljust(15),"Student Roll")

for data in range(no):
    print(s1.stu_name[data].ljust(20),s1.roll[data])


# --------------------------------------------------------------------
# Another process to initialize student data...
# --------------------------------------------------------------------

# class Student:
#     def __init__(self):
#         self.stu_name = []
#         self.roll = []

#     def add_student(self, name, roll):
#         self.stu_name.append(name)
#         self.roll.append(roll)

#     def display_students(self):
#         print("Student Name".ljust(15), "Student Roll")
#         for name, roll in zip(self.stu_name, self.roll):
#             print(name.ljust(15), roll)

# s1 = Student()
# no = int(input("How many student records you want to enter? -> "))
# for i in range(no):
#     name = input("Enter the name -> ").strip()
#     roll = int(input("Enter the roll -> "))
#     s1.add_student(name, roll)

# print("\nPrinting the Student's data...")
# s1.display_students()
