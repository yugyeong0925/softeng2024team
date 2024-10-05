from flask import Flask, render_template
 
app = Flask(__name__)
 
@app.route('/')
@app.route('/index')
def index():
  return render_template('index.html', title='home')
 


@app.route('/blog')
def blog():
   return render_template('blog.html', title='blog')


@app.route('/about_us')
def about():
    return render_template('about_us.html', title='About')



if __name__ == '__main__':
   app.run(debug=True)

