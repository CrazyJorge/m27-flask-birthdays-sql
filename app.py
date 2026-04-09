from flask import Flask, render_template, request, redirect, url_for
from cs50 import SQL

app = Flask(__name__)

# Connect to the database
db = SQL("sqlite:///birthdays.db")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # TODO: Read the form data (name, month, day) from request.form
        # TODO: Insert the new birthday into the database using db.execute
        #       Use: db.execute("INSERT INTO birthdays (name, month, day) VALUES(?, ?, ?)", name, month, day)
        # TODO: Redirect back to "/"
        pass

    # TODO: Query all birthdays from the database
    #       Use: birthdays = db.execute("SELECT * FROM birthdays")
    # TODO: Pass the birthdays list to the template
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
