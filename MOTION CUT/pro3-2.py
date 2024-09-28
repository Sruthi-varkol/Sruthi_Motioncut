import tkinter as tk
import random

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Challenge")
        
        self.words = ["python", "developer", "hangman", "challenge", "programming", "interface", "computer"]
        self.word_to_guess = random.choice(self.words).lower()
        self.guessed_letters = set()
        self.incorrect_guesses = 0
        self.max_incorrect_guesses = 6

        # Display widgets
        self.word_label = tk.Label(root, text=self.get_word_state(), font=("Arial", 24))
        self.word_label.pack(pady=10)
        
        self.guess_entry = tk.Entry(root, font=("Arial", 14))
        self.guess_entry.pack(pady=5)
        
        self.submit_button = tk.Button(root, text="Guess", command=self.check_guess)
        self.submit_button.pack(pady=5)

        self.incorrect_label = tk.Label(root, text=f"Incorrect guesses: {self.incorrect_guesses}/{self.max_incorrect_guesses}", font=("Arial", 14))
        self.incorrect_label.pack(pady=5)

        self.guessed_label = tk.Label(root, text=f"Guessed letters: {', '.join(self.guessed_letters)}", font=("Arial", 14))
        self.guessed_label.pack(pady=5)

    def get_word_state(self):
        return " ".join([letter if letter in self.guessed_letters else "_" for letter in self.word_to_guess])

    def check_guess(self):
        guess = self.guess_entry.get().lower()
        self.guess_entry.delete(0, tk.END)
        
        if len(guess) != 1 or not guess.isalpha():
            return
        
        if guess in self.guessed_letters:
            return
        elif guess in self.word_to_guess:
            self.guessed_letters.add(guess)
        else:
            self.incorrect_guesses += 1
            self.guessed_letters.add(guess)
        
        self.update_display()

        if all(letter in self.guessed_letters for letter in self.word_to_guess):
            self.word_label.config(text=f"Congratulations! You guessed the word '{self.word_to_guess}'")
            self.submit_button.config(state=tk.DISABLED)
        elif self.incorrect_guesses >= self.max_incorrect_guesses:
            self.word_label.config(text=f"Game over! The word was '{self.word_to_guess}'")
            self.submit_button.config(state=tk.DISABLED)

    def update_display(self):
        self.word_label.config(text=self.get_word_state())
        self.incorrect_label.config(text=f"Incorrect guesses: {self.incorrect_guesses}/{self.max_incorrect_guesses}")
        self.guessed_label.config(text=f"Guessed letters: {', '.join(sorted(self.guessed_letters))}")

if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()
