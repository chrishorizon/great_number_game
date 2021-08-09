from flask import Flask, render_template, session, redirect, request
import random
app = Flask(__name__)
app.secret_key = "secret lock"

@app.route('/')
def home():
    if 'count' not in session:
        session['count'] = random.randint(1, 100)
    return render_template("index.html")

@app.route('/random', methods=['POST'])
def guess():
    session['random'] = int(request.form['random'])
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)