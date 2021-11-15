import string
import random

# prompt for length of pw
pw_type = input('What is the password for? ')
pw_length = int(input('Length of password? '))

# define data to use
lower = string.ascii_lowercase
upper = string.ascii_uppercase
nums = string.digits
special_chars = string.punctuation

# create pool of eligible chars
char_pool = lower + upper + nums + special_chars

# use sample method to create list of pw_length unique random number of
# elements from char pool
temp = random.sample(char_pool, pw_length)

# combine list to create pw string
password = ''.join(temp)

# open file in append mode. create file if it doesn't exist.
fo = open('passwords.txt', 'a')

# write where pw is used, pw, and new line so each password starts on new line
fo.write(pw_type + ': ' + password + '\n')

# close file
fo.close()

