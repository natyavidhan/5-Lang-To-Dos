import tkinter as tk
import json


class App:
    def __init__(self, root):
        root.title("Python To Do List")
        root.geometry("400x400")
        self.root = root
        self.label = tk.Label(root, text="To Do List",
                              font=("Consolas", 24), anchor="center")
        self.label.place(relx=0.5, rely=0.1, anchor="center")

        self.TaskInput = tk.Entry(root, font=("Consolas", 16))
        self.TaskInput.place(relx=0.05, rely=0.2, relwidth=0.55, relheight=0.1)
        self.TaskInput.focus()
        self.TaskAdd = tk.Button(root, text="Add Task", font=(
            "Consolas", 16), command=self.AddTask)
        self.TaskAdd.place(relx=0.65, rely=0.2, relwidth=0.3, relheight=0.1)
        self.TaskList = tk.Listbox(root, font=(
            "Consolas", 16), selectmode=tk.SINGLE)
        self.TaskList.place(relx=0.05, rely=0.4, relwidth=0.85, relheight=0.4)
        self.Scrollbar = tk.Scrollbar(
            root, orient="vertical", command=self.TaskList.yview)
        self.Scrollbar.place(relx=0.90, rely=0.4, relwidth=0.05, relheight=0.4)
        self.TaskList.configure(yscrollcommand=self.Scrollbar.set)
        self.DeleteButton = tk.Button(root, text="Delete Task", font=(
            "Consolas", 16), command=self.DeleteTask)
        self.DeleteButton.place(
            relx=0.5, rely=0.9, relwidth=0.5, relheight=0.1, anchor="center")
        self.load()

    def AddTask(self):
        task = self.TaskInput.get()
        self.TaskInput.delete(0, tk.END)
        fileData = json.load(open("data.json", "r"))
        fileData.append(task)
        json.dump(fileData, open("data.json", "w"))
        self.load()

    def DeleteTask(self):
        if index := self.TaskList.curselection():
            fileData = json.load(open("data.json", "r"))
            fileData.pop(index[0])
            json.dump(fileData, open("data.json", "w"))
        self.load()

    def load(self):
        self.TaskList.delete(0, tk.END)
        fileData = json.load(open("data.json", "r"))
        for task in fileData:
            self.TaskList.insert(tk.END, task)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
