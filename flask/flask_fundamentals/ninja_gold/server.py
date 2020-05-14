from flask import Flask, session, redirect, request, render_template
import datetime
import random

app = Flask(__name__)
app.secret_key = 'secretkey'

def formatActivity(action, gold, location):
    timestamp = datetime.datetime.now()
    return '%s %d from the %s! (%s)' % (action, gold, location, timestamp)
    
@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
    if 'activities' not in session:
        session['activities'] = []

    return render_template('index.html', gold=session['gold'], activities=session['activities'])

@app.route('/process_money', methods=['POST'])
def process_money():
    if request.form.get('action') == "farm":
        earned = random.randrange(10, 20)
        session['gold'] += earned
        session['activities'].insert(0, ['earned', formatActivity('Earned', earned, 'farm')])
    
    if request.form.get('action') == "cave":
        earned = random.randrange(5, 10)
        session['gold'] += earned
        session['activities'].insert(0, ['earned', formatActivity('Earned', earned, 'cave')])
    
    if request.form.get('action') == "house":
        earned = random.randrange(2, 5)
        session['gold'] += earned
        session['activities'].insert(0, ['earned', formatActivity('Earned', earned, 'house')])

    if request.form.get('action') == "casino":
        earned = random.randrange(-50, 50)
        session['gold'] += earned
        if earned > 0:
            session['activities'].insert(0, ['earned', formatActivity('Earned', earned, 'casino')])
        else:
            session['activities'].insert(0, ['lost', formatActivity('Lost', -earned, 'casino')])

    
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')

app.run(debug=True)