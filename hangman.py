import random

fruits_list = ["kiwi", "papaya", "cherry", "lemon", "guava"]
secret_word = random.choice(fruits_list)

used_letters = []
chances = 6

print(" Welcome to Fruit Guess Game")

while chances > 0:
    output = ""
    for ch in secret_word:
        if ch in used_letters:
            output += ch
        else:
            output += "*"

    print("\nWord:", output)
    print("Attempts left:", chances)

    if "*" not in output:
        print(" You won! The word is:", secret_word)
        break

    user_letter = input("Enter a letter: ").lower()

    if user_letter in used_letters:
        print("Already tried this letter.")
    elif user_letter in secret_word:
        print("Nice! Correct letter.")
        used_letters.append(user_letter)
    else:
        chances -= 1
        used_letters.append(user_letter)
        print("Oops! Wrong letter.")

if chances == 0:
    print(" Game Over! Word was:", secret_word)
