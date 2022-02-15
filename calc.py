import tkinter as tk
from tkinter.tix import COLUMN

class Calc:
    def __init__(self, Label) -> None:
        self.btnArr = [tk.Button(text = str(x), command = self.show) for x in range(10)]
        self.btnArr.append([tk.Button(text = "+")])
        self.btnArr.append([tk.Button(text = "-")])
        self.btnArr.append([tk.Button(text = "=")])
        self.Label = tk.Label(text = "0").grid(row = 0, column = 1)
    LAYOUT = [[x for x in range(4)] for i in range(3)]
    def _setButtonPos_(self):
        for r in range(3):
            for c in range(3):
                self.btnArr[index].grid(column = c, row = 1 + r)
                index +=1
    
    def _setLabelPos_(self):
        self.Label.grid(row = 0, COLUMN = 4)