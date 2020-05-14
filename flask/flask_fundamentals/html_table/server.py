from flask import Flask, render_template # Import Flask to allow us to create our app.
app = Flask(__name__)  # Global variable __name__ tells Flask whether or not we are running the file
                        # directly, or importing it as a module.
print(__name__)         # Just for fun, print __name__ to see what it is
@app.route('/')         # The "@" symbol designates a "decorator" which attaches the following
                        # function to the '/' route. This means that whenever we send a request to
                        # localhost:5000/ we will run the following "hello_world" function.


@app.route("/")
def users():
    users = [
        {'first_name': 'Hannah', 'last_name': 'Kingsolver', 'entry_number': '1'},
        {'first_name': 'Tanner', 'last_name': 'Colley', 'entry_number': '2'},
        {'first_name': 'Spongebob', 'last_name': 'Squarepants', 'entry_number': '3'},
        {'first_name': 'Patrick', 'last_name': 'Star', 'entry_number': '4'}
    ]

    return render_template("htmltable.html", users=users)


if __name__ == "__main__":
    app.run(debug=True)
