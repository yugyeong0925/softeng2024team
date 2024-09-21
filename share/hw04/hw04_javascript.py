from flask import Flask, request

app = Flask(__name__)



@app.route("/")
def gugudan():
    html_str = """
    <!DOCTYPE html>
    <html lang="kr">
    <head>
    <meta charset="UTF-8">
    <script
    src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></scr
    ipt>
    </head>
    <body>
    <form id="form_id" action="javascript:post_query()">
    <input type="text" name="dan" value="7">
    <button type="submit">Go</button>
    </form>
    <div id="results"></div>
    <script>
    function post_query() {
    $.ajax({
    type: "GET",
    url: "http://localhost:5000/gugudan",
    data: $("#form_id").serialize(),
    success: update_result,
    dataType: "html"
    });
    }
    function update_result(data) {
    $("#results").html(data);
    }
    </script>
    </body>
    </html>
    """
    return html_str

if __name__ == "__main__":
    app.run(debug=True)
