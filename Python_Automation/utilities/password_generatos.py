import random
import string

# Password settings
password_length = 12

# Characters to use
letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

all_characters = letters + numbers + symbols

# Generate password
password = ""

for i in range(password_length):
    password += random.choice(all_characters)

print("Generated Password:")
print(password)