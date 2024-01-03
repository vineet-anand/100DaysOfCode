#!/usr/bin/env python
# coding: utf-8

# 100 Days Of Code - Log
# 
# Day 11: January 3, 2024
# 
# **Today's Progress:**
#
#
# 1. Access Specifier
# 2. Polymorphism
# 3. Overriding & issues happening on it
# 4. Diamond Shape Problem
# 5. Operator Overloading
# 6. Special Methods
# 8. Quick Revision on Inheritance

# In[ ]:





# In[ ]:





# In[ ]:





# # **Object Oriented Programming (OOPS) Part 2**


# **Access Specifier**
# 1. Public
# 2. Protected
# 3. Private

# In[11]:


class Employee:
    
    # this is a public variable
    no_of_leaves = 9
    
    # this is protected variable name start with 1 underscore '_'
    _protect = 10  # this is protected variable & accessable to this class as well as class derive from this only(inherited).
    
    # this is a private variable name start with 2 underscore '__'
    __private = 97 # restricted to be access by this class only
    
    var = 20
    
    def __init__(self,name,salary,role):
        self.name = name
        self.salary = salary
        self.role = role
        
    def printdetails(self):
        return f'my name is {self.name}, I earn {self.salary} for the job role of {self.role}'
    
    @classmethod
    def changeleaves(cls,newleaves):
        cls.no_of_leaves = newleaves
        
    @classmethod
    def from_dash(cls,string):
        return cls(*string.split("-"))
    
    
    @staticmethod
    def printgood(string):
        print('this is good ' + string)

        


# In[12]:


harry = Employee('Harry', 45,'Dev')


# In[13]:


harry._protect


# In[17]:


# private variable cann't access like this because of name mangling
# harry.__private
# instead it's private. So convention change to access it

harry._Employee__private


# 1. Inheritance

# In[1]:


# base class
class Animal():
    
    def __init__(self):
        print("Animal Created")
        
    def who_am_i(self):
        print("I'm an animal")
        
    def eat(self):
        print("I'm eating")


# In[2]:


# derive class
class Dog(Animal):
    
    def __init__(self):
        Animal.__init__(self)
        print("Dog Class Created")
    
    # we are overriding the base class method
    def who_am_i(self):
        print("I'm a dog")
    
    def eat(self):
        print("I'm a dog & eating Dish")
        
    def bark(self):
        print("Woof!")


# In[4]:


mydog = Dog()


# In[3]:


myanimal = Animal()


# In[5]:


myanimal.eat()


# In[6]:


myanimal.who_am_i()


# In[7]:


mydog.eat()


# In[8]:


mydog.who_am_i()


# In[11]:


mydog.bark()


# **Polymorphism**

# In[1]:


# Note: It's a concept to take various form
# Overriding 
# Usecase of Super() 


# In[24]:


class A:
    
    classvar1 = "I'm a class variable in Class A"
    
    def __init__(self):
        self.var1 = "I'm inside class A constructor"
        self.classvar1 = "I'm a instance variable in Class A"
        self.special = "Special test"
    
class B(A):
    
    classvar1 = "I'm a class variable in Class B"
    
    def __init__(self):
        self.var1 = "I'm inside class B constructor"
        self.classvar1 = "I'm a instance variable in Class B"
    


# In[25]:


a = A()
b = B()


# In[26]:


b.classvar1


# In[27]:


b.var1


# In[32]:


# Note: Once a method get override then it's parent method doesn't have any value left in it 
# And only the overriding method will produce it's property/attribute


# In[31]:


# here calling special attribute show errer because method of derive class has been override and no value left for base class
b.special


# In[6]:


# to get the attribute of method that has been override but have in base class only we use super()
class A:
    
    classvar1 = "I'm a class variable in Class A"
    
    def __init__(self):
        self.var1 = "I'm inside class A constructor"
        self.classvar1 = "I'm a instance variable in Class A"
        self.special = "Special test"
    
class B(A):
    
    classvar1 = "I'm a class variable in Class B"
    
    def __init__(self):
        
        # super() will go 1st to base class constructor
        # then take all attribute values
        # again back to derive class and replace values for those attribute that has been override rest it will consider
        # if it is getting call first
        # if it's call at end then base class value will be assigned 
        
        super().__init__()
        self.var1 = "I'm inside class B constructor"
        self.classvar1 = "I'm a instance variable in Class B"
    


# In[7]:


a = A()
b = B()


# In[8]:


b.classvar1


# In[9]:


b.var1


# In[10]:


b.special


# In[7]:


# here demonstrating the polymorphism where same method do different action, unique to the different classes
#


# In[1]:


class Dog:
    
    def __init__(self,name):
        self.name = name
    
    def speak(self):
        return self.name + " Woof!"


# In[2]:


class Cat:
    
    def __init__(self,name):
        self.name = name
    
    def speak(self):
        return self.name + " Meow!"


# In[3]:


niko = Dog("Niko")
felix = Cat("Felix")


# In[5]:


niko.speak()


# In[6]:


felix.speak()


# In[13]:


# both object share the same method but belongs from different class

for pet in [niko,felix]:
    print(type(pet))
    print(type(pet.speak))
    print(pet.speak())


# In[16]:


# demonstrating polymorphism from function
def pet_speak(pet):
    return pet.speak()


# In[17]:


pet_speak(niko)


# In[19]:


pet_speak(felix)


# In[1]:


from abc import ABC, abstractmethod


# In[2]:


# abstract method is a concept to enforce method that is derive from the base class


# In[4]:


# here we are enforcing class to add printarea method
class Shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0


# In[5]:


class Rectangle(Shape):
    type = 'Rectangle'
    side = 4
    
    def __init__(self):
        self.length = 6
        self.breadth = 7
        
#    def printarea(self):
#        return self.length * self.breadth
    


# In[7]:


# will throw error because of the absence of abstract method printarea
rect1 = Rectangle()


# In[11]:


class Rectangle(Shape):
    type = 'Rectangle'
    side = 4
    
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
        
    def printarea(self):
        return self.length * self.breadth
    


# In[14]:


rect1 = Rectangle(6,7)


# In[15]:


rect1.printarea()


# In[26]:


# another example to implement abstract class and polymorphism


# In[27]:


class Animal:
    
    def __init__(self,name):
        self.name = name
    
    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")


# In[28]:


class Dog(Animal):

    def speak(self):
        return self.name + " Woof!"


# In[29]:


class Cat(Animal):

    def speak(self):
        return self.name + " Meow!"


# In[30]:


fido = Dog('Fido')
ishu = Cat('Ishu')


# In[31]:


fido.speak()


# In[32]:


ishu.speak()


# In[1]:


# special methods
# these are use to run builtin method on our object


# In[9]:


class Book:
    
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    #special method for string representation
    def __str__(self):
        return f'{self.title} by {self.author}'
    
    def __len__(self):
        return self.pages
    


# In[10]:


b = Book('Python','Anand', 150)


# In[11]:


print(b)


# In[12]:


len(b)


# In[16]:


# method to delete variable
del b


# In[14]:


b


# In[ ]:




