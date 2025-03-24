import tkinter as tk

root = tk.Tk()
root.title("Das ist der Titel")
root.geometry("600x400")
root.minsize(400, 300)
root.maxsize(800, 600)

label1 = tk.Label(root, text="Polska", bg="white")
label1.pack(side="top", expand=True, fill="both")

label2 = tk.Label(root, text="Gurom", bg="red")
label2.pack(side="top", expand=True, fill="both")

root.mainloop()