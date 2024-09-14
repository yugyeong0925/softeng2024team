import tkinter as tk
from tkinter import messagebox

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def find_primes():
    """Find all prime numbers in the specified range and display them."""
    try:
        lower = int(lower_entry.get())
        upper = int(upper_entry.get())
        if lower > upper:
            raise ValueError("Lower bound must be less than or equal to upper bound.")
        
        primes = [num for num in range(lower, upper + 1) if is_prime(num)]
        result_var.set(', '.join(map(str, primes)))
    
    except ValueError as ve:
        messagebox.showerror("Invalid Input", str(ve))

root = tk.Tk()
root.title("범위 내에서 소수 찾기")

tk.Label(root, text="시작 값:").pack(padx=10, pady=5)
lower_entry = tk.Entry(root)
lower_entry.pack(padx=10, pady=5)

tk.Label(root, text="마지막 값:").pack(padx=10, pady=5)
upper_entry = tk.Entry(root)
upper_entry.pack(padx=10, pady=5)

find_button = tk.Button(root, text="범위 입력", command=find_primes)
find_button.pack(padx=10, pady=10)

result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var)
result_label.pack(padx=10, pady=10)

# Run the application
root.mainloop()
