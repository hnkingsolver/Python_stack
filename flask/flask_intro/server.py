#essential first two lines
from flask import Flask, render_template 
app = Flask(__name__)

@app.route('/')
def root():
    return "I STARTED MY FIRST WEB SERVER"

@app.route('/hello')
def hello():
    return "Hello World!"

#make variables in routes with carrot symbol <>
@app.route('/like/<int:waffle>')
def like(waffle):
    return "I like the number " + str(waffle) + "!"

@app.route('/template')
def temp():
    return render_template("index.html", phrase= 'the phrase!!', characters=["Deku", "Todoroki", "sin"])



#essential last two lines of code
if __name__ == "__main__": 
    app.run(debug=True)