from flask import Flask, request, render_template
import random

app = Flask(__name__)


def sort_letters(message):
    """A helper method to sort the characters of a string in alphabetical order
    and return the new string."""
    return "".join(sorted(list(message)))


@app.route("/")
def homepage():
    """A homepage with handy links for your convenience."""
    return render_template("home.html")


@app.route("/froyo")
def choose_froyo():
    """Shows a form to collect the user's Fro-Yo order."""
    return render_template("froyo_form.html")


@app.route("/froyo_results")
def show_froyo_results():
    """Shows the user what they ordered from the previous page."""

    context = {
        "users_froyo_flavor": request.args.get("flavor"),
        "users_froyo_toppings": request.args.get("toppings"),
    }
    return render_template("froyo_results.html", **context)


@app.route("/favorites")
def favorites():
    """Shows the user a form to choose their favorite color, animal, and city."""
    return """
    <form action="/favorites_results" method="GET">
        <label>
        What is your favorite color?
        <input type="text" name="color" />
        </label> </br>
        <label>
        What is your favorite animal?
        <input type="text" name="animal" />
        </label> </br>
        <label>
        What is your favorite city?
        <input type="text" name="city" /></br>
        <input type="submit" value="Submit!"/>
        </label>
    </form>

    """


@app.route("/favorites_results")
def favorites_results():
    """Shows the user a nice message using their form results."""
    users_fav_color = request.args.get("color")
    users_fav_animal = request.args.get("animal")
    users_fav_city = request.args.get("city")

    return f"<p>Wow, I didn't know {users_fav_color} {users_fav_animal}s lived in {users_fav_city}!</p>"


@app.route("/secret_message")
def secret_message():
    """Shows the user a form to collect a secret message. Sends the result via
    the POST method to keep it a secret!"""

    return """
        <form action="/message_results" method="POST">
            <label>
                Enter a secret message:
                <input type="text" name="message"/>
            </label></br>

            <input type="submit" value="Submit!"/>
            
        </form>
    """


@app.route("/message_results", methods=["POST"])
def message_results():
    """Shows the user their message, with the letters in sorted order."""
    users_secret_message = request.form.get("message")
    users_secret_message_sorted = sort_letters(users_secret_message)

    return f"Here's your secret message!\n {users_secret_message_sorted}"


@app.route("/calculator")
def calculator():
    """Shows the user a form to enter 2 numbers and an operation."""
    return render_template("calculator_form.html")


@app.route("/calculator_results")
def calculator_results():
    """Shows the user the result of their calculation."""
    operation = request.args.get("operation")
    operand1 = int(request.args.get("operand1"))
    operand2 = int(request.args.get("operand2"))

    if operation == "add":
        result = operand1 + operand2
    elif operation == "subtract":
        result = operand1 - operand2
    elif operation == "multiply":
        result = operand1 * operand2
    elif operation == "divide":
        result = operand1 / operand2

    context = {
        "operation": operation,
        "operand1": operand1,
        "operand2": operand2,
        "result": result,
    }

    return render_template("calculator_results.html", **context)


HOROSCOPE_PERSONALITIES = {
    "aries": "Adventurous and energetic",
    "taurus": "Patient and reliable",
    "gemini": "Adaptable and versatile",
    "cancer": "Emotional and loving",
    "leo": "Generous and warmhearted",
    "virgo": "Modest and shy",
    "libra": "Easygoing and sociable",
    "scorpio": "Determined and forceful",
    "sagittarius": "Intellectual and philosophical",
    "capricorn": "Practical and prudent",
    "aquarius": "Friendly and humanitarian",
    "pisces": "Imaginative and sensitive",
}


@app.route("/horoscope")
def horoscope_form():
    """Shows the user a form to fill out to select their horoscope."""
    return render_template("horoscope_form.html")


@app.route("/horoscope_results")
def horoscope_results():
    """Shows the user the result for their chosen horoscope."""

    # TODO: Get the sign the user entered in the form, based on their birthday
    horoscope_sign = ""

    # TODO: Look up the user's personality in the HOROSCOPE_PERSONALITIES
    # dictionary based on what the user entered
    users_personality = ""

    # TODO: Generate a random number from 1 to 99
    lucky_number = 0

    context = {
        "horoscope_sign": horoscope_sign,
        "personality": users_personality,
        "lucky_number": lucky_number,
    }

    return render_template("horoscope_results.html", **context)


if __name__ == "__main__":
    app.config["ENV"] = "development"
    app.run(debug=True)
