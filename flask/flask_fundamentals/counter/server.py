from flask import Flask, render_template, request, session, redirect
app = Flask(__name__)
app.secret_key = "wheresTheChapstick" # this can be any string // also very essential for SESSION.

#start the logic below
@app.route('/')
def root():
    if 'count' in session:
        print('count exists!')
        session['count'] += 1
    else:
        print('count does not exit')
        session['count']=1
    return render_template("counter.html") # red thing is used for the front end

@app.route('/destroy_session', methods=['POST'])
def dest():
    session.clear() # takes our dictionary and returns a blank dictionary
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)