from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)

@app.route("/")
def index():
   return render_template("index.html")

@app.route('/success/<name>')
def success(name):
   return f'Welcome, {name}!'

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      print(f"Received POST user: {user}")
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      print(f"Received GET user: {user}")
      return redirect(url_for('success',name = user))

if __name__ == '__main__':
   app.run(debug = True)