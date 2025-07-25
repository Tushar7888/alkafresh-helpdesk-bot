from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import openai
import os

app = Flask(__name__)
openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route("/bot", methods=["POST"])
def bot():
    incoming_msg = request.values.get('Body', '')
    response = MessagingResponse()
    chat_reply = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": incoming_msg}]
    )
    response.message(chat_reply['choices'][0]['message']['content'])
    return str(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
