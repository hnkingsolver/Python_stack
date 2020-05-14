from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def root():
    return render_template ('index.html')

@app.route('/the_encounter')
def encouter():
    return render_template('index2.html')

@app.route('/battle')
def battle():
    return render_template('Index3.html')

@app.route('/run')
def run():
    return render_template('run.html')

@app.route('/done')
def done():
    return render_template('done.html')
if __name__ == "__main__":
    app.run(debug=True)