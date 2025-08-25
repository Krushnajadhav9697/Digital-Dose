# AI-Lite Chatbot

AI-Lite Chatbot is a simple web-based chatbot built with **Flask**, **Python**, and **NLTK**. It can respond to multiple user queries in a single message, such as greetings, time, date, weather information, and casual conversation. The chatbot also stores and displays chat history.

---

## Features

- Responds to greetings like "Hi", "Hello", "Hey".
- Handles questions like "How are you?".
- Provides current **time** and **date**.
- Fetches **weather information** for any city using OpenWeatherMap API.
- Supports **multiple queries in a single message**, e.g., "weather in Delhi and time".
- Stores **chat history** in memory and allows viewing it.
- Fallback response if the input is not recognized.

---

## Technologies Used

- **Python 3**
- **Flask** – Web framework
- **NLTK** – Natural language processing for tokenization
- **Requests** – To fetch weather information from OpenWeatherMap API
- **HTML, CSS, JavaScript** – Frontend

---

## Installation

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd <repository-folder>

   ```

   2.**Create & activate a virtual environment (optional)**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Mac/Linux
   venv\Scripts\activate      # On Windows

   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt

   ```

3. **Run the project**

   ```
   python app.py

   ```
