#!/usr/bin/env python
# coding: utf-8

# 100 Days Of Code - Log
# 
# Day 7: November 21, 2023
# 
# **Today's Progress**: 
# 
# 1. Learned python functions and how do we can make them to interact with each other.
# 2. Build up roadmap to work on 1 small mini project
# 3. Explore few methods and worked on it.
# 4. Tried to worked on logic building by debugging code.

# #
# **LOGIC UNITS**

# In[1]:


r1 = [' ',' ',' ']
r2 = [' ',' ',' ']
r3 = [' ',' ',' ']


# In[3]:


def display(row1,row2,row3):
    print(row1)
    print(row2)
    print(row3)


# In[4]:


display(r1,r2,r3)


# In[7]:


r2[0] = 'X'


# In[9]:


display(r1,r2,r3)


# In[29]:


index_position = int(input("Enter the index number: "))


# In[31]:


r3[index_position]


# In[33]:


r2[index_position]


# In[90]:


def user_input():
    result = ' '     # taking a placeholder and considering it as string because input will return str value at first
    while result.isdigit() == False:    # running a loop so that user put a valid output in a correct range as reuired
        result = input("Enter the index number from 0,1,2: ")   # after getting string as output we are typecasting it in a integer
        if result.isdigit() == False:
            print("Uh Oh That's a wrong choice of digit or nat a digit")
    return int(result)


# In[92]:


user_input()


# In[104]:


# We can mak this function in very simple way of taking user input
# But the main motive of building is to add more condition to get only specific and exact required input from user
def user_input():
    
    #variable
    #initial
    #validating two choices
    
    result = ' '     # taking a placeholder and considering it as string because input will return str value at first
    input_range = range(0,11)
    valid_range = False
    while result.isdigit() == False or valid_range == False:    # running a loop so that user put a valid output in a correct range as reuired
        result = input("Enter the index number from 0,1,2: ")   # after getting string as output we are typecasting it in a integer
        
        # This condition is only for digit check if False then again this loop will run
        if result.isdigit() == False:
            print("Uh Oh !!! That's a wrong choice of digit or not a digit")
        
        # This condition is for valid input range check if true then this loop will operate
        if result.isdigit() == True:
            if int(result) in input_range:
                valid_range = True
            else:
                print("Uh Oh !!! The digit is not in specific range (0-10) ")
                valid_range = False
        
    return int(result)


# In[106]:


user_input()


# #

# In[11]:


def display_game(l1):
    print("Here is the current list")
    print(l1)


# In[35]:


lst1 = [0,1,2]
display_game(lst1)


# In[13]:


def user_choice():
    choice = ' '
    while choice not in ['0','1','2']:

        choice = input("Enter the valid index choice from 0,1,2: ")
        
        if choice not in ['0','1','2']:
            print("Uh oh! That's incorrect or invalid index option")
        
    return int(choice)


# In[19]:


user_choice()


# In[15]:


def placing_value(main_list, selected_choice):
    
    value = input("Enter the value you want to place at the above selected choice: ")
    
    main_list[selected_choice] = value
    
    return main_list


# In[37]:


placing_value(lst1, 2)


# In[17]:


# We are making thi sfunction for the continuation of the game
def game_on():
    
    choice = ' '
    while choice not in ['Y', 'N']:
        choice = input("Do you what to play Game? Yes or No (Y/N): ")
        
        if choice not in ['Y', 'N']:
            print("Oh Sorry! I didn't get you.")
    
    if choice == 'Y':
        return True
    else:
        return False


# In[43]:


game_on()


# In[23]:


# Game contruction
game = True
game_lst = [0,1,2]


while game:
    # display list
    display_game(game_lst)

    # take user index choice
    choice = user_choice()
    
    # place value of user choice
    game_list = placing_value(game_lst, choice)
    
    display_game(game_lst)
    
    # Now we will run game's next step based upon the game_on function i.e. on players choice selection
    game = game_on()
    


# #
# 
# 3 things we learn from this example
# 1. ability to display user option
# 2. accept user input
# 3. validate user input
# 4. assigning the changes in user input
# 5. Getting more user information to continue playing

# In[ ]:




