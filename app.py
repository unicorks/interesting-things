import re
import datetime
import asyncio
import aiohttp

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, jsonify
from flask_session.__init__ import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required

# Configure app
app = Flask(__name__)
# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True
# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response
# Configure session to use filesystem
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
# Configure SQLite database
db = SQL("sqlite:///interesting.db")

@app.route('/')
@login_required
def index():
    api_calls = [f"http://www.boredapi.com/api/activity/", f"https://api.adviceslip.com/advice",
                 f"https://api.quotable.io/random",
                 f"https://official-joke-api.appspot.com/random_joke", f"https://random-words-api.vercel.app/word",
                 f"https://uselessfacts.jsph.pl/random.json?language=en",
                 f"https://catfact.ninja/fact"]
    res = []
    async def main():
        async with aiohttp.ClientSession() as session:
            tasks = []
            for api_call in api_calls:
                task = asyncio.ensure_future(session.get(api_call))
                tasks.append(task)

            responses = await asyncio.gather(*tasks)
            for response in responses:
                res.append(await response.json(content_type=None))

    asyncio.run(main())

    # get 'for you' stuff
    question = db.execute("SELECT question FROM questions ORDER BY RANDOM() LIMIT 1 ")[0]['question']
    activity = res[0]["activity"]
    adv = res[1]["slip"]["advice"]
    quote = res[2]["content"] + '     - ' + res[2]["author"]
    joke = res[3]["setup"] + " " + res[3]["punchline"]
    word = res[4][0]["word"] + ': ' + res[4][0]["definition"]
    fact = res[5]["text"]
    cat = res[6]["fact"]

    for_you = [
        {"type": "Bored? Do this!", "content": activity},
        {"type": "A piece of advice", "content": adv},
        {"type": "Question", "content": question},
        {"type": "Joke", "content": joke},
        {"type": "Quote", "content": quote},
        {"type": "Word", "content": word},
        {"type": "Fun Fact", "content": fact},
        {"type": "Cat Fact", "content": cat},
    ]
    return render_template('index.html', for_you=for_you)


@app.route('/saved')
@login_required
def saved():
    """ SHOW NOTES TAKEN BY USER """
    user_id = session["user_id"]
    data = db.execute("SELECT * FROM notes WHERE id = ?", user_id)
    data.reverse()  # for arranging notes by latest time
    return render_template('saved.html', data=data)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""
    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("You must provide a username!", 403)
        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("You must provide a password!", 403)
        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))
        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("Your username or password were invalid!", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]
        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("welcome.html")



@app.route("/register", methods=["POST"])
def register():
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if not request.form.get("username"):
        return apology("You must provide a username!", 400)
    elif not request.form.get("password"):
        return apology("You must provide a password!", 400)
    elif not request.form.get("email") or not (re.fullmatch(regex, request.form.get("email"))):
        return apology("You must provide a valid email", 400)
    x = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))
    if x:
        return apology("That username is already taken!", 400)
    db.execute("INSERT INTO users (username, hash, email) VALUES (?, ?, ?)", request.form.get("username"),
               generate_password_hash(request.form.get("password")), request.form.get("email"))
    return redirect("/")


@app.route("/addnote", methods=["POST"])
@login_required
def addnote():
    user_id = session["user_id"]
    title = request.form.get("title")
    note = request.form.get("note-content")
    note_id = request.form.get('savenote')
    print(note_id)
    if note_id:
        db.execute("DELETE FROM notes WHERE id= ? AND note_id= ?", user_id, note_id)
    if not title and not note:
        return apology("You must write a note!")
    db.execute("INSERT INTO notes (id, title, note, time) VALUES (?,?,?,?)", user_id, title, note,
               str(datetime.datetime.now().replace(microsecond=0)))
    return redirect("/saved")


@app.route("/deletenote", methods=['POST'])
@login_required
def editnote():
    user_id = session["user_id"]
    note_id = request.form.get('delete')
    db.execute("DELETE FROM notes WHERE id= ? AND note_id= ?", user_id, note_id)
    return redirect("/saved")


@app.route("/search")
def search():
    user_id = session["user_id"]
    query = "%" + request.args.get("q") + "%"
    results = db.execute("SELECT * FROM notes WHERE id= ? AND (title LIKE ? OR note LIKE ?)", user_id, query, query)
    return jsonify(results)

@app.route("/settings")
def settings():
    return render_template("settings.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)

if __name__ == '__main__':
    app.run()
