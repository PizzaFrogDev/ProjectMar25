import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def delete_input():
    print("Eingabe gelöscht")
    print(entry1.get())
    entry1.delete(0, tk.END)

def print_input():
    print("Ausgabe:")    
    print(entry1.get())

root = tk.Tk()
root.title("Das ist der Titel")
root.geometry("600x400")

entry1 = tk.Entry(root, background="yellow", width=30, font=("Comic Sans MS", 18))
entry1.pack()

button1 = ttk.Button(root, text="Ausgeben", command=print_input)
button1.pack()

button2 = ttk.Button(root, text="Löschen", command=delete_input)
button2.pack()

root.mainloop()