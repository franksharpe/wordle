import random
import string

# Open the file and read the words
with open("C:\\Users\\Frank\\Desktop\\wordle project\\words.txt", "r") as f:
    allText = f.read()
    words = list(map(str, allText.split()))

# Choose a random word from the list
wordto = random.choice(words)

# Print the alphabet from a to z using lowercase ASCII letters.
print("Alphabet from a-z:")
print(" ".join(string.ascii_lowercase))

# Function to provide feedback on the guessed word
def check_guess(guess, wordto):
    feedback = []  # This will store feedback on each letter
    for i in range(len(guess)):
        if guess[i] == wordto[i]:
            feedback.append(f"{guess[i]}: Correct position")
        elif guess[i] in wordto:
            feedback.append(f"{guess[i]}: Wrong position")
        else:
            feedback.append(f"{guess[i]}: Not in word /n /n /n")
    return feedback

# Function to handle a single guess
def handle_guess(guess, wordto):
    if len(guess) > 5:
        print("Error! Only 5 characters allowed!")
        return False
    elif not guess.isalpha():
        print("Error! Only alphabetic characters are allowed.")
        return False
    else:
        guess = guess.lower()
        feedback = check_guess(guess, wordto)
        for f in feedback:
            print(f)
        return guess == wordto

# Loop to allow multiple guesses (5 in this case)
for attempt in range(1, 6):
    guess = input(f"\nGuess {attempt} (You have {6 - attempt} attempts left): ")
    if handle_guess(guess, wordto):
        print("You win!")
        break
else:
    print(f"Game over! The correct word was: {wordto}")
