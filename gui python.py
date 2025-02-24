import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Basic Calculator")
        self.root.geometry("300x400")

        self.result_var = tk.StringVar()

        # Entry field for the expression
        entry = tk.Entry(root, textvariable=self.result_var, font=("Arial", 18), bd=10, insertwidth=2, width=14, borderwidth=4)
        entry.grid(row=0, column=0, columnspan=4)

        # Buttons layout
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
            ('C', 5, 0)
        ]

        for (text, row, col) in buttons:
            button = tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 14), command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col)

    def on_button_click(self, char):
        if char == 'C':
            self.result_var.set("")
        elif char == '=':
            try:
                result = str(eval(self.result_var.get()))
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        else:
            current_text = self.result_var.get()
            self.result_var.set(current_text + char)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
