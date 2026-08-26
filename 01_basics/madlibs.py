# ==================== Mad Libs Word Game ====================

"""
Mad Libs Game Overview:
- Interactive text game that prompts the user for various parts of speech (nouns, adjectives, verbs).
- Injects collected user inputs into a predefined story template.
- Core Concepts Covered:
    - String inputs using input()
    - Multiple variable management
    - Formatted string literals (f-strings) for dynamic narrative generation
"""

# ==================== 1. Word Inputs ====================
# Prompting user for specific word categories to populate the story placeholders.
adjective1 = input("Enter an adjective (description): ")
noun1 = input("Enter a noun (person, place, thing: ")
adjective2 = input("Enter an adjective (description): ")
verb1 = input("Enter a verb ending with 'ing': ")
adjective3 = input("Enter an adjective (description): ")

# ==================== 2. Story Output ====================
# Interpolates the collected words directly into the story sentences using f-strings.
print(f"Today I went to a {adjective1} zoo.")
print(f"In an exhibit, I saw an {noun1}.")
print(f"{noun1} was {adjective2} and {verb1}.")
print(f"I was {adjective3}!")

