import random
import string

# Prompt the user to input desired password length
length = int(input("Enter the desired password length: "))

# Define character sets to include in the password
uppercase_letters = string.ascii_uppercase
lowercase_letters = string.ascii_lowercase
digits = string.digits
symbols = string.punctuation

# Combine all character sets
all_characters = uppercase_letters + lowercase_letters + digits + symbols

# Generate a random password
password = ''.join(random.choice(all_characters) for _ in range(length))

# Display the generated password
print(f"Generated Password: {password}")
