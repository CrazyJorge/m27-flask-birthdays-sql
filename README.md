# Assignment 4: Birthdays -- SQL

Welcome to the gaiden! We're stepping away from Record of Tasks to learn about databases. You'll build a birthday tracker using SQL.

## Setup

1. Open this repository in GitHub Codespaces. The database is created automatically when the Codespace starts -- you don't need to do anything.
2. Run the app:
   ```
   flask run --debug
   ```
3. Click the link in the terminal to open the app in your browser.

## Background

So far, we've stored data in CSV files. That works, but it has limitations: to find one record you have to read the entire file, deleting a single row is awkward, and there's no way to enforce data types or required fields.

A **database** solves these problems. Instead of reading and writing files yourself, you write **SQL queries** -- short statements that tell the database exactly what you want. The database handles the searching, sorting, and storage.

Your app uses **SQLite**, a lightweight database stored in a single file called `birthdays.db`. This file has already been created (by `init_db.py`) with a table called `birthdays` and 5 sample entries. The table has four columns:

| Column | Type    | Description                          |
|--------|---------|--------------------------------------|
| id     | INTEGER | Unique identifier (assigned automatically) |
| name   | TEXT    | The person's name                    |
| month  | INTEGER | Birth month (1-12)                   |
| day    | INTEGER | Birth day (1-31)                     |

To interact with the database from Python, we use the **CS50 SQL library**. It lets you run SQL queries with a simple `db.execute(...)` call.

## Assignment

Complete the app so that users can view, add, and delete birthdays. Work through these steps in order.

### Step 1: Display birthdays (GET route)

Open `app.py`. In the `index()` function, find the section after the `if` block (the part that handles GET requests). Add code to:

- Query all birthdays from the database:
  ```python
  birthdays = db.execute("SELECT * FROM birthdays")
  ```
- Pass the result to the template:
  ```python
  return render_template("index.html", birthdays=birthdays)
  ```

### Step 2: Uncomment the template loop

Open `templates/index.html`. Find the commented-out Jinja2 loop inside `<tbody>`. Remove the `<!--` and `-->` comment markers so the loop runs.

**Important:** Do this step *after* Step 1. If you uncomment the loop before the route passes `birthdays` to the template, you'll get an error because the variable doesn't exist yet.

### Step 3: Test the display

Run the app. You should see the 5 sample birthdays (Alice, Bob, Charlie, Diana, Edward) displayed in the table.

### Step 4: Add a birthday (POST route)

In `app.py`, find the `if request.method == "POST"` block inside `index()`. Replace `pass` with code to:

- Read the form data:
  ```python
  name = request.form.get("name")
  month = request.form.get("month")
  day = request.form.get("day")
  ```
- Insert the new birthday into the database:
  ```python
  db.execute("INSERT INTO birthdays (name, month, day) VALUES(?, ?, ?)", name, month, day)
  ```
- Redirect back to the home page:
  ```python
  return redirect(url_for("index"))
  ```

### Step 5: Test adding

Run the app. Type a name, month, and day into the form and click Add. The new birthday should appear in the table.

### Step 6: Delete a birthday

In `app.py`, find the `delete()` function. Replace `pass` with code to:

- Get the birthday id from the form:
  ```python
  id = request.form.get("id")
  ```
- Delete that birthday from the database:
  ```python
  db.execute("DELETE FROM birthdays WHERE id = ?", id)
  ```
- Redirect back to the home page:
  ```python
  return redirect(url_for("index"))
  ```

### Step 7: Test deleting

Run the app. Click the Delete button next to any birthday. That row should disappear from the table.

## SQL Reference

Here are the SQL queries you'll use in this assignment. In each one, `db` is the database connection created at the top of `app.py`.

| Operation | Code | Returns |
|-----------|------|---------|
| Read all rows | `db.execute("SELECT * FROM birthdays")` | A list of dictionaries, one per row |
| Insert a row | `db.execute("INSERT INTO birthdays (name, month, day) VALUES(?, ?, ?)", name, month, day)` | The new row's id |
| Delete a row | `db.execute("DELETE FROM birthdays WHERE id = ?", id)` | -- |

**Always use `?` for user input.** Never paste variables directly into the SQL string. The `?` placeholders keep your app safe from SQL injection attacks.

## What to Submit

Push your completed code to this repository.
