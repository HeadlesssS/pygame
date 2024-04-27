import tkinter as tk

def print_line():
    print("lu thichis")

root= tk.Tk()
button = tk.Button(root,text="Thich",command=print_line)
button.pack()

root.mainloop()