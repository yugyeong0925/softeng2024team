import tkinter as tk

# 버튼 클릭시 실행될 함수
def is_even():
    a = int(ent_number.get())
    if a % 2 == 0:
        result["text"] = f"{a}는 짝수입니다."
    else:
        result["text"] = f"{a}는 홀수입니다."

# 그냥 써
window = tk.Tk()
window.title("odd_even")
window.resizable(width=True, height=True)

# 프레임 만들기 -> 창 배경..?
frm_entry = tk.Frame(master=window, padx=10, pady=10)
frm_entry.grid(row=0, column=0)

# entry -> 입력할 수 있는 창 | Label -> 글(입력 못함)
ent_number = tk.Entry(master=frm_entry, width=10)
lbl_number = tk.Label(master=frm_entry, text="홀수인지 짝수인지 구별할 숫자를 입력하세요.")
result = tk.Label(master=frm_entry)
#command는 버튼 클릭시 함수 실행
button = tk.Button(master=frm_entry, text="입력", command=is_even)

#grid는 창 요소(entry 등) 위치 지정
ent_number.grid(row=0, column=1, padx=10, pady=5)
lbl_number.grid(row=0, column=0, padx=10, pady=5)
result.grid(row=0, column=2, padx=10, pady=5)
button.grid(row=0, column=3, padx=10, pady=5)

window.mainloop()
