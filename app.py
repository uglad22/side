from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')


@app.route('/letter')
def letter():
   return render_template('letter.html')


@app.route('/about')
def about():
   return render_template('about.html')


if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True)