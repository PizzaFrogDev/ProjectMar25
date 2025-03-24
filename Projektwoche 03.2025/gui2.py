import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def say_hi():
    print("hi there")

root = tk.Tk()
root.title("Das ist der Titel")
root.geometry("600x400")

button1 = tk.Button(root, text="Hi", command=say_hi)
button1.pack()

quit_button = tk.Button(root, text="Quit", command=root.quit)
quit_button.pack()

Image = Image.open("Bild/MeatboyHD.webp")
Image = Image.resize((600, 400))
Bild = ImageTk.PhotoImage(Image)

label1 = ttk.Label(root, text="Polska", image=Bild, compound="bottom", font=("Comic Sans MS", 18))
label1.pack()

for item in label1.keys():
    print(item.lower() , label1[item])


root.mainloop()