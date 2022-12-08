# Interesting Things
#### Video Demo:  https://www.youtube.com/watch?v=0P6-CDyuoaQ
#### Description:
‘Interesting Things’ is a Flask-based web application made as a submission for CS50x’s final project. It is a notes app hybrid with inspiration in the form of activities, questions, jokes, quotes and more. The website is responsive on both mobile devices and computers.

The main page of the website has three sections- For You, Saved and Explore.

The first section, For You, consists of the ‘inspiration’ I previously talked about. The components of this section are shown in the form of cards in a flexbox layout. If a user finds anything interesting in this section, they can click on the little pencil button shown at the top right corner of each card to edit the component and save it to their collection.

Once the user saves it, they are redirected to the second section, Saved, where the user’s saved notes can be viewed. The saved notes are shown in a card flexbox layout, similar to the ones in For You section. But, in these cards, there is a little delete button present next to the edit button on the top right corner. 
Above the user’s saved notes, there is a menu-bar like component. It consists of a ‘+’ button for adding notes, a search bar for searching notes, and a ‘⚙' button to open the settings.

On clicking the add note button, a modal opens up with spaces to fill in the note’s title and content. The user can ‘Save Changes’ or ‘Close’ the modal.
To search their notes, the user only needs to input the search term and the integrated javascript will show the search results as they type in the query.
The settings page only has a logout option for now, but I’m going to add options for the user to edit their credentials, add a display name and profile picture, and enable dark mode.

There isn’t anything in the Explore section for now, since my exams start soon, the deadline for this project is approaching, and I’m fresh out of ideas of things to add there. Maybe in the near future, I’ll put something nice there.

When the user is not logged in, a welcome page displays. It has the application banner, a tiny paragraph about the app and CTA, forms for both sign up and log in, and a footer with copyright, name, my email, and the project’s source code on Github.

I didn’t make a proper menu bar for my website because I don’t have a good logo yet, don’t want to make an ‘about’ page (my app’s pretty simple) and already have a banner with the application’s name displaying across all pages.

As I hadn’t made a menu bar, I got confused as to where I should place the search bar for notes and the settings button. Which is why I made the menu-bar like component on the Saved page.

Now, about the backend.

The application is mainly saved in the app.py file, along with a function or two in the helpers.py file. I am using a sqlite3 database with the CS50 library to store the user’s data.

The application loads the components on the For You page by collecting them from various APIs. To make the API calls take less time, I used the asyncio library with aiohttp to make requests. The APIs that I am using in my application are- http://www.boredapi.com/api/activity/, https://api.adviceslip.com/advice, https://api.quotable.io/random, https://official-joke-api.appspot.com/random_joke, https://random-words-api.vercel.app/word,
https://uselessfacts.jsph.pl/random.json?language=en and https://catfact.ninja/fact .

Using the APIs with async has prevented me from hosting the application on a proper server online, but whenever time allows, I shall get to work on making this web application available for use.

Possible features that I could add to my application are- option to upload audios, videos and images in the note, toggle dark mode, improve design with better backgrounds and clipart, add a proper menubar and footer, make a logo and make an about page and contact page.

This was CS50x!
