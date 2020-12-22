#!/usr/bin/env python
# coding: utf-8

# In[32]:


circumference = float(input("Enter the circumference of the Circle:"))
radius = (circumference / (2 * 3.1416))
area = (radius**2) * 3.1416
print(area)


# In[ ]:





# In[47]:


entered_string = input("Enter a 5 character string:")
v = lambda x: x[0:1]
w = lambda x: x[1:2]
x = lambda x: x[2:3]
y = lambda x: x[3:4]
z = lambda x: x[4:5]
z(entered_string)
y(entered_string)
x(entered_string)
w(entered_string)
v(entered_string)
print(z(entered_string),y(entered_string),x(entered_string),w(entered_string),v(entered_string))


# In[ ]:





# In[5]:


def sum_of_numbers(entered_number):
    sum = 0
    while entered_number > 0:
        sum += entered_number
        entered_number -=1
    return sum

entered_number = float(input("Enter A Number:"))
final_sum = sum_of_numbers(entered_number)
print("Sum of Numbers within the number:",final_sum)


# In[ ]:





# In[7]:


sum_of_squared_numbers = 0
including_number = (entered_number + 1)
for i in range(int(including_number)):
    sum_of_squared_numbers = sum_of_squared_numbers + (i ** 2)

square_of_sum_of_numbers = 0
for i in range(int(including_number)):
    square_of_sum_of_numbers += i
    final_square_of_sum = square_of_sum_of_numbers ** 2
    
entered_number = int(input("Enter A Number:"))
including_number = (entered_number + 1)
final_sum = sum_of_squared_numbers
final_squared_sum = final_square_of_sum
final_answer = final_squared_sum - final_sum
print(final_sum)
print(final_squared_sum)
print(final_answer)


# In[ ]:





# In[ ]:


entered_money = int(input("Please Enter Money you want changed:"))
print((entered_money//100), "1 Peso/s")
entered_money = (entered_money%100)
print((entered_money//25), "25 Cents")
entered_money = (entered_money%100)
print((entered_money//10), "10 Cents")
entered_money = (entered_money%100)
print((entered_money//5), "5 Cents")
entered_money = (entered_money%100)
print((entered_money//1), "1 Cent/s")
entered_money = (entered_money%100)

