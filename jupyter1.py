#!/usr/bin/env python
# coding: utf-8

# #                                         Ans  # 01:
# OBJECT ORIENTED PROGRAMMING:Object Oriented Programming Is a Paradigim in which real-world objects are each viewed as separate entities having their own state which is modified only by built in procedures, called methods.
#                                                   OR
#                                                   
# Object-Oriented Programming is a methodology or paradigm to design a program using classes and objects. It simplifies software development and maintenance by providing some concepts:
# 
# o	Object
# 
# o	Class
# 
# o	Inheritance
# 
# o	Polymorphism
# 
# o	Abstraction
# 
# o	Encapsulation
#                                      
#                                             Ans#02:
# BENEFITS OF OOP’S:
# 
# 1.OOPs makes development and maintenance easier, whereas, in a procedure-oriented programming language, it is not easy to manage if code grows as project size increases.
# 
# 2.OOPs provides data hiding, whereas, in a procedure-oriented programming language, global data can be accessed from anywhere.
# 
# 3.The Class is Shareable So Code Can Be Reused.
# 
# 4.The Productivity of Programmer Increases.
# 
#                                           
#                                           Ans#03:
# Function                                      /             Method                    
# 1.Function Does Not Have Any Refrence          1.Methods Are Called By Refrence 
# Variable.	                                      Variable.
#                                                 
# 2.All Data That Is Passed to a function         2.it is implicitly Passed The Object 
# Is explicitly Passed.                              For Which it was called.
# 
# 3.It does not have acess controlling            3.It has acess Controlling.	
# 
#                                              
#                                              Ans#04:
# OBJECT:
# Any entity that has state and behavior is known as an object. For example, a chair, pen, table, keyboard, bike, etc. It can be physical or logical.
# An Object can be defined as an instance of a class. An object contains an address and takes up some space in memory. Objects can communicate without knowing the details of each other's data or code. The only necessary thing is the type of message accepted and the type of response returned by the objects.
# Example: A dog is an object because it has states like color, name, breed, etc. as well as behaviors like wagging the tail, barking, eating, etc.
# 
# ClASS:
# Collection of objects is called class. It is a logical entity.
# A class can also be defined as a blueprint from which you can create an individual object. Class doesn't consume any space.
# 
# ATTRIBUTE:
# An attribute is defined as a quality or characteristic of a person, place, or thing. Real life individuals and fictional characters possess various attributes.	
# 
# Behaviour:
# The behavior of an object is defined by its methods, which are the functions and subroutines defined within the object class. ... Methods determine what type of functionality a class has, how it modifies its data, and its overall behavior.
# 

# In[1]:


class Car:
    def __init__(self, name, brand, model, color, doors):
        self.name = name
        self.brand = brand
        self.model = model
        self.color = color
        self.doors = doors
    def printCar(self):
        print(self.name, self.brand, self.model, self.color,self.doors)
    def drive(self):
        print(self.name,"is now being driven")
    def stop(self):
        print(self.name,"is stopped")
        
car1 = Car("Honda", "City", "2005", "White", 4)
car2 = Car("Swift", "Suzuki", "2011", "Blue", 2)
car3 = Car("Fe22", "Ferrari", "2011", "Green", 4)
car4 = Car("Corolla", "Toyota", "2012", "Red", 2)
car5 = Car("Vitz", "Honda", "2019", "Gray", 4)
car2.printCar()
car4.stop()
car2.drive()







