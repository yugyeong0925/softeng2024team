import tkinter as tk
from tkinter import messagebox



def is_even(a):
    return a % 2 == 0

def calculate_even_sum():
    try:
        n = int(number_entry.get())
        if n < 1:
            raise ValueError("0보다 큰 수를 입력해 주세요.")
        
        total = sum(i for i in range(1, n + 1) if is_even(i))
        result_var.set(f"1부터 {n}까지 짝수의 합은 {total}입니다.")
    
    except ValueError as ve:
        messagebox.showerror("Invalid Input", str(ve))

root = tk.Tk()
root.title("짝수 합 구하기")


tk.Label(root, text="짝수의 합을 구할 범위의 마지막 숫자를 입력하세요:").pack(pady=10)

number_entry = tk.Entry(root)
number_entry.pack(pady=5)

calculate_button = tk.Button(root, text="계산", command=calculate_even_sum)
calculate_button.pack(pady=10)

result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var)
result_label.pack(pady=10)


root.mainloop()
