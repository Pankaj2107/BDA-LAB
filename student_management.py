class Student:
    def __init__(self, roll, name, m1, m2):
        self.roll = roll
        self.name = name
        self.m1 = m1
        self.m2 = m2

    def accept(self, roll, name, m1, m2):
        ob = Student(roll, name, m1, m2)
        l.append(ob)

    def display(self, ob):
        print("RollNo : ", ob.roll)
        print("Name : ", ob.name)
        print("Marks1 : ", ob.m1)
        print("Marks2 : ", ob.m2)
        print()

    def search(self, roll):
        for i in range(len(l)):
            if l[i].roll == roll:
                return i
        return -1

    def update(self, roll, no):
        for i in range(len(l)):
            if l[i].roll == roll:
                l[i].roll = no

    def delete(self, roll):
        for i in range(len(l)):
            if l[i].roll == roll:
                del l[i]

l = []
ob = Student(0, "", 0, 0)
print("Operations available are :")
print("1. Accept Student details \n2.Display Student details \n3. Search Student details \n4.Update Student details \n.5 Delete Student details")
ob.accept(124, "Puneeth", 98, 100)
ob.accept(113, "Aarya", 98, 99)
ob.accept(120, "Prithviraj", 99, 98)
ch = int(input("Enter your choice : "))
if ch == 1:
    print("Enter Student details")
    roll = int(input())
    name = input()
    m1 = input()
    m2 = input()
    ob.accept(roll, name, m1, m2)
elif ch == 2:
    a = int(input("Enter the roll no of student : "))
    if ob.search(a) != -1:
        ob.display(l[ob.search(a)])
    else:
        print("Data not found")
elif ch == 3:
    a = int(input("Enter the roll no of student : "))
    if ob.search(a) != -1:
        print("Data is Available in the database")
    else:
        print("Data not found")
elif ch == 4:
    a = int(input("Enter the roll no of student : "))
    b = int(input("Enter the rollno to be updated"))
    if ob.search(a) != -1:
        ob.update(a, b)
    else:
        print("Data not found")
else:
    a = int(input("Enter the roll no of student : "))
    if ob.search(a) != -1:
        ob.delete(a)
        print("Deleted successfully")
    else:
        print("Data not found")
    
        

