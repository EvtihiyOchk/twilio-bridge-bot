from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)

@app.route("/call", methods=["POST"])
def call():
    response = VoiceResponse()
    response.dial(request.args.get("call_to"))
    return str(response)

if __name__ == "__main__":
    app.run(port=5000)
