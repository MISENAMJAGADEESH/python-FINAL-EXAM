# -*- coding: utf-8 -*-
"""pythonIA1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Z8O9xYwrgCHDiKCEz2ozx26BOrPBJLZV
"""

#1
length = int(input("Enter a length: "))
width = int(input("Enter a width: "))
print (length*width)

#2
weight = int(input("Enter the weight in kg :"))
height = int(input("Enter the height in m :"))
print (weight/height^2)

#3
new_dictionary = {'abdul':50,'mahesh':34,'suresh':35,}
print(abdul())

#4
def classify_age():
    age = int(input("Enter an age: "))
    if age < 18:
        print('minor')
    elif 18 <= age < 60:
        print('adult')
    else:
        print('senior')
classify_age()

#5
start = 0
end = 50

for num in range(start, end + 1):
    if num % 2 == 0:
        print(num)

#6
def password_prompt():

    correct_password = "latentview"

    while True:
        user_password = input("Enter the password: ")
        if user_password == correct_password:
            print("Password correct. Access granted!")
            break
        else:
            print("Incorrect password. Please try again.")
# Call the function to start the password prompt
password_prompt()

#7
def average_of_list(num):
    if len(num) == 0:
        return None
    else:
        total = sum(num)
        average = total / len(num)
        return average
num = [10, 20, 30, 40, 50]
avg = average_of_list(num)
print("Average:", avg)

#8
def count(s):
  count = 0
  for char in s:
    if char in ['a','e','i','o','u']:
      count +=1
  return count
string = input('Enter the string : ')
result = count(string)
print(result)

#9
from datetime import datetime
current_date =datetime.now()
print(current_date)

#10
a = "hi"
b = 200
try:
  print(a+b)
except:
  print("sum not possible")

#11
try:
    integer = int(input("Enter the integer: "))
    print("integer")
except ValueError:
    print("not integer")

#12
try:
    value1 = int(input("enter a value"))
    value2 = int(input("enter a value"))
    print("value1 / value2 = 0")
except valueError:
    print("error")

#13
with open("example.txt", "w") as file:
    file.write("Hello Python!\n")

#14
with open("example.txt", "r") as file:
    content = file.read()
    print("Content of the file:", content)

#15
with open("example.txt", "a") as file:
    file.write("This is a new line.\n")