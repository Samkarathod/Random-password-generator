import random
import string

def generate_password(length, complexity):
    if complexity == 'low':
        characters = string.ascii_lowercase
    elif complexity == 'medium':
        characters = string.ascii_letters
    elif complexity == 'high':
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        return "Invalid complexity level!"

    password = ''.join(random.choice(characters) for i in range(length))
    return password

# User input
length = int(input("Enter the desired length of the password: "))
complexity = input("Enter the complexity level (low, medium, high): ")

# Generate and display password
print(f"Generated Password: {generate_password(length, complexity)}")