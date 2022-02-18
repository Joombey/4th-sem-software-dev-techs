import tkinter as tk

class Calc:
    def __init__(self) -> None:
        self.window = tk.Tk()

        self.btnArr = [tk.Button(self.window, text = str(x), command = lambda: self.event(x)) for x in range(10)]
        self.btnArr.append(tk.Button(self.window, text = "+", command = lambda: self.event("+")))
        self.btnArr.append(tk.Button(self.window, text = "-", command = lambda: self.event("-")))
        self.btnArr.append(tk.Button(self.window, text = "=", command = lambda: self.event("=")))
        
        self.entry = tk.Entry(self.window, text = "")
        self.entry.grid(row = 0, columnspan = 4, sticky = 'wens')

    
    def setButtonPos(self):
        index = 0
        for r in range(3):
            for c in range(4):
                self.btnArr[index].grid(column = c, row = 1 + r, sticky = 'wens')
                index +=1
    
    def __calc__(operation):
        operation_counter = list(map(operation.find, ["-", "+"])).sort()
        operation_counter = list(filter(lambda x: x != -1, operation_counter))
        number = operation[0:operation_counter[0] + 1]
        for i in len(operation_counter) - 1:
            if(operation[i] == "+"):
                number += int(operation[operation_counter[i]:: operation_counter[i + 1]])
            else:
                number -= int(operation[operation_counter[i]:: operation_counter[i + 1]])
            

    def event(self, operand):
        if operand != "=":
            self.entry.insert(0, operand)
        else:
            self.calculator.get()
            self.entry.delete(0, tk.END)

    def main(self):
        self.setButtonPos()
        self.window.mainloop()


if __name__ == '__main__':
    window = Calc().main()