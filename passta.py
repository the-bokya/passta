#!/bin/python3
import random
import string
from getpass import getpass
length = int(input("Enter the length of the password to be generated: "))
password = getpass("Enter your password: ")
salt = getpass("Enter salt: ")
secure_password = ""
random.seed(password+str(length)+salt)
for i in range(length):
  secure_password += random.choice(string.printable[:95])

print(secure_password)
