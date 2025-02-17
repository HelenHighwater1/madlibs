"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    "awesome",
    "terrific",
    "fantastic",
    "neato",
    "fantabulous",
    "wowza",
    "oh-so-not-meh",
    "brilliant",
    "ducky",
    "coolio",
    "incredible",
    "wonderful",
    "smashing",
    "lovely",
]


@app.route("/")
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route("/hello")
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route("/greet")
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html", person=player, compliment=compliment)

@app.route("/game")
def show_madlib_form():
    """Get user's response."""
    response = request.args.get("game")
    # print( "request.args:", request.args)
    if response == 'no':
        return render_template('goodbye.html')
    else:
        return render_template('game.html')

@app.route("/madlib")
def show_madlib():
    "Shows the madlib the user created"
    print(request.args)
    person = request.args.get("person")
    noun = request.args.get("noun")
    color = request.args.get("color")
    adjective = request.args.get("adjective")
    hobbies = []
    
    if request.args.get('painter'):
        hobbies.append('painter')
    if request.args.get('baker'):
        hobbies.append('baker')
    if request.args.get('fighter'):
        hobbies.append('fighter')
    if request.args.get('hiker'):
        hobbies.append('hiker')

    return render_template('madlib.html', person=person, noun=noun, color=color, adjective=adjective, hobbies=hobbies)


if __name__ == "__main__":
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0", port=6060)

