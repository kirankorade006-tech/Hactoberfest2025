# random_quote.py
# Author: Your Name
# Date: October 2025
# Description: A simple Python script that prints a random programming quote.
# Perfect for Hacktoberfest contributions! 🎃

import random

def get_random_quote():
    """
    Returns a random programming quote from a predefined list.
    """
    quotes = [
        "Talk is cheap. Show me the code. — Linus Torvalds",
        "Programs must be written for people to read, and only incidentally for machines to execute. — Harold Abelson",
        "First, solve the problem. Then, write the code. — John Johnson",
        "Experience is the name everyone gives to their mistakes. — Oscar Wilde",
        "In order to be irreplaceable, one must always be different. — Coco Chanel",
        "Simplicity is the soul of efficiency. — Austin Freeman",
        "Code never lies, comments sometimes do. — Ron Jeffries"
    ]
    return random.choice(quotes)

def main():
    print("💻 Random Programming Quote Generator 🎯\n")
    print(get_random_quote())

if __name__ == "__main__":
    main()
