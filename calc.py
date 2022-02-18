import tkinter as tk

class Calc:
    def __init__(self) -> None:
        window = tk.Tk()

        self.btnArr = [tk.Button(window, text = str(x), command = lambda: self.event(x)) for x in range(10)]
        self.btnArr.append([tk.Button(window, text = "+", command = lambda: self.event("+"))])
        self.btnArr.append([tk.Button(window, text = "-", command = lambda: self.event("-"))])
        self.btnArr.append([tk.Button(window, text = "=", command = lambda: self.event("="))])
        
        self.entry = tk.Entry(window, text = "").grid(row = 0, columnspan = 4, sticky = 'wens')

        self.calculator = []
    def setButtonPos(self):
        for r in range(3):
            for c in range(3):
                self.btnArr[index].grid(column = c, row = 1 + r)
                index +=1
    
    def __calc__(operation):
        pass
    
    def bindButtons(self):
        for button in self.btnArr:
            button.bind()
    
    def event(self, operand):
        if self.operand != "=":
            self.insert(0, self.operand)
        else:
            self.calculator.get()
            self.entry.delete(0, tk.END)

        