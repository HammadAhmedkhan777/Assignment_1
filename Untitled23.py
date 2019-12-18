#!/usr/bin/env python
# coding: utf-8

# In[1]:


num = int(input("Enter number:"))
factorial = 1
# check if the number is negative, positive or zero
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)


# In[2]:


def string_test():
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    a=input("Enter Letter:")
    for c in a:
        if c.isupper():
           d["UPPER_CASE"]+=1
        elif c.islower():
           d["LOWER_CASE"]+=1
        else:
           pass
    print ("Original String : ", a)
    print ("No. of Upper case characters : ", d["UPPER_CASE"])
    print ("No. of Lower case Characters : ", d["LOWER_CASE"])

string_test()


# In[3]:


list1 = [10, 21, 4, 45, 66, 93] 
  
# iterating each number in list 
for num in list1: 
      
    # checking condition 
    if num % 2 == 0: 
       print(num, end = " ")


# In[4]:


def isPalindrome(string):
	left_pos = 0
	right_pos = len(string) - 1
	
	while right_pos >= left_pos:
		if not string[left_pos] == string[right_pos]:
			return False
		left_pos += 1
		right_pos -= 1
	return True
print(isPalindrome('aza')) 


# In[5]:


def test_prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True;
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True             
print(test_prime(9))


# In[ ]:




