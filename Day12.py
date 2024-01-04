#!/usr/bin/env python
# coding: utf-8

# 100 Days Of Code - Log
# 
# Day 12: January 4, 2024
# 
# **Today's Progress:**
#
#
# 1. Learned about Exception handling
# 2. Got to know about try, except, finally
# 3. Worked on exception handling in combination of functions and loops
#
#
# **Exception Handling**

# In[15]:


# Exception handling is the concept to consider something in the event of error...
# ...and proceed with the further important executions of code


# In[28]:


num1 = input()
num2 = input()
try:    
    print(int(num1) + int(num2))
except Exception as e:             # Here it's handling exception in case of error
    print(e)
    print("This an another way to call except Block")

print('This line is important to consider!')


# In[17]:


def add(n1,n2):
    return n1+n2


# In[18]:


add(4,5)


# In[19]:


n1 = 10


# In[20]:


# creating error for example
n2 = input('Kindly provide Number: ')


# In[23]:


# further block of code 
add(n1,n2)
print('Something Happened!')


# In[34]:


try:
    # want to attemp this code
    # may have an error
    result = 10 + 10
except:
    print("Hey it looks you're not adding properly")
else:
    print("Addition went well!")
    print(result)


# In[33]:


result


# In[1]:


try:
    f = open('testfile','w')
    f.write("Write a test line")
except TypeError:
    print("There was a Type Error")
except OSError:
    print("Hey you have an OS Error")
finally:
    print("I'll always execute")
    


# In[2]:


try:
    f = open('testfile','r')
    f.write("Write a test line")
except TypeError:
    print("There was a Type Error")
except OSError:
    print("Hey you have an OS Error")
finally:
    print("I'll always execute")
    


# In[3]:


try:
    f = open('testfile','r')
    f.write("Write a test line")
except TypeError:
    print("There was a Type Error")
except:
    print("All other exception")
finally:
    print("I'll always execute")
    


# In[4]:


try:
    f = open('testfile','r')
    f.write("Write a test line")
except:
    print("All other exception")
finally:
    print("I'll always execute")
  


# In[5]:


try:
    f = open('testfile','w')
    f.write("Write a test line")
except:
    print("All other exception")
finally:
    print("I'll always execute")
  


# In[6]:


# exceptional handling on function where to get specific input from user


# In[1]:


def as_for_int():
    try:
        result = int(input("Get User input of number:"))
    except:
        print("Oops! that's not a number")
    finally:
        print("End of Exceptions")


# In[2]:


as_for_int()


# In[3]:


as_for_int()


# In[1]:


def as_for_int():
    
    while True:
        try:
            result = int(input("Get User input of number:"))
        except:
            print("Oops! that's not a number")
            continue
            
        else:
            print("Thanks for integeral input")
            break
        finally:
            print("End of Exceptions")
            print("I'll always run")


# In[2]:


as_for_int()


# In[3]:


as_for_int()


# In[ ]:




