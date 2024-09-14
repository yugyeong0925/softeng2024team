import tkinter as tk

# 변환 함수 정의
def meters_to_feet(meters):
    return meters * 3.28084

def feet_to_meters(feet):
    return feet * 0.3048

# 변환 처리 함수
def convert_length():
    try:
        value = float(entry.get())
        if conversion_type.get() == "Meters to Feet":
            result = meters_to_feet(value)
            result_label.config(text=f"{value:.2f} 미터는 {result:.2f} 피트입니다.")
        else:
            result = feet_to_meters(value)
            result_label.config(text=f"{value:.2f} 피트는 {result:.2f} 미터입니다.")
    except ValueError:
        result_label.config(text="유효한 숫자를 입력하세요.")

# 메인 윈도우
window = tk.Tk()
window.title("길이 변환기")

# 입력
tk.Label(window, text="입력:").pack(padx=10, pady=5)
entry = tk.Entry(window)
entry.pack(padx=10, pady=5)

# 변환 유형 선택
conversion_type = tk.StringVar(value="Meters to Feet")
tk.Radiobutton(window, text="미터 → 피트", variable=conversion_type, value="Meters to Feet").pack(padx=10, pady=5)
tk.Radiobutton(window, text="피트 → 미터", variable=conversion_type, value="Feet to Meters").pack(padx=10, pady=5)

# 변환 버튼
tk.Button(window, text="변환", command=convert_length).pack(padx=10, pady=10)

# 결과 레이블
result_label = tk.Label(window, text="")
result_label.pack(padx=10, pady=5)

#gui 실행
window.mainloop()