from flask import Flask, render_template 
app = Flask(__name__)

@app.route('/')
def helloWolrd():
    return "Hello World!"

@app.route('/dojo')
def dojo():
    return "Dojo!"

# @app.route("/<name>")
# def hello_person(name):
#     print("in hello_person function")
#     print(name)
#     return f"Hi {name}!"

@app.route('/repeat/<x>/<word>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def repeat(word,x):
    print(word,x)
    return render_template("index.html", word = word, x = int(x))




if __name__ == "__main__": 
    app.run(debug=True)