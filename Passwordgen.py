import random

length = int(input("Entre the length of the password: ")) # asking for length of password

char_for_passwords = ['$', 'x', 'n', '*', 'z', '6', '#', 'R', '^', 'Y', 'm','7', ';', 'h', 'U', '-', 'G', 'l', 'c', 'I', '?', 'M', 'w', 'D', '=', 'V', 'J', 'Z', 'e', 'F', 'H', 'b', 'f', 'u', '2', 'T', 'g', 't', 'N', '@', 'X',  'p', '9', '!', 'i', '0', 'B', 'E', '+', 'K', '3', 'q', 's', 'j', 'O', 'v', 'Q', 'a', 'S', '8', '1', '4', 'L', 'y', 'k', '&', 'A', 'P', 'd', '5', 'r', 'o', 'C',  'W']   # list of character to make password

password = '' # Empty string to store password

for i in range(length): # loop to form a random password
    random_word = random.choice(char_for_passwords)
    password += random_word

print(password)