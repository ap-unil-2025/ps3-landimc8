"""
Bonus Challenge: Password Generator
Generate secure passwords with customizable options.
"""

import random
import string
# Note: Ensure these two import lines are at the very top of your file.

def generate_password(length=12, use_uppercase=True, use_lowercase=True,
                     use_digits=True, use_special=True):
    """
    Generate a random password based on criteria.
    """
    # Initialize variables
    characters = ""
    guarantee_chars = []
    
    # 1. Build the character set and ensure minimum requirements are met
    if use_lowercase:
        guarantee_chars.append(random.choice(string.ascii_lowercase))
        characters += string.ascii_lowercase
        
    if use_uppercase:
        guarantee_chars.append(random.choice(string.ascii_uppercase))
        characters += string.ascii_uppercase

    if use_digits:
        guarantee_chars.append(random.choice(string.digits))
        characters += string.digits

    if use_special:
        guarantee_chars.append(random.choice(string.punctuation))
        characters += string.punctuation

    if not characters:
        return "Error: No character types selected!"

    # Initialize the list that will hold the password characters (Fixes NameError)
    password_list = []

    # 2. Ensure at least one character from each selected type
    password_list.extend(guarantee_chars)

    # 3. Fill the rest of the password randomly
    remaining_length = length - len(guarantee_chars)
    
    if remaining_length > 0:
        # Use random.choices to pick remaining characters from the full set
        password_list.extend(random.choices(characters, k=remaining_length))

    # 4. Shuffle the password list to randomize order
    random.shuffle(password_list)

    return ''.join(password_list)


def password_strength(password):
    """
    Rate password strength from 1-5.

    Args:
        password (str): Password to evaluate

    Returns:
        str: Strength rating
    """
    score = 0

# 1. Length Criteria
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1

    # 2. Character Type Criteria
    # Check for presence of character types using any() and sets
    if any(c in string.ascii_lowercase for c in password):
        score += 1 # Contains lowercase
        
    if any(c in string.ascii_uppercase for c in password):
        score += 1 # Contains uppercase
        
    if any(c in string.digits for c in password):
        score += 1 # Contains digits
        
    if any(c in string.punctuation for c in password):
        score += 1 # Contains special characters
    
    # Maximum score is 6, so we limit the index to 5 for the 'Very Strong' rating
    strength = ["Very Weak", "Weak", "Fair", "Good", "Strong", "Very Strong"]
    return strength[min(score, 5)] 


def main():
    """Main function to run the password generator."""
    print("Password Generator")
    print("-" * 30)

    # Get password length from user
    length_input = input("Password length (default 12): ").strip()
    length = int(length_input) if length_input else 12

    # Generate password
    password = generate_password(length)
    print(f"\nGenerated Password: {password}")
    print(f"Strength: {password_strength(password)}")

    # Generate alternative passwords
    print("\nAlternative passwords:")
    for i in range(3):
        alt_password = generate_password(length)
        print(f"{i+1}. {alt_password} ({password_strength(alt_password)})")


if __name__ == "__main__":
    main()