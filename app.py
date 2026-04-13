from flask import Flask, render_template, request, redirect, url_for
from cs50 import SQL

app = Flask(__name__)

# Connect to the database
db = SQL("sqlite:///birthdays.db")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        month = request.form.get("month")
        day = request.form.get("day")
        db.execute("INSERT INTO birthdays (name, month, day) VALUES(?, ?, ?)", name, month, day)
        return redirect(url_for("index"))

    # TODO: Query all birthdays from the database
    birthdays = db.execute("SELECT * FROM birthdays")
    # TODO: Pass the birthdays list to the template
    return render_template("index.html",birthdays = birthdays)

if __name__ == "__main__":
    app.run(debug=True)
