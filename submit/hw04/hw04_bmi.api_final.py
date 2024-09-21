from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)






@app.route("/")
def bmi():
    html_str = """
    <!DOCTYPE html>
    <html lang="ko">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>BMI 계산기</title>
        <style>
            body {
                font-size: 20px;
                color: #333;
            }
            h1 {
                font-size: 40px;
                color: #2e8b57;
            }
            h2 {
                font-size: 40px;
                color: #ff4500;
            }
            label {
                font-size: 25px;
                color: #4682b4;
                display: block;
                margin: 10px 0;
            }
            input {
                font-size: 20px;
                padding: 5px;
                width: 50%;
                margin-bottom: 15px;
            }
            button {
                font-size: 25px;
                background-color: #4caf50;
                color: white;
                padding: 10px 15px;
                margin-top: 10px;

            }
        </style>
    </head>
    <body>
        <h1>BMI 계산기</h1>
        <label>체중 (kg): <input type="number" id="weight" required></label>
        <label>신장 (m): <input type="number" step="0.01" id="height" required></label>
        <button id="calculate">계산하기</button>
        <h2 id="result"></h2>

        <script>
            document.getElementById('calculate').addEventListener('click', function() {
                const weight = parseFloat(document.getElementById('weight').value);
                const height = parseFloat(document.getElementById('height').value);

                if (weight > 0 && height > 0) {
                    const bmi = weight / (height * height);
                    let category;

                    if (bmi < 18.5) category = '저체중';
                    else if (bmi < 24.9) category = '정상 체중';
                    else if (bmi < 29.9) category = '과체중';
                    else category = '비만';

                    document.getElementById('result').innerText = `BMI: ${bmi.toFixed(2)} (${category})`;
                } else {
                    document.getElementById('result').innerText = '체중과 신장은 0보다 커야 합니다.';
                }
            });
        </script>
    </body>
    </html>

        """
    return html_str





app.run(debug=True)
