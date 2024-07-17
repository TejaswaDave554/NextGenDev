from PIL import Image, ImageTk
from tkinter import messagebox

def resize_image(image_path):
    try:
        img = Image.open(image_path)
        img = img.resize((100, 100), Image.ANTIALIAS)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        messagebox.showerror("Error", f"Error loading image: {image_path}\n{str(e)}")
        raise e
