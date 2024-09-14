

import tkinter as tk
from tkinter import messagebox

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def calculate_factorial():
    try:
        number = int(number_entry.get())
        if number < 0:
            raise ValueError("0보다 큰 수를 입력해 주세요.")
        result = factorial(number)
        result_var.set(f"{number}!(팩토리얼) 값은 {result}입니다.")
    except ValueError as ve:
        messagebox.showerror("Invalid Input", str(ve))

root = tk.Tk()
root.title("팩토리얼 값 구하기")

tk.Label(root, text="팩토리얼 값을 구할 숫자를 입력하세요.").pack(pady=10)

number_entry = tk.Entry(root)
number_entry.pack(pady=5)

calculate_button = tk.Button(root, text="입력", command=calculate_factorial)
calculate_button.pack(pady=10)

result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var)
result_label.pack(pady=10)

root.mainloop()
