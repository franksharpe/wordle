import random
import string

# Open the file and read the words
f = open("C:\\Users\\Frank\\Desktop\\wordle project\\words.txt", "r")
allText = f.read()
words = list(map(str, allText.split()))

# Choose a random word from the list
wordto = random.choice(words)

# Print the alphabet from a to z using lowercase ASCII letters.
print("Alphabet from a-z:")
for letter in string.ascii_lowercase:
    print(letter, end=" ")

# Function to provide feedback on the guessed word
def check_guess(guess, wordto):
    feedback = []  # This will store feedback on each letter
    for i in range(len(guess)):
        if guess[i] == wordto[i]:
            feedback.append(f"{guess[i]}: Correct position")
        elif guess[i] in wordto:
            feedback.append(f"{guess[i]}: Wrong position")
        else:
            feedback.append(f"{guess[i]}: Not in word")
    return feedback

# Input for guessing the word
guess = input("\nGuess a word: ")

# Check if the input is more than 5 characters
if len(guess) > 5:
    print("Error! Only 5 characters allowed!")
else:
    # Convert all letters to lowercase and ensure the guess contains only letters
    if guess.isalpha():
        guess = guess.lower()
        print(f"Your processed guess is: {guess}")

        # Convert guess and wordto to lists and print them
        guess_list = list(guess)
        wordto_list = list(wordto)

        print(f"The randomly chosen word is: {''.join(wordto_list)}")

        # Provide feedback on the guess
        feedback = check_guess(guess, wordto)
        for f in feedback:
            print(f)
    else:
        print("Error! Only alphabetic characters are allowed.")
