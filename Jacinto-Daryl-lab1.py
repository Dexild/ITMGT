#!/usr/bin/env python
# coding: utf-8

# 192527
# Jacinto
# 2 BS ITE

# In[ ]:


def final_dollars_to_pesos(us_dollars):
    dollars_to_pesos = (us_dollars * 48.45)
    return dollars_to_pesos


# In[ ]:


us_dollars = float(input("Enter the amount in US Dollars:"))
dollars_to_pesos = final_dollars_to_pesos(us_dollars)
print (us_dollars, "US dollar(s) = ", dollars_to_pesos)


# In[ ]:





# In[ ]:


def final_integer(first_integer, second_integer):
    sum_integer = (first_integer + second_integer)
    difference_integer = (first_integer - second_integer)
    product_integer = (first_integer * second_integer)
    quotient_integer = (first_integer // second_integer)
    remainder_integer = (first_integer % second_integer)
    return sum_integer, difference_integer, product_integer, quotient_integer, remainder_integer


# In[ ]:


first_integer = float(input("Enter the First Integer:"))
second_integer = float(input("Enter the Second Integer:"))
sum_integer = final_integer(first_integer, second_integer)
difference_integer = final_integer(first_integer, second_integer)
product_integer = final_integer(first_integer, second_integer)
quotient_integer = final_integer(first_integer, second_integer)
remainder_integer = final_integer(first_integer, second_integer)
print (*sum_integer, sep = "\n")


# In[ ]:





# In[ ]:


def final_bmi(weight_integer, height_integer):
    quotient_bmi_integer = ((height_integer / 100)**2)
    bmi = (weight_integer/(quotient_bmi_integer))
    return bmi


# In[ ]:


weight_integer = float(input("Enter Weight in kilograms:"))
height_integer = float(input("Enter Height in centimeters:"))
quotient_bmi_integer = final_bmi(weight_integer, height_integer)
bmi = final_bmi(weight_integer, height_integer)
print (bmi)

