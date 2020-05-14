from flask import Flask, render_template 
app = Flask(__name__)

@app.route('/play')
def index():
    return render_template("playground.html", times=3)

# 7 boxes
@app.route('/play/<times>')
def index_play_x(times):
    return render_template('playground.html', times=int(times))

@app.route('/play/<times>/<color>')
def index_play_color(times,color):
    return render_template('playground.html', times=int(times),color=color)



if __name__ == "__main__": 
    app.run(debug=True)