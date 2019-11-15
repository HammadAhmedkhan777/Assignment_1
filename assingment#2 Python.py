#!/usr/bin/env python
# coding: utf-8

# In[1]:


sub1=float(input("Enter marks of the first subject: "))
sub2=float(input("Enter marks of the second subject: "))
sub3=float(input("Enter marks of the third subject: "))
sub4=float(input("Enter marks of the fourth subject: "))
sub5=float(input("Enter marks of the fifth subject: "))
avg=(sub1+sub2+sub3+sub4+sub4)/5
if(avg>=90):
    print("Grade: A")
elif(avg>=80 and avg<90):
    print("Grade: B")
elif(avg>=70 and avg<80):
    print("Grade: C")
elif(avg>=60 and avg<70):
    print("Grade: D")
else:
    print("Grade: F")


# In[2]:


num = int(input("Enter a number: "))
mod = num % 2
if mod > 0:
    print("This is an odd number.")
else:
    print("This is an even number.")


# In[3]:


a = [] 
a.append("Hammad") 
a.append("khan") 
a.append("For") 
a.append("king") 
print("The length of list is: ", len(a))


# In[5]:


lst = []
num = int(input('How many numbers: '))
for n in range(num):
    numbers = int(input('Enter number '))
    lst.append(numbers)
print("Sum of elements in given list is :", sum(lst))


# In[12]:


lst = []
num = int(input('How many numbers: '))
for n in range(num):
    numbers = int(input('Enter number '))
    lst.append(numbers)
print("Maximum element in the list is :", max(lst),)


# In[13]:


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for i in a:

    if i < 5:

        print(i)


# In[ ]:




