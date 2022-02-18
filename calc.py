import tkinter as tk
from functools import partial

class Calc:
    def __init__(self) -> None:
        self.window = tk.Tk()
        
        self.btnArr = [tk.Button(self.window, text = x, command = partial(self.event, str(x))) for x in range(10)]
        self.btnArr.append(tk.Button(self.window, text = "+", command = lambda: self.event("+")))
        self.btnArr.append(tk.Button(self.window, text = "-", command = lambda: self.event("-")))
        self.btnArr.append(tk.Button(self.window, text = "=", command = lambda: self.event("=")))
        self.btnArr.append(tk.Button(self.window, text = "C", command = self.clear))
        
        self.entry = tk.Entry(self.window, text = "", justify= "right")
        self.entry.grid(row = 0, column = 0, columnspan = 4, sticky="wens")

    def clear(self):
        self.entry.delete(0, tk.END)
    def setButtonPos(self):
        index = 0
        for r in range(3):
            for c in range(4):
                self.btnArr[index].grid(column = c, row = 1 + r, sticky = "wens")
                index +=1
        self.btnArr[-2].grid(column = 4, row = 2, sticky = "ns", rowspan = 2)
        self.btnArr[-1].grid(column = 4, row = 0, sticky = "ns", rowspan = 2)

    def event(self, operand):
        if operand != "=":
            self.entry.insert(tk.END, operand)
        else:
            equation = self.entry.get()
            self.entry.delete(0, tk.END)
            self.entry.insert(0, eval(equation))

    def main(self):
        self.setButtonPos()
        self.window.mainloop()


if __name__ == '__main__':
    window = Calc().main()