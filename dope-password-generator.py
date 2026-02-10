import random
import string

# Welcome message
print("Welcome to Dope Password Generator – Star Wars Edition! 🌌")
print("Generate passwords inspired by a galaxy far, far away...")
print("-" * 40)

# Star wars word bank
star_wars_words = [
    "Jedi", "Sith", "Force", "Lightsaber", "Yoda", "Vader", "Luke", "Leia",
    "Han", "Chewie", "Tatooine", "Hoth", "Endor", "Coruscant", "Naboo",
    "Droid", "Stormtrooper", "Empire", "Rebel", "Falcon"
]

#   password generator function
def generate_passphrase(
    num_words=3,           # how many Star Wars words to use
    separator="-",         # what to put between words: "-", " ", "." , "" etc.
    capitalize=True,       # CapitalizeEachWord?
    add_number=True,       # add digits at the end?
    add_symbol=True,       # add a symbol at the end?
    min_length=14          # we'll warn if it's too short
):
    """
    Creates a readable Star Wars passphrase.
    Examples: Yoda-Luke-Chewie42!
              Force.Han.Rebel77@
    """
    if num_words < 2:
        num_words = 2  # at least 2 words for decent security

    # Pick unique random words (no repeats)
    selected_words = random.sample(star_wars_words, num_words)

    # Capitalize if requested (makes it look nicer)
    if capitalize:
        selected_words = [word.capitalize() for word in selected_words]

    # Join them with the separator
    passphrase = separator.join(selected_words)

    # Add number (two digits so it looks clean)
    if add_number:
        passphrase += str(random.randint(10, 99))  # 10-99 looks better than 0-9 or 000

    # Add one symbol at the end
    if add_symbol:
        passphrase += random.choice("!@#$%^&*?")

    # Quick length check + warning (but still return it)
    if len(passphrase) < min_length:
        print(f"Note: This passphrase is only {len(passphrase)} chars — consider more words or no separator.")

    return passphrase

#flow

print("\nHow would you like your Star Wars passphrase?")

try:
    num_words = int(input("How many words? (recommended 3–5): "))
    if num_words < 2 or num_words > 8:
        print("Using 3 words instead (best balance).")
        num_words = 3
except:
    print("Using 3 words.")
    num_words = 3

sep = input("Separator between words? (hit enter for '-', or type e.g. '.' ' ' '_'): ").strip()
if not sep:
    sep = "-"

use_cap = input("Capitalize each word? (y/n): ").lower().startswith('y')
use_num = input("Add two digits at the end? (y/n): ").lower().startswith('y')
use_sym = input("Add a symbol at the end? (y/n): ").lower().startswith('y')

# Generate it!
pw = generate_passphrase(
    num_words=num_words,
    separator=sep,
    capitalize=use_cap,
    add_number=use_num,
    add_symbol=use_sym
)

# Show result
print("\n" + "=" * 50)
print("   Your Star Wars passphrase:")
print("   " + pw)
print("=" * 50)
print(f"Length: {len(pw)} characters")
print("May the Force be with you! Copy it somewhere safe. 🌌")
