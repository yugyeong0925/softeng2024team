# from flask import Flask, request
# from markupsafe import escape



# app = Flask(__name__)



# @app.route("/")
# def gugudan():
#     html_str = """
#     <!DOCTYPE html>
#     <html lang="kr">
#     <head>
#     <meta charset="UTF-8">
#     <script
#     src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
#     <title>Flask Home Page</title>
#     </head>
#     <body>
#     <h2>구구단 출력하기</h2>
#     <form id="form_id" action="javascript:post_query()">
#     <input type="text" name="dan" value="7">
#     <button type="submit">출력</button>
#     </form>
#     <div id="results"></div>
#     </body>
#     </html>

#     """
#     return html_str


# app.run(debug=True)





from flask import Flask, request

app = Flask(__name__)

@app.route("/dan/")
def gugudan_arg_html():
    dan = request.args.get("dan", "2")  #기본값
    html_str = ""
    for i in range(1, 10):
        html_str += f"{dan} X {i} = <strong>{int(dan)*i}</strong><br>"
    return html_str

@app.route("/")
def gugudan():
    html_str = """
    <!DOCTYPE html>
    <html lang="kr">
    <head>
    <meta charset="UTF-8">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
    <title>Flask Home Page</title>
    <script>
    function post_query() {
        var dan = $("input[name='dan']").val();
        $.get("/dan/", { dan: dan }, function(data) {
            $("#results").html(data);
        });
    }
    </script>
    </head>
    <body>
    <h2>구구단 출력하기</h2>
    <form id="form_id" action="javascript:post_query()">
    <input type="text" name="dan" value="7">
    <button type="submit">출력</button>
    </form>
    <div id="results"></div>
    </body>
    </html>
    """
    return html_str

if __name__ == "__main__":
    app.run(debug=True)
