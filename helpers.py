from flask import redirect, render_template, request, session
from functools import wraps
import requests

def apology(message, code=400):

    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.
        """
        for old, new in [("-", "--"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code


def login_required(f):
    """
    Decorate routes to require login.
    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function


def bored():
    # Contact API
    try:
        url = f"http://www.boredapi.com/api/activity/"
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException:
        return "Oops, there was an error!"
    # Parse response
    try:
        activity = response.json()
        return activity["activity"]
    except (KeyError, TypeError, ValueError):
        return "Oops, there was an error!"


def getquote():
    # Contact API
    try:
        url = f"https://api.quotable.io/random"
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException:
        return "Oops, there was an error!"
    # Parse response
    try:
        res = response.json()
        quote = res["content"] + '     - ' + res["author"]
        return quote
    except (KeyError, TypeError, ValueError):
        return "Oops, there was an error!"

def getjoke():
    # Contact API
    try:
        url = f"https://icanhazdadjoke.com/"
        response = requests.get(url, headers={"Accept": "application/json"})
        response.raise_for_status()
    except requests.RequestException:
        return "Oops, there was an error!"
    # Parse response
    try:
        res = response.json()
        return res["joke"]
    except (KeyError, TypeError, ValueError):
        return "Oops, there was an error!"

def getword():
    # Contact API
    try:
        url = f"https://random-words-api.vercel.app/word"
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException:
        return "Oops, there was an error!"
    # Parse response
    try:
        res = response.json()[0]
        word = res["word"] + ': ' + res["definition"]
        return word
    except (KeyError, TypeError, ValueError):
        return "Oops, there was an error!"

def getfact():
    # Contact API
    try:
        url = f"https://uselessfacts.jsph.pl/random.json?language=en"
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException:
        return "Oops, there was an error!"
    # Parse response
    try:
        res = response.json()
        return res["text"]
    except (KeyError, TypeError, ValueError):
        return "Oops, there was an error!"

