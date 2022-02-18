import tkinter as tk
from re import findall

class Calc:
    def __init__(self) -> None:
        self.window = tk.Tk()

        self.btnArr = [tk.Button(self.window, text = str(x), command = lambda: self.event(str(x))) for x in range(10)]
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
        self.btnArr[-2].grid(column = 4, row = 0, sticky = "wens", rowspan = 1)
        self.btnArr[-1].grid(column = 4, row = 1, sticky = "wens", rowspan = 2)
    
    def __calc__(self, operation):
        operation_counter = [i for i, x in enumerate(operation) if x == "+" or x == "-"]
        number = int(operation[0 : operation_counter[0]])
        """while True:
            if(opera)
            elif(operation[operation_counter[i]] == "+"):
                number += int(operation[operation_counter[i] + 1 : operation_counter[i + 1]])
            elif(operation[operation_counter[i]] == "-"):
                number -= int(operation[operation_counter[i] + 1 : operation_counter[i + 1]])"""
        for i in range(len(operation_counter) - 1):
            if(operation[operation_counter[i]] == "+"):
                print(1)
                number += int(operation[operation_counter[i] + 1 : operation_counter[i + 1]])
            elif(operation[operation_counter[i]] == "-"):
                number -= int(operation[operation_counter[i] + 1 : operation_counter[i + 1]])
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, number)

    def event(self, operand):
        if operand != "=":
            self.entry.insert(tk.END, operand)
        else:
            self.__calc__(self.entry.get())

    def main(self):
        self.setButtonPos()
        self.window.mainloop()


if __name__ == '__main__':
    window = Calc().main()