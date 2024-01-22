from flask import Flask, request, jsonify
from Utils import chat_bot

app = Flask(__name__)


@app.route("/request", methods=["POST"])
def post_question():
    try:
        data = request.get_json()
        if "question" not in data:
            return jsonify({"error": "Missing 'question' parameter"}), 400

        question = data["question"]

        # If you have an optional 'answer' parameter
        answer = data.get("answer", None)

        # Use the chat_bot function
        response = chat_bot(question, answer)
    except Exception as e:
        return jsonify(e)
    return jsonify(data_obj)


@app.route("/hello", methods=["GET"])
def hello():
    return "hello"


if __name__ == "__main__":
    app.run()
