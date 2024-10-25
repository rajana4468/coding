1                    # Creating a Class and Objects and initializing a Arguments

"""class Mobile:
    def __init__(self,Brand,Battery,Price,Ram,Owner):
        self.Brand = Brand
        self.Battery = Battery
        self.Price = Price
        self.Ram = Ram
        self.Owner = Owner
    def display(self):
        print("Brand:",self.Brand)
        print("Battery:",self.Battery)
        print("Price:",self.Price)
        print("Ram:",self.Ram)
        print("Owner:",self.Owner)
        print("------------")
obj1 = Mobile("Apple","4000Mah","16000","8gb","ME")
obj1.display()
obj2 = Mobile("Realme","5000Mah","17000","9gb","ME")
obj2.display()
obj3 = Mobile("Oppo","4000Mah","19000","8gb","SHE")
obj3.display()"""

# What is self ?

# In Pythons Object-Oriented Programming (OOP), self is a reference variable which is always pointing to the current instance of the class. 
# It is used within class methods to access attributes and other methods of the object being created. The self-parameter must be the first parameter of any method in the class, but it is not included when the method is called on an instance of the class.


# By using self, we can Differentiating Between Class and Instance Variables: self helps in differentiating between class-level attributes and instance-level attributes.

"""class Dog:
    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name  # Instance variable self.name
        self.age = age    # Instance variable self.age

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

# Creating an object (instance) of the Dog class
my_dog = Dog("Buddy", 3)

# Accessing attributes and calling methods
print(my_dog.description())  # Output: Buddy is 3 years old
print(my_dog.speak("Woof"))  # Output: Buddy says Woof"""


"""class My:
    def __init__(self,a,b):   # if we initialize variables in init method we can access them in other Class also
        self.a = a
        self.b = b
class fun(My):           # --> class "fun" is inherit by "My" class
    def display(self):
        print(self.a,self.b)  # Accessing Variables 

obj = fun(25,63)
obj.display()"""


"""class My_self:
    def __init__(self,Name,Studies,Age,Goal):
        #print("Hii")
        self.Name = Name
        self.Studies = Studies
        self.Age = Age
        self.Goal = Goal
    def display(self):
        print(f"Good Moring, my_name is {self.Name} and iam Studying {self.Studies} iam {self.Age} years Old, my Gaol is to {self.Goal}.")


obj = My_self("Sai Krishna","B-tech Final year in the stream of ECE","21"," Place in a Reputed Company")
obj.display()"""


          # init method will be Execute Without calling a Object

"""class Sai:
    def __init__(self):
        print("This is init")
obj = Sai()"""

"""class Movie:
    def __init__(self,tit,her,hrne):
        self.title=tit
        self.hero=her
        self.heroine=hrne
    def info(self):
        print("Movie Name is: ",self.title)
        print("Movie hero is: ",self.hero)
        print("Movie heroine is: ",self.heroine)

listt = []

while True:
    title=input("Enter movie Name: ")
    hero=input("Enter Movie HEro: ")
    heroine=input("Enter MOvie Heroine: ")
    op = Movie(title,hero,heroine)
    listt.append(op)
    print("Movie added to the listt successfully")
    option=input("If you want to add another movie Yes/No: ")
    if option.lower()=="no":
        break
print("All movies information")
print("*"*15)
for movie in listt:
    movie.info()
    print()"""


"""import sys

class Customer:
    bank_name = "Your _ Bank"
    def __init__(self,name,balance=0):
        self.name = name
        self.balance = balance

    def deposit(self,amt):
        self.balance = self.balance+amt
        print("Your amount is deposited")
        print("Total Balance is :", self.balance)
        print("*"*50)

    def withdraw(self,amt):
        if amt > self.balance:
            print("Insufficient funds")
            print("*"*50)
            return
        self.balance-=amt
        print("balance after withdraw: ",self.balance )
        print("*"*50)

print(f"Welcome to {Customer.bank_name}.")
name = input("Enter Your Name: ")
obj = Customer(name)
flag = True
while True:
    if flag:
        print(f"hii {name} welcome to {Customer.bank_name}")
        flag = False
    print("These are all our service, please choose One")
    print("For deposit Enter: D" )
    print("For Withdraw Enter: W")
    print("For Balance Enquiry Enter: B")
    op = input("Your Option is: ")
    if op.lower()=="d":
        amt = int(input("Enter Your Amount: "))
        obj.deposit(amt)
    elif op.lower()=="w":
        amt = int(input("Enter Your amount: "))
        obj.withdraw(amt)
    elif op.lower() == "b":
        print("Your Balance is ",obj.balance)
        print("*"*50)
    op = input("Continue our service! Yes/No: ")
    if op.lower()=="no":
        print("Thank You visit Again")
        break"""


                            # Method Overriding.

"""class Vehicle:

    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price

    def show(self):
        print('Details:', self.name, self.color, self.price)

    def max_speed(self):
        print('Vehicle max speed is 150')

    def change_gear(self):
        print('Vehicle change 6 gear')


# inherit from vehicle class
class Car(Vehicle):
    def max_speed(self):
        print('Car max speed is 240')

    def change_gear(self):
        print('Car change 7 gear')


# Car Object
car = Car('Car x1', 'Red', 20000)
car.show()
# calls methods from Car class
car.max_speed()
car.change_gear()

# Vehicle Object
vehicle = Vehicle('Truck x1', 'white', 75000)
vehicle.show()
# calls method from a Vehicle class
vehicle.max_speed()
vehicle.change_gear()"""
    
# output
"""Details: Car x1 Red 20000
Car max speed is 240
Car change 7 gear

Details: Truck x1 white 75000
Vehicle max speed is 150
Vehicle change 6 gear"""


"""As you can see, due to polymorphism, the Python interpreter recognizes that the
max_speed() and change_gear() methods are overridden for the car object.
So, it uses the one defined in the child class (Car)

On the other hand, the show() method isn’t overridden in the Car class,
so it is used from the Vehicle class."""


                              # Method OverLoading
def addition(a, b):
    c = a + b
    print(c)


def addition(a, b, c):
    d = a + b + c
    print(d)


# the below line shows an error
# addition(4, 5)

# This line will call the second product method
#addition(3, 7, 5)


                          # Access Modifier
# Public Access Modifier
# Public: Members are accessible from outside the class.

"""class Parent:
    public_data = 10
    def public_met(self):
        print(self.public_data)

class Child(Parent):
    def meth(self):
        print(self.public_data)

obj1 = Parent()
obj1.public_met()
print(obj1.public_data)

obj2 = Child()
obj2.meth()
print(obj2.public_data)"""


# Protected Access Modifier

# Protected: Members are accessible within the class and its subclasses

class Parent:
    _protected_data = 10
    def public_met(self):
        print(self._protected_data)

class Child(Parent):
    def meth(self):
        print(self._protected_data)

obj1 = Parent()
obj1.public_met()
print(obj1._protected_data)

obj2 = Child()
obj2.meth()
print(obj2._protected_data)


                           # INHERITANCE

# Single Inheritance

"""class Parent:
    def fun1(self):
        print("This is Parent")
class Child(Parent):      # Parent to Child
    def fun2(self):
        print("This is Child")
obj1 = Child()      # obj is Created is only Child Class
#obj1.fun2()
obj1.fun1()      # Accessing Parent Class methods from Child Object"""


# Multilevel Inheritance

"""class Grand_parent:
    def fun1(self):
        print("This is Grand_parent Class")
class Parent(Grand_parent):
    def fun2(self):
        print("This is Parent Class")
class Child(Parent):
    def fun3(self):
        print("This is Child Class")
obj = Child()       # Creating obj only for Child Class
obj.fun1()          # Accessing Grand_parent Class methods from Child Object
obj.fun2()          # Accessing Parent Class methods from Child Object"""


# Hierarchial Inheritance


"""class Parent:
    def fun1(self):
        print("This is Parent Class")
class Child1(Parent):
    def fun2(self):
        print("This is Child1 Class")
class Child2(Parent):
    def fun3(self):
        print("This is Child2 Class")
obj1 = Child1()     # Creating obj only for Child1 Class
obj2 = Child2()     # Creating obj only for Child2 Class

#obj1.fun2()
#obj1.fun1()
obj2.fun3()         # Accessing Child1 Class methods from Child2 Object
obj2.fun1()         # Accessing Parent Class methods from Child2 Object"""

# Multiple Inheritance

"""class Parent1:
    def fun1(self):
        print("This is Parent1 Class")
class Parent2:
    def fun2(self):
        print("This is Parent2 Class")
class Child(Parent1,Parent2):
    def fun3(self):
        print("This is Child Class")
obj = Child()       # Creating obj only for Child Class
obj.fun1()          # Accessing Parent1 Class methods from Child Object
obj.fun2()          # Accessing Parent2 Class methods from Child Object
obj.fun3()          # Accessing Parent3 Class methods from Child Object"""


                         #  ENCAPSULATION
                                   
"""class Capsule:
    def __init__(self,a,b):
        self.__a = a  # (double Under Score indicates -- > Private Variable)
        self._b = b   # (Single Under Score indicates -- > Protected Variable)

class Encap(Capsule):
    def display(self):
        print(self.__a)
        print(self._b)

obj = Encap(25,63)
obj.display()"""

#if you run the above code it gives error 'Encap' object has no attribute '_Encap__a', because it is Private Variable 

"""class Capsule:
    def __init__(self,a,b):
        self.__a = a  # Private
        self._b = b   # Protected

class Encap(Capsule):
    def display(self):
        #print(self.__a)
        print(self._b)

obj = Encap(25,63)
obj.display()"""

#if you run the above code it gives only "b" Value because its a Protected Variable it can be Access in Another Classes.
 



                                    # Super Keyword      theory in Notce
# it is used to call the methods and constructors from parent class to child class
# it always goes to the immediate parent class
# mainly used in inheritace below is the example. of thatttt

"""class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print("Name is: ",self.name)
        print("Age is: ",self.age)


class Student(Person):
    def __init__(self,name,age,roll,marks):
        super().__init__(name,age)
        self.roll = roll
        self.marks = marks

    def display(self):
        # print("Name is: ",self.name)   # instead of calling name and age, i call the display function from parent class
        # print("age is: ",self.age)
        super().display()
        print("Roll is: ",self.roll)
        print("marks is: ",self.marks)

class Teacher(Person):
    def __init__(self,name,age,salary,subject):
        super().__init__(name,age)
        self.salary = salary
        self.subject = subject

    def display(self):
        # print("Name is: ",self.name)     # instead of calling name and age, i call the display function from parent class
        # print("age is: ",self.age)
        super().display()
        print("Salary is: ",self.salary)
        print("Subject is: ",self.subject)

s = Student("SAi Krishna",23,19,35)
t = Teacher("Pavan",35,70000,"Coding")
s.display()
print()
t.display()"""



"""class Parent:
    def fun1(self):
        print("Hii this is Parent")

class Child(Parent):
    def fun2(self):
        print("Hii this is Child")
        super().fun1()

obj = Child()
obj.fun2()"""




                        # Creating a Singly Linked List

"""class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None

class Linked_List:
    def __init__(self):
        self.head = None
    def append(self,data):
        new_Node = Node(data)
        if not self.head:
            self.head = new_Node
            return
        current = self.head
        while current.ref:
            current = current.ref
        current.ref = new_Node

def print_list(items):
    obj = Linked_List()
    for i in items:
        obj.append(i)
    return obj

items = [1,2,3,4,5]
listt = print_list(items)

curr = listt.head

while curr.ref:
    print(curr.data)
    curr = curr.ref"""





                        # creating a tree represent in inorder

"""class Node:               
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(5)
root.left.left = Node(4)
root.right.left = Node(6)
root.right.right = Node(7)

def inorder(root):
    if root == None:
        return
    inorder(root.left)
    print(root.val,end = " ")
    inorder(root.right)
inorder(root)

print()


def postorder(root):
    if root == None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.val,end=" ")
postorder(root)"""

                # creating a Binary_Search_Tree represent in a inorder Traversal 



"""class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def sorted_list_to_bst(sorted_list):
    if not sorted_list:
        return None

    # Find the middle index
    mid_index = len(sorted_list) // 2

    # Create a TreeNode with the middle element as the root
    root = TreeNode(sorted_list[mid_index])

    # Recursively build left and right subtrees
    root.left = sorted_list_to_bst(sorted_list[:mid_index])
    root.right = sorted_list_to_bst(sorted_list[mid_index + 1:])

    return root

def print_inorder(root):
    if root:
        print_inorder(root.left)
        print(root.value, end=" ")
        print_inorder(root.right)

# Example usage:
input_list = [1, 2, 1, 2, 5, 4, 1, 21, 25]
sorted_list = sorted(input_list)  # Sort the input list

# Convert the sorted list to a binary search tree
bst_root = sorted_list_to_bst(sorted_list)

# Print the elements of the BST in inorder traversal (sorted order)
print_inorder(bst_root)"""




"""class BST:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
    def insert(self,data):
        if self.key is None:
            self.key = data
            return
        if self.key > data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = BST(data)
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right = BST(data)
root = BST(5)
lt = [1,2,3,4,5,6,7,8,9]
for i in lt:
    root.insert(i)
from collections import deque
def level_order(root):
    q = deque()
    q.append(root)
    res = []
    while q:
        dum = []
        l = len(q)
        for i in range(l):
            k = q.popleft()
            dum.append(k.key)
            if k.left:
                q.append(k.left)
            if k.right:
                q.append(k.right)
        res.append(dum)
    return res
print(level_order(root))"""




