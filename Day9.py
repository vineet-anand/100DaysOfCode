#!/usr/bin/env python
# coding: utf-8

# 100 Days Of Code - Log
# 
# Day 9: January 1, 2024
#
# **Today's Progress:**
# 
#
# 1. Learned Abstraction & Encapsulation Concept
# 2. Learned about Inheritance and it's types

# In[ ]:





# In[ ]:





# In[ ]:





# # **Object Oriented Programming (OOPS) Part 2**

# **Abstraction & Encapsulation**
# 1. Seggregation of any component is known as abstraction.
# 2. There could be any Level of abstraction.
# 3. Hinding the abstraction level is known as encapsulation
# 4. In other word Hiding the implementation detail is known as encapsulation

# **Inheritance**

# **Single Inheritance**
# 1. Single Inheritance is a property where any object inherit it's property from other parent or other supporting class

# In[45]:


class Employee:
    
    no_of_leaves = 9
    
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
        
    
# Here we are inheriting the employee properties into the programmer class 
# We are doing this by passing Employee class name into the programmers argument

class Programmer(Employee):
    
    noof_holiday_packages = 58
    
# Note: Not using super to inherit the parent class constructor variable properties, will do it later

    def __init__(self,name,salary,role,language):
        self.name = name
        self.salary = salary
        self.role = role
        self.language = language
    
    def printprog(self):
        return f"my programmer's name is {self.name}, I earn {self.salary} for the job role of {self.role} in {self.language} language"
    


# In[46]:


harry = Employee('Harry',255,'Analyst')
rohan = Employee('Rohan',745,'Devops')


# In[47]:


shubham = Programmer('Shumbham', 578,'DSA Coder',['Python','Java'])
karan = Programmer('Karan', 254, 'Decorator',['Python'])


# In[48]:


shubham.printprog()


# In[49]:


karan.printdetails()


# In[50]:


karan.noof_holiday_packages


# **Multiple Inheritance**

# In[29]:


# creating 1st class for person who is an employee
class Employee:
    
    no_of_leaves = 9
    
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
        
# creating 2nd class for person who is a player in any game
class Player:
    no_of_game = 4
    
    var = 30
    
    def __init__(self,name,game):
        self.name = name
        self.game = game
    
    def printplayerdetails(self):
        return f'my name is {self.name}, I play {self.game} game'
    
# creating 3rd class for multiple iheritance... 
# ...where this class will inherit the property of both 1st Employee & 2nd Player class

# Order in multiple inheritance matters while passing class name as an argument

# Note: whatever class be pass in 1st order get the highest precedence... 
# ...on untilizing the Method or Attribute define with same name in both the classes AFTER the class in which it is passing
# for example var define in coolproger get 1st precedence followed by Employee then player class
class CoolProgrammer(Employee,Player):
    language = 'C++'
    
#    var = 40
    
    def printlanguage(self):
        print(self.language)
    
    


# In[30]:


harry = Employee('Harry',255,'Analyst')
rohan = Employee('Rohan',745,'Devops')


# In[31]:


shubham = Player('Shubham',['Chess','Cricket'])


# In[32]:


karan = CoolProgrammer('Karan',997,'CoolProg')


# In[33]:


karan.printdetails()


# In[34]:


karan.printlanguage()


# In[35]:


karan.var


# **Multilevel Inheritance**

# In[15]:


class Dad:
    basketball = 1

class Son(Dad):
    dance = 1
    
    def isdance(self):
        return f'yes I dance {self.dance} times'

class GrandSon(Son):
    dance = 6
    
    # overriding is happening on son class and this will prioritize
    def isdance(self):
        return f'yes I dance a lot by {self.dance} times'
    


# In[16]:


darry = Dad()
larry = Son()
harry = GrandSon()


# In[17]:


# when Grandson function is active
# it will use the same class method and attribute
harry.isdance()


# In[14]:


# when Grandson function is inactive
# it will use the inhertited class method and active attribute
harry.isdance()


# In[18]:


harry.basketball

