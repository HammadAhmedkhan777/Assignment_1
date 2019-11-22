#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Python Program To make a simple calculator that perform addition, multiplication,division and subtraction
# This function adds two numbers 
def add(x, y):
   return x + y
# This function subtracts two numbers 
def subtract(x, y):
   return x - y
# This function multiplies two numbers
def multiply(x, y):
   return x * y
# This function divides two numbers
def divide(x, y):
   return x / y
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
# Take input from the user 
choice = input("Enter choice(1/2/3/4): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))
elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))
elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))
elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("Invalid input")


# In[2]:


test_list = [ 1, 6, 3, 5, 3, 4 ] 
print("Checking if 4 exists in list ( using loop ) : ") 
for i in test_list: 
    if(i == 4) : 
        print ("Element Exists") 
  
print("Checking if 4 exists in list ( using in ) : ") 
if (4 in test_list): 
    print ("Element Exists")


# In[3]:


d = {0:10, 1:20}
print(d)
d.update({2:30})
print(d)


# In[4]:


# Python3 Program to find sum of  
# all items in a Dictionary 
  
# Function to print sum 
def returnSum(myDict): 
      
    sum = 0
    for i in myDict: 
        sum = sum + myDict[i] 
      
    return sum
  
# Driver Function 
dict = {'a': 100, 'b':200, 'c':300} 
print("Sum :", returnSum(dict))


# In[5]:


my_list = [20,30,20,30,40,50,15,11,20,40,50,15,6,7]
 
my_list.sort()
print(my_list)
 
new_list = sorted(set(my_list))
dup_list =[]
 
 
for i in range(len(new_list)):
        if (my_list.count(new_list[i]) > 1 ):
            dup_list.append(new_list[i])
        
print(dup_list)


# In[6]:


d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def is_key_present(x):
  if x in d:
      print('Key is present in the dictionary')
  else:
      print('Key is not present in the dictionary')
is_key_present(5)
is_key_present(9)


# In[ ]:




