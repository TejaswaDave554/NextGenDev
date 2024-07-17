import tkinter as tk
from gui import RockPaperScissorsGame

if __name__ == '__main__':
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()
