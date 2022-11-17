from flask import redirect, render_template, request, session
from functools import wraps
import requests
import aiohttp
import asyncio

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


api_calls = [f"http://www.boredapi.com/api/activity/", f"https://api.adviceslip.com/advice", f"https://api.quotable.io/random",
             f"https://official-joke-api.appspot.com/random_joke", f"https://random-words-api.vercel.app/word", f"https://uselessfacts.jsph.pl/random.json?language=en",
             f"https://catfact.ninja/fact", f"https://www.dogfactsapi.ducnguyen.dev/api/v1/facts/?number=1"]

def get_tasks(session):
    tasks = []
    for api_call in api_calls:
        tasks.append(session.get(api_call))
        return tasks


res = []
async def get_calls():
    async with aiohttp.ClientSession() as session:
        tasks = get_tasks(session)
        responses = await asyncio.gather(*tasks)
        for response in responses:
            res.append(await response.json())