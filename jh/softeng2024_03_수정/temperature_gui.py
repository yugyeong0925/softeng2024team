import tkinter as tk

# 온도 변환 함수 정의
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# 변환 처리 함수
def convert_temperature():
    try:
        value = float(entry.get())
        if conversion_type.get() == "Celsius to Fahrenheit":
            result = celsius_to_fahrenheit(value)
            result_label.config(text=f"{value:.2f} 섭씨는 {result:.2f} 화씨입니다.")
        else:
            result = fahrenheit_to_celsius(value)
            result_label.config(text=f"{value:.2f} 화씨는 {result:.2f} 섭씨입니다.")
    except ValueError:
        result_label.config(text="유효한 숫자를 입력하세요.")

# 메인 윈도우
window = tk.Tk()
window.title("온도 변환기")

# 입력
tk.Label(window, text="입력:").grid(row=0, column=0, padx=10, pady=5)
entry = tk.Entry(window)
entry.grid(row=0, column=1, padx=10, pady=5)

# 변환 유형 선택
conversion_type = tk.StringVar(value="Celsius to Fahrenheit")
tk.Radiobutton(window, text="섭씨 → 화씨", variable=conversion_type, value="Celsius to Fahrenheit").grid(row=1, column=0, columnspan=2, padx=10, pady=5)
tk.Radiobutton(window, text="화씨 → 섭씨", variable=conversion_type, value="Fahrenheit to Celsius").grid(row=2, column=0, columnspan=2, padx=10, pady=5)

# 변환 버튼
tk.Button(window, text="변환", command=convert_temperature).grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# 결과 레이블
result_label = tk.Label(window, text="")
result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

# GUI 실행
window.mainloop()
