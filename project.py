import random
import string
import tkinter as tk
from tkinter import messagebox

# Initialize the Tkinter root window
root = tk.Tk()
root.title("Wordle Game")
root.geometry("400x300")

# Open the file and read the words
with open("C:\\Users\\Frank\\Desktop\\wordle project\\words.txt", "r") as f:
    allText = f.read()
    words = list(map(str, allText.split()))

# Choose a random word from the list
wordto = random.choice(words)

# Function to check the guess and provide feedback
def check_guess(guess, wordto):
    feedback = []  # This will store feedback on each letter
    for i in range(len(guess)):
        if guess[i] == wordto[i]:
            feedback.append(f"{guess[i]}: Correct position")
        elif guess[i] in wordto:
            feedback.append(f"{guess[i]}: Wrong position")
        else:
            feedback.append(f"{guess[i]}: Not in word")
    return "\n".join(feedback)

# Function to handle the guess and update the UI
def handle_guess():
    guess = gues_entry.get().lower()
    
    if len(guess) != 5:
        messagebox.showerror("Error", "Only 5 characters allowed!")
        return
    elif not guess.isalpha():
        messagebox.showerror("Error", "Only alphabetic characters are allowed!")
        return
    
    feedback = check_guess(guess, wordto)
    feedback_label.config(text=feedback)

    global attempt
    attempt += 1
    if guess == wordto:
        messagebox.showinfo("Congratulations!", "You win!")
        reset_game()
    elif attempt >= 6:
        messagebox.showinfo("Game Over", f"The correct word was: {wordto}")
        reset_game()
    else:
        attempt_label.config(text=f"Attempts left: {6 - attempt}")

# Function to reset the game
def reset_game():
    global wordto, attempt
    wordto = random.choice(words)
    attempt = 0
    gues_entry.delete(0, tk.END)
    feedback_label.config(text="")
    attempt_label.config(text="Attempts left: 6")

# Initialize attempts
attempt = 0

# Set up GUI components
gues_label = tk.Label(root, text="Enter your 5-letter guess:", font=('calibre', 10, 'bold'))
gues_label.pack(pady=10)

gues_entry = tk.Entry(root, font=('calibre', 10, 'normal'))
gues_entry.pack(pady=5)

attempt_label = tk.Label(root, text="Attempts left: 6", font=('calibre', 10, 'bold'))
attempt_label.pack(pady=5)

feedback_label = tk.Label(root, text="", font=('calibre', 10, 'normal'))
feedback_label.pack(pady=10)

guess_button = tk.Button(root, text="Submit Guess", command=handle_guess, font=('calibre', 10, 'bold'))
guess_button.pack(pady=10)

# Run the Tkinter main loop
root.mainloop()
