from flask import Flask, render_template, request, jsonify
import nltk
import datetime
import random
import requests

app = Flask(__name__)
nltk.download('punkt')

responses = {
    "greeting": [
        "Hi there! How can I help you today?",
        "Hello! What can I do for you?",
        "Hey! Need any help?"
    ],
    "time": "The current time is {}",
    "date": "Today's date is {}",
    "how_are_you": [
        "I'm doing great, thanks for asking! How about you?",
        "All good here! How are you doing?",
        "I'm fine, thank you! Hope you're doing well."
    ],
    "exit": [
        "Goodbye! Have a great day!",
        "Bye! Take care.",
        "See you soon!"
    ],
    "fallback": "I'm not sure I understand. Can you rephrase?"
}

API_KEY = "f5a698a68b683c6698a7a2bb00ca3e10"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

chat_history = []


def get_time():
    now = datetime.datetime.now()
    formatted = now.strftime("%I:%M %p").lstrip("0")
    if formatted.endswith(":00 AM") or formatted.endswith(":00 PM"):
        formatted = formatted.replace(":00", "")
    return formatted


def get_date():
    today = datetime.date.today()
    return today.strftime("%B %d, %Y")


def get_weather(city="Mumbai"):
    try:
        url = f"{BASE_URL}q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        if data.get("cod") == 200:
            temp = round(data["main"]["temp"])
            weather = data["weather"][0]["description"].capitalize()
            return f"The weather in {city.title()} is {weather} with {temp}°C temperature."
        else:
            return f"Error: {data.get('message', 'Unable to fetch weather')}"
    except Exception as e:
        return f"Sorry, I couldn't fetch the weather. Error: {str(e)}"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "").lower().strip()
    replies = []

    # greeting 
    if user_input in ["hi", "hello", "hey","hii"]:
        replies.append(random.choice(responses["greeting"]))

    
    elif any(q in user_input for q in ["how are you", "how r u", "how u doing"]):
        replies.append(random.choice(responses["how_are_you"]))

    else:
        # time
        if "time" in user_input:
            replies.append(responses["time"].format(get_time()))

        # date
        if "date" in user_input:
            replies.append(responses["date"].format(get_date()))

        # weather
        if "weather" in user_input:
            city = "Mumbai"
            if "in" in user_input:
                city = user_input.split("in", 1)[1].strip()
                if "and" in city:  # in case of "weather in delhi and time"
                    city = city.split("and")[0].strip()
            replies.append(get_weather(city))

        # exit
        if any(word in user_input for word in ["bye", "exit"]):
            replies.append(random.choice(responses["exit"]))

    #if nothing matched
    if not replies:
        replies.append(responses["fallback"])

    bot_reply = " and ".join(replies)

    
    chat_history.append({
        "user": user_input,
        "bot": bot_reply,
        "time": datetime.datetime.now().strftime("%H:%M")
    })

    return jsonify({"reply": bot_reply})


@app.route("/history", methods=["GET"])
def history():
    return jsonify(chat_history)


if __name__ == "__main__":
    app.run(debug=True)
