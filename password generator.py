#PASSWORD GENERATOR CODSOFT TASK 
import random
letters=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

numbers =['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols=['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '|', '<', '>', '?']

all_characters =letters+numbers+symbols
password_length=int(input("How long would you like your password to be?\nPlease enter a number: "))

password_list=[]
for char in range(0,password_length):
    password_list.append(random.choice(all_characters))

password=""
for char in password_list :
    password +=char
print(f"Your password is:\n{password }")