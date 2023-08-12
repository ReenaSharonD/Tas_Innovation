import tkinter as tk
from tkinter import messagebox
import random

class GuessNumberGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Guess the Number Game")
        
        self.target_number = random.randint(1, 100)
        self.max_attempts = 10
        self.attempts = 0
        self.score = 100
        
        self.label = tk.Label(root, text="Guess a number between 1 and 100:")
        self.label.pack()
        
        self.entry = tk.Entry(root)
        self.entry.pack()
        
        self.submit_button = tk.Button(root, text="Submit", command=self.check_guess)
        self.submit_button.pack()
        
    def check_guess(self):
        guess = int(self.entry.get())
        self.attempts += 1
        
        if guess == self.target_number:
            messagebox.showinfo("Congratulations!", f"You guessed the number {self.target_number} in {self.attempts} attempts.\nYour final score is: {self.score}")
            self.reset_game()
        elif guess < self.target_number:
            messagebox.showinfo("Hint", "Your guess is too low.")
            self.score -= 10
        else:
            messagebox.showinfo("Hint", "Your guess is too high.")
            self.score -= 10
        
        if self.attempts >= self.max_attempts:
            messagebox.showinfo("Game Over", f"Sorry, you've reached the maximum number of attempts. The target number was {self.target_number}.\nYour final score is: {self.score}")
            self.reset_game()

    def reset_game(self):
        self.target_number = random.randint(1, 100)
        self.attempts = 0
        self.score = 100
        self.entry.delete(0, "end")

if __name__ == "__main__":
    root = tk.Tk()
    game = GuessNumberGame(root)
    root.mainloop()
