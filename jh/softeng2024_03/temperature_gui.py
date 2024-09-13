import tkinter as tk
from tkinter import messagebox

from main import print_hi


# 소수 판별 함수
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

# GUI 함수
def check_prime():
    try:
        num = int(entry.get())
        if is_prime(num):
            result = f"{num}은(는) 소수입니다."
        else:
            result = f"{num}은(는) 소수가 아닙니다."
        messagebox.showinfo("결과", result)
    except ValueError:
        messagebox.showerror("입력 오류", "유효한 숫자를 입력하세요.")

# Tkinter 윈도우 설정
root = tk.Tk()
root.title("소수 판별기")

# 레이아웃 설정
tk.Label(root, text="숫자를 입력하세요:").pack(pady=10)
entry = tk.Entry(root)
entry.pack(pady=5)
check_button = tk.Button(root, text="소수 판별", command=check_prime)
check_button.pack(pady=20)

# GUI 실행
root.mainloop()
