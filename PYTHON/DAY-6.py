# utilities.py

import math
import random
import string


def roll_and_square() -> tuple:
    """
    Rolls a random integer between 1 and 6 (inclusive) and returns its square.
    
    Returns:
        tuple: (rolled_number, squared_value)
    """
    rolled_number = random.randint(1, 6)
    squared_value = math.pow(rolled_number, 2)
    return rolled_number, squared_value


def generate_password(length: int = 8) -> str:
    """
    Generates a random secure password with letters, digits, and punctuation.
    
    Args:
        length (int): Desired password length. Default is 8.
    
    Returns:
        str: The generated password.
    """
    if length < 4:
        raise ValueError("Password length should be at least 4 characters.")
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


if __name__ == "__main__":
    # Demonstrate roll_and_square
    roll, square = roll_and_square()
    print(f"🎲 Dice rolled: {roll}")
    print(f"📐 Square of the roll: {square}")

    # Generate and print random password
    password = generate_password()
    print(f"🔐 Generated password: {password}")
