import random
import string

def generate_password(length, use_uppercase, use_numbers, use_symbols):
    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if use_uppercase else ''
    digits = string.digits if use_numbers else ''
    symbols = string.punctuation if use_symbols else ''

    # Combine all character sets
    all_characters = lowercase + uppercase + digits + symbols

    if not all_characters:
        raise ValueError("At least one character set must be selected.")

    # Generate password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    
    # Get user input
    length = int(input("Enter the desired password length: "))
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    # Generate password
    password = generate_password(length, use_uppercase, use_numbers, use_symbols)
    
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
