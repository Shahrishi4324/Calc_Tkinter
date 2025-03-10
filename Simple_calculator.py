import tkinter as tk

def create_window():
    window = tk.Tk()
    window.title("Simple Calculator")
    window.geometry("300x400")

    display = tk.Entry(window, width=16, font=("Arial", 24), borderwidth=2, relief="solid")
    display.grid(row=0, column=0, columnspan=4)

    buttons = [
        '7', '8', '9', '/',
        '4', '5', '6', '*',
        '1', '2', '3', '-',
        '0', '.', '=', '+',
        'C'
    ]

    def button_click(value):
        if value == "=":
            try:
                result = eval(display.get())
                display.delete(0, tk.END)
                display.insert(0, str(result))
            except:
                display.delete(0, tk.END)
                display.insert(0, "Error")
        elif value == "C":
            display.delete(0, tk.END)
        else:
            current_text = display.get()
            display.delete(0, tk.END)
            display.insert(0, current_text + value)

    row_val = 1
    col_val = 0
    for button in buttons:
        tk.Button(window, text=button, width=5, height=2, font=("Arial", 18), command=lambda val=button: button_click(val)).grid(row=row_val, column=col_val)
        col_val += 1
        if col_val > 3:
            col_val = 0
            row_val += 1

    window.mainloop()

if __name__ == "__main__":
    create_window()