"""
title: bruh2
author: CHH892A
date: 6/26/19 10:25 AM
"""
import random
name = input("What is your name: ")
salary = int(input("Whats ur salary: "))
raise_per = random.randint(0,100)
print (name + " your raise is " + str(raise_per) + "%")
raise_amount = (salary + (salary * (raise_per * .01)))
print (name + " your new salary is " + str(raise_amount))