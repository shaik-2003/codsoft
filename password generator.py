import random
import string

def generate_password(length=12, use_special_chars=True, use_digits=True):
    """Generate a random password.

    Args:
        length (int): Length of the password.
        use_special_chars (bool): Whether to include special characters.
        use_digits (bool): Whether to include digits.

    Returns:
        str: The generated password.
    """
    # Define character sets
    letters = string.ascii_letters
    digits = string.digits if use_digits else ""
    special_chars = string.punctuation if use_special_chars else ""

    # Combine all possible characters
    all_chars = letters + digits + special_chars

    # Ensure the password length is at least 1
    if length < 1:
        raise ValueError("Password length must be at least 1.")

    # Generate the password
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

def main():
    """Main function to interact with the user."""
    print("Welcome to the Password Generator!")
    
    try:
        length = int(input("Enter the desired password length: "))
        use_special_chars = input("Include special characters (Y/N)? ").strip().lower() == 'y'
        use_digits = input("Include digits (Y/N)? ").strip().lower() == 'y'
        
        # Generate the password
        password = generate_password(length, use_special_chars, use_digits)
        print(f"Generated password: {password}")
        
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
