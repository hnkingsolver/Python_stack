from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def root():
    return render_template("index.html") #GET ROUTE, retrieving information

@app.route('/tell_secret', methods=["POST"]) #POST ROUTE, sending information
def secret():
    print(request.form) 
    return render_template("secret.html", secret=request.form['secret'])

if __name__ == "__main__":
    app.run(debug=True)