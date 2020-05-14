from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def frontpage():
    return render_template('index.html')


@app.route('/result', methods=["POST"])
def result():
    return render_template('result.html', txtName=request.form['txtName'], txtEmail=request.form['txtEmail'], txtLocation=request.form['txtLocation'], txtMsg=request.form['txtMsg'])

if __name__ == "__main__":
    app.run(debug=True)
