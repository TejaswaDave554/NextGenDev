import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
from utils import resize_image

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")
        
        self.choices = ["rock", "paper", "scissors"]
        self.player_choice = None
        self.player_score = 0
        self.computer_score = 0

        self.rock_img = resize_image("images/rock.jpg")
        self.paper_img = resize_image("images/paper.jpg")
        self.scissors_img = resize_image("images/scissors.jpg")

        self.create_widgets()
        
    def create_widgets(self):
        # Create frames for better organization
        top_frame = tk.Frame(self.root)
        top_frame.pack(pady=10)

        middle_frame = tk.Frame(self.root)
        middle_frame.pack(pady=10)

        bottom_frame = tk.Frame(self.root)
        bottom_frame.pack(pady=10)

        # Labels for player and computer choices
        self.player_choice_label = tk.Label(top_frame, text="Your Choice", font=("Helvetica", 14))
        self.player_choice_label.grid(row=0, column=0, padx=20)

        self.computer_choice_label = tk.Label(top_frame, text="Computer Choice", font=("Helvetica", 14))
        self.computer_choice_label.grid(row=0, column=1, padx=20)

        # Result label
        self.result_label = tk.Label(middle_frame, text="", font=("Helvetica", 18))
        self.result_label.grid(row=0, column=0, columnspan=2, pady=10)

        # Score label
        self.score_label = tk.Label(middle_frame, text="Score: You 0 - 0 Computer", font=("Helvetica", 14))
        self.score_label.grid(row=1, column=0, columnspan=2, pady=10)

        # Buttons for player choices
        self.rock_button = tk.Button(bottom_frame, image=self.rock_img, command=lambda: self.select_choice("rock"))
        self.rock_button.grid(row=0, column=0, padx=20)

        self.paper_button = tk.Button(bottom_frame, image=self.paper_img, command=lambda: self.select_choice("paper"))
        self.paper_button.grid(row=0, column=1, padx=20)

        self.scissors_button = tk.Button(bottom_frame, image=self.scissors_img, command=lambda: self.select_choice("scissors"))
        self.scissors_button.grid(row=0, column=2, padx=20)
        
        # Submit and Play Again buttons
        self.submit_button = tk.Button(bottom_frame, text="Submit", command=self.play, state=tk.DISABLED)
        self.submit_button.grid(row=1, column=1, pady=10)

        self.play_again_button = tk.Button(bottom_frame, text="Play Again", command=self.reset_game, state=tk.DISABLED)
        self.play_again_button.grid(row=1, column=2, pady=10)
        
        # Center the frames
        self.root.update()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        frame_width = self.root.winfo_width()
        frame_height = self.root.winfo_height()

        x = (screen_width // 2) - (frame_width // 2)
        y = (screen_height // 2) - (frame_height // 2)
        self.root.geometry(f'+{x}+{y}')

    def select_choice(self, choice):
        self.player_choice = choice
        if choice == "rock":
            self.player_choice_label.config(image=self.rock_img)
        elif choice == "paper":
            self.player_choice_label.config(image=self.paper_img)
        else:
            self.player_choice_label.config(image=self.scissors_img)
        
        self.submit_button.config(state=tk.NORMAL)

    def play(self):
        computer_choice = random.choice(self.choices)
        
        if computer_choice == "rock":
            self.computer_choice_label.config(image=self.rock_img)
        elif computer_choice == "paper":
            self.computer_choice_label.config(image=self.paper_img)
        else:
            self.computer_choice_label.config(image=self.scissors_img)
        
        result = self.determine_winner(self.player_choice, computer_choice)
        if result == "tie":
            self.result_label.config(text="It's a tie!")
        elif result == "win":
            self.result_label.config(text="You win!")
            self.player_score += 1
        else:
            self.result_label.config(text="You lose!")
            self.computer_score += 1
        
        self.score_label.config(text=f"Score: You {self.player_score} - {self.computer_score} Computer")
        self.submit_button.config(state=tk.DISABLED)
        self.play_again_button.config(state=tk.NORMAL)
        
    def determine_winner(self, player, computer):
        if player == computer:
            return "tie"
        elif (player == "rock" and computer == "scissors") or \
             (player == "paper" and computer == "rock") or \
             (player == "scissors" and computer == "paper"):
            return "win"
        else:
            return "lose"
    
    def reset_game(self):
        self.player_choice = None
        self.player_choice_label.config(image='')
        self.computer_choice_label.config(image='')
        self.result_label.config(text="")
        self.submit_button.config(state=tk.DISABLED)
        self.play_again_button.config(state=tk.DISABLED)
