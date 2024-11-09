import tkinter as tk
import random

def play_game():
    user_choice = int(user_entry.get())
    if user_choice >= 3 or user_choice < 0:
        result_label.config(text="You entered invalid number, You lose!")
    else:
        computer_choice = random.randint(0, 2)    
        computer_label.config(text=f"Computer Chose: {computer_choice}")
        if computer_choice == user_choice:
            result_label.config(text="It's a draw!")
        elif computer_choice == 0 and user_choice == 2:
            result_label.config(text="You lose!")
        elif user_choice == 0 and computer_choice == 2:
            result_label.config(text="You win!")
        elif computer_choice > user_choice:
            result_label.config(text="You lose!")
        elif user_choice > computer_choice:
            result_label.config(text="You win!")

root = tk.Tk()
root.title("Rock, Paper, Scissors")
root.geometry("400x250")  # increased size

user_label = tk.Label(root, text="Enter your choice: Type 0 for Rock, 1 for Paper, 2 for Scissors.", font=("Arial", 14), fg="white", bg="blue")  # changed font, text color, and background color
user_label.pack(pady=10)  # added padding

user_entry = tk.Entry(root, width=20, font=("Arial", 14))  # increased width and font size
user_entry.pack(pady=10)

play_button = tk.Button(root, text="Play", command=play_game, font=("Arial", 14), bg="green", fg="white")  # changed button color and font
play_button.pack(pady=10)

computer_label = tk.Label(root, text="", font=("Arial", 14), fg="white", bg="blue")  # changed font, text color, and background color
computer_label.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14), fg="white", bg="blue")  # changed font, text color, and background color
result_label.pack(pady=10)

root.mainloop()