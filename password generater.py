import random
import string

def check_strength(password):
    if len(password) < 8:
        return 'Weak'
    elif len(password) < 12:
        return 'Medium'
    else:
        return 'Strong'

def generate_password(length=12, use_uppercase=True, use_lowercase=True, use_digits=True, 
                      use_special=True, avoid_common=False, difficulty='hard'):
    available_characters = ''
    if use_uppercase:
        available_characters += string.ascii_uppercase
    if use_lowercase:
        available_characters += string.ascii_lowercase
    if use_digits:
        available_characters += string.digits
    if use_special:
        available_characters += string.punctuation
    
    password = []
    if use_uppercase:
        password.append(random.choice(string.ascii_uppercase))
    if use_lowercase:
        password.append(random.choice(string.ascii_lowercase))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_special:
        password.append(random.choice(string.punctuation))
    
    password += random.choices(available_characters, k=length - len(password))
    if avoid_common:
        common_passwords = {'123456', 'password', '123456789', '12345', 'qwerty', 'abc123'}
        while ''.join(password) in common_passwords:
            password = generate_password(length, use_uppercase, use_lowercase, use_digits, 
                                         use_special, avoid_common, difficulty)
    
    if difficulty == 'easy':
        password = random.choices(available_characters, k=min(length, 8))
    elif difficulty == 'hard':
        password = random.choices(available_characters, k=length)

    random.shuffle(password)
    password_str = ''.join(password)
    strength = check_strength(password_str)
    
    return password_str, strength

password_length = 16  
password, strength = generate_password(length=password_length, difficulty='hard')

print(f"Generated password: {password}")
print(f"Password strength: {strength}")
