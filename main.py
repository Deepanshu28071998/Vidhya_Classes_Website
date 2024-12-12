from flask import Flask, render_template, request, jsonify
from Chatbot_2_2 import chatbot_response  # Assuming this is your chatbot logic module

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('Home_page.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        # Ensure the request is JSON
        if not request.is_json:
            return jsonify({'reply': "Invalid request format. Please send JSON."}), 400

        # Extract user message
        user_message = request.json.get('message', '').strip()

        if not user_message:
            return jsonify({'reply': "Please enter a valid message."}), 400

        # Get chatbot response
        bot_reply = chatbot_response(user_message)

        if not bot_reply:
            bot_reply = "I'm sorry, I didn't understand that. Can you please rephrase?"

        return jsonify({'reply': bot_reply})

    except Exception as e:
        # Log the error and send a generic error message
        print(f"Error in /chat: {e}")
        return jsonify({'reply': "An error occurred on the server. Please try again later."}), 500

@app.route("/about")
def about():
    return render_template('About_us.html')

@app.route("/contact")
def contact():
    return render_template('Contact_Us.html')

@app.route("/courses")
def courses():
    return render_template('Courses.html')

@app.route("/gallery")
def gallery():
    return render_template('Gallery.html')

@app.route("/youtube")
def youtube():
    return render_template('Youtube.html')

if __name__ == '__main__':
    app.run(debug=True)