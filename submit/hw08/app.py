from flask import Flask, render_template
import pandas as pd
import os

app = Flask(__name__)
 
@app.route('/')
@app.route('/index')
def index():
  return render_template('index.html', title='home')
 


@app.route('/blog')
def blog():
   file_path = "./data.csv"
   if not os.path.exists(file_path):
      return "CSV file not found."
   df = pd.read_csv(file_path)
   post_list = []
   for i, row in df.iterrows():
      post_list.append({"title": row['title'], "content": row['content']})
   print(post_list)
   return render_template('blog.html', title="blog_post",posts=post_list)



@app.route('/about_us')
def about():
   return render_template('about_us.html', title='About')



if __name__ == '__main__':
   app.run(debug=True)

