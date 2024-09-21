from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)






@app.route("/")
def bmi():
    html_str = """
    <!DOCTYPE html>
    <html lang="kr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>BMI 계산기</title>
    </head>
    <body>
        <h1>BMI 계산기</h1>
        <label>체중 (kg): <input type="number" id="weight" required></label><br>
        <label>신장 (cm): <input type="number" id="height" required></label><br>
        <button id="calculate">계산하기</button>
        <h2 id="result"></h2>

        <script>
            document.getElementById('calculate').addEventListener('click', function()
                {const weight = parseFloat(document.getElementById('weight').value);
                const height = parseFloat(document.getElementById('height').value);

                if (weight > 0 &&
                height > 0) {
                    const bmi = weight / ((height * 0.01)**2);
                    let category;

                    if (bmi < 23) category = '비만이 아닙니다.';
                    else if (bmi < 25) category = '비만 전 단계입니다.';
                    else if (bmi < 30) category = '1단계 비만입니다.';
                    else if (bmi < 35) category = '2단계 비만입니다.';
                    else category = '3단계 비만입니다.';

                    document.getElementById('result').innerText = `BMI: ${bmi.toFixed(2)} (${category})`;}
                else {
                    document.getElementById('result').innerText = '체중과 신장은 0보다 커야 합니다.';}
            });
        </script>
    </body>
    </html>

        """
    return html_str





app.run(debug=True)