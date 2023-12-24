#!/usr/bin/env python
# coding: utf-8


# 100 Days Of Code - Log
# 
# Day 8: December 24, 2023
# 
# **Today's Progress**: 
# 
# 1. Learned OOPS concept in python.
# 2. Had a understanding on methods and attributes.
# 3. Tried to worked on logic building by debugging code.


# # **Object Oriented Programming(OOPS) Part 1**

# 1. in OOPS we buildup Classes which are template
# 2. Object are the instance of the Class
# 3. DRY - Don't Repeat Yourself

# In[51]:


class student:
    pass


# In[52]:


harry = student()   # this is a 1st object of student class # or 1st instance of class
larry = student()   # this is a 2nd object of student class # or 2nd instance of class


# In[53]:


# from running this we can observe the output showing 2 different object at different location
print(harry, larry) 


# In[54]:


# initializing instance variable for the object
harry.name = 'Harry'
harry.std = 12
harry.section = 1
#larry.name = 'Larry'
larry.std = 2
larry.subject = ['hindi', 2, 'english']


# In[55]:


print(larry.subject)


# In[70]:


print(list)


# In[1]:


class Employee:
    no_of_leaves = 8    # this is an example of class variable
                        # this variable will be same for every object derive from this class
    pass


# In[2]:


harry = Employee()
rohan = Employee()


# In[3]:


# this is an example of object variable not an class variable
# in other word these are a property of the object not of class
harry.name = 'Harry'
harry.salary = 455
harry.role = 'Tester'

rohan.name = 'Rohan'
rohan.salary = 769
rohan.role = 'Data'


# In[4]:


print(Employee.no_of_leaves)
print(rohan.__dict__)


# In[5]:


rohan.no_of_leaves = 9


# In[7]:


# instance variable can't change the properties of class variable therefore can't overwrite
print(Employee.no_of_leaves)
print(Employee.__dict__)
print(rohan.__dict__)


# In[77]:


# this shows that class variable are not overwritten and shared among all the objects derived
print(Employee.__dict__)


# Example of changing class variable or attribute with an instance variable

# In[10]:


class Sample:
    class_variable = 97
    


# In[2]:


rai = Sample()


# In[6]:


rai.instance_variable = 33
print(rai.instance_variable)
rai.instance_variable = 73
print(rai.instance_variable)


# In[11]:


print(Sample.__dict__)
Sample.class_variable = 77
print(Sample.__dict__)


# In[13]:


print(rai.instance_variable)
rai.class_variable = 11
print(rai.__dict__)
print(Sample.__dict__)


# Usecase of SELF Argument
# 
# NOTE:
# If we won't give the method (i.e. the function developed on class) 'self' argument & run the "print(object.print_details())"
# It will say 1 positional argument is given that means it automatically takes argument itself for the object passed with
# So, that why we pass self as a argument in the method always

# In[21]:


#building method 
class Employee:
    no_of_leaves = 8
    def print_details(self):    # self is that instant on which this function will be call
        return f' Hi I am {self.name}\n My Salary is {self.salary} and I work as an {self.role}'


# In[22]:


# assigning object
harry = Employee()  
rohan = Employee()


# In[23]:


harry.name = 'Harry'
harry.salary = 455
harry.role = 'Tester'

rohan.name = 'Rohan'
rohan.salary = 769
rohan.role = 'Data'


# In[24]:


# method calling
rohan.print_details()


# In[26]:


harry.print_details()


# Usecase of CONSTRUCTOR
# 
# NOTE:
# We use this to pass the items in the class name as a argument instead of making insatance variable

# In[1]:


class Employee:
    no_of_leaves = 8
    
    def __init__(self, arg_name, arg_salary, arg_role):
        self.name = arg_name
        self.salary = arg_salary
        self.role = arg_role
        
        
    def print_details(self):
        return f' Hi I am {self.name}\n My Salary is {self.salary} and I work as an {self.role}'


# In[2]:


# the argument pass through class is always goes to __init__ function only otherwise error will happen like in SELF Usecase
harry = Employee('Harry', 20, 'Analyst') 
larry = Employee('Larry', 39, 'Devops')


# In[3]:


print(harry.salary)


# In[6]:


print(larry.salary)


# DECORATORS

# In[1]:


def function1():
    print('subscribe')


# In[5]:


func2 = function1
del function1
func2()


# In[14]:


def funcret(n):
    if n == 0:
        return print
    if n == 1:
        return int
    if n == 2:
        return sum


# In[16]:


a = funcret(0)
print(a)
b = funcret(1)
print(b)
c = funcret(2)
print(c)


# In[19]:


# This is a concept to show that we can return function from the function itself
def executer(func):
    func("This Line")


# In[20]:


executer(print)


# In[1]:


def topdec(func1):
    def exedec():
        print("Executing...")
        func1()
        print("Executed!")
    return exedec


# In[23]:


@topdec
def who_is_this():
    print("This is Vineet")
# who_is_this = topdec(who_is_this)
who_is_this()


# In[28]:


class Employee:
    
    no_of_leaves = 8
    
    def __init__(self, arg_name, arg_salary, arg_role):
        self.name = arg_name
        self.salary = arg_salary
        self.role = arg_role
    
    def details():
        return f'Hi ! My name is {self.name}. I earn {self.salary} lakh for the role of {self.role}'
        
    @classmethod              # classmethod help to access and manipulate only the class variable/attribute
    def changeleaves(cls, new_leaves):
        cls.no_of_leaves = new_leaves
        


# In[29]:


harry = Employee('Harry', 20, 'Devops')
larry = Employee('Larry', 30, 'Analyst')


# In[30]:


harry.changeleaves(74)
print(Employee.no_of_leaves)


# In[31]:


print(harry.no_of_leaves)


# In[32]:


Employee.no_of_leaves


# In[19]:


# creating class method as alternative constructors
class Employee:
    
    no_of_leaves = 8
    
    def __init__(self, arg_name, arg_salary, arg_role):
        self.name = arg_name
        self.salary = arg_salary
        self.role = arg_role
    
    def details():
        return f'Hi ! My name is {self.name}. I earn {self.salary} lakh for the role of {self.role}'
        
    @classmethod              # classmethod help to access and manipulate only the class variable/attribute
    def desig(cls, string):
#        splt_lst = string.split("-")
#        return cls(splt_lst[0],splt_lst[1],splt_lst[2])
        return cls(*string.split("-"))


# In[20]:


karan = Employee.desig("Karan-480-Dev")


# In[21]:


karan.name


# In[22]:


karan.no_of_leaves


# In[23]:


karan.role


# In[24]:


karan.salary


# In[13]:


class Employee:
    
    no_of_leaves = 8
    
    def __init__(self, arg_name, arg_salary, arg_role):
        self.name = arg_name
        self.salary = arg_salary
        self.role = arg_role
    
    def details():
        return f'Hi ! My name is {self.name}. I earn {self.salary} lakh for the role of {self.role}'
        
    @classmethod              # classmethod help to access and manipulate only the class variable/attribute
    def desig(cls, string):
#        splt_lst = string.split("-")
#        return cls(splt_lst[0],splt_lst[1],splt_lst[2])
        return cls(*string.split("-"))

    @staticmethod             # static method is use to make function only for only getting utilize by it's class
    def printgood(string):
        print("This is good " +string)
        return 


# In[8]:


karan = Employee.printgood("Vineet")


# In[14]:


print(Employee.printgood("Harry"))


# In[16]:


Employee.printgood("Ronny")


# UDEMY SECTION

# In[1]:


class Sample():
    pass


# In[2]:


my_sample = Sample()


# In[4]:


type(my_sample)


# In[7]:


class Dog():
    
    # User defined Attributes
    # __init__ is a constructor of the class
    # self here is nothing but refering to the instance of the class itself
    def __init__(self,arg_mybreed, arg_name, arg_spot):    # this init function/method let you to connect with the instance of the class.
        
        # Attribute
        # we take in argument
        # assign it using self.attribute_name
        self.breed = arg_mybreed
        self.name = arg_name
        
        # Expect boolean True/False
        self.spot = arg_spot


# In[2]:


pet = Dog('huski','tom',True)


# In[5]:


pet.breed


# In[31]:


my_dog = Dog(arg_mybreed= 'lab', arg_name='sammy', arg_spot= False)


# In[32]:


type(my_dog)


# In[33]:


my_dog.breed


# In[34]:


my_dog.name


# In[35]:


my_dog.spot


# In[8]:


# If attribute will be same for any instance of the class

class Dog():
    
    # Attribute at class object level
    # same for any instance of the class
    species = 'mammal'
    
    
    # User defined Attributes
    # __init__ is a constructor of the class
    # self here is nothing but refering to the instance of the class itself
    def __init__(self,arg_mybreed, arg_name, arg_spot):    # this init function/method let you to connect with the instance of the class.
        
        # Attribute
        # we take in argument
        # assign it using self.attribute_name
        self.breed = arg_mybreed
        self.name = arg_name
        
        # Expect boolean True/False
        self.spot = arg_spot


# In[2]:


my_dog = Dog(arg_mybreed = 'lab', arg_name = 'sam', arg_spot= False)


# In[3]:


type(my_dog)


# In[4]:


my_dog.species


# In[3]:


class Dog():
    
    # Attribute at class object level
    # same for any instance of the class
    species = 'mammal'
    
    
    # User defined Attributes
    # __init__ is a constructor of the class
    # self here is nothing but refering to the instance of the class itself
    def __init__(self,arg_mybreed, arg_name):    # this init function/method let you to connect with the instance of the class.
        
        # Attribute
        # we take in argument
        # assign it using self.attribute_name
        self.breed = arg_mybreed
        self.name = arg_name
       
    # Operation/Action --> Methods
    # self is to connect with object of the class
    def bark(self):
        print("Woof!")
    
    


# In[4]:


my_dog = Dog('lab', 'franke')


# In[12]:


# Attributes are never called with parenthesis (),
# because they are buildup to show class properties/information.
my_dog.species


# In[13]:


my_dog.name


# In[14]:


# here demonstrating the method called without parenthesis ().
# methods are madeup to perform some action. So, alway called with parenthsis other it will sow following output 
my_dog.bark


# In[15]:


my_dog.bark()


# Repeating the same example of code to revise concept bound in comments

# In[25]:


class Dog():
    
    # Attribute at class object level
    # same for any instance of the class
    species = 'mammal'
    
    
    # User defined Attributes
    # __init__ is a constructor of the class
    # self here is nothing but refering to the instance of the class itself
    def __init__(self,arg_mybreed, arg_name):    # this init function/method let you to connect with the instance of the class.
        
        # Attribute
        # we take in argument
        # assign it using self.attribute_name
        self.breed = arg_mybreed
        self.name = arg_name
       
    # Operation/Action --> Methods
    # self is to connect with object of the class
    def bark(self,num):       # proving num arg to be provided by user
        print("Woof! My name is {} & my number is {}" .format(self.name, num))
    
    


# In[26]:


my_dog = Dog('Huskie','groot')


# In[27]:


my_dog.bark(7)


# Overview of class & object with attribute(class, object), function  

# In[18]:


class Circle():
    
    # Class object attribute
    pi = 3.141
    
    def __init__(self, radius = 1):
        self.radius = radius
#        self.area = self.pi * radius * radius

        # for class attribute we can place other thing as well instead of self
        # it will make no difference as class attribute cann't be change like doing below by placing 'Circle'
        # which is also more readable for coders
        self.area = Circle.pi * radius*radius     
    
    # this method is to get circumference
    def get_circumference(self):
        return 2 * Circle.pi * self.radius 
    


# In[19]:


my_circle = Circle(89)


# In[20]:


my_circle.pi


# In[21]:


my_circle.radius


# In[22]:


my_circle.get_circumference()


# In[23]:


my_circle.area


# In[ ]:




