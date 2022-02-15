import tkinter as tk

def show(x):
    Label = tk.Label(text = x)
    pass
root = tk.Tk()

table = [[x for x in range(3)] for i in range(3)]

Label = tk.Label(text = "0").grid(row = 0, column = 1)
btnArr = [tk.Button(text = str(x), command = show(x)) for x in range(10)]
btnArr.append(tk.Button(text = "="))
index = 0
for r in range(3):
    for c in range(3):
        btnArr[index].grid(column = c, row = 1 + r)
        index +=1
root.mainloop()