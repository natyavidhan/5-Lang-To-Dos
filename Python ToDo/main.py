import tkinter as tk
import json

class App:
    def __init__(self, root):
        root.title("Python To Do List")
        root.geometry("400x400")
        self.root = root

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()