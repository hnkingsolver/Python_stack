from flask import Flask , render_template, request, redirect, session
import random

app=Flask(__name__)
app.secret_key='secret'

@app.route('/')
def homepage():
    if 'message' not in session:
        session["message"]=""
    if 'number' not in session:
        session['number']=random.randrange(1,101)
    if 'box' not in session:
        session['box'] = 'none'
    print(session['number'])
    return render_template("numbers.html", message=session['message'], box=session['box'] )

@app.route('/guess', methods = ['POST'])
def guess():
    guess = int(request.form['number'])
    if guess == session['number']:
        session['message'] = "YOU WIN! :)"
        session['box'] = 'correct'
    if guess > session['number']:
        session['message' ] = 'Too high guess lower!'
        session['box'] = 'wrong'
    elif guess < session['number']:
        session['message'] = 'Too low guess higher!'
        session['box'] = 'wrong'
    return redirect('/')

@app.route('/reset')
def reset():
    session['number']
    session.pop("number")
    session.pop("message")
    return redirect('/')
app.run(debug=True)