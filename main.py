from flask import Flask, request, jsonify
from Utils import chat_bot

app = Flask(__name__)


class Data:
    def __init__(self, question, answer=None):
        self.question = question
        self.answer = answer


@app.route("/request", methods=["POST"])
def post_question():
    data = request.get_json()

    # Validate input data (you may need to customize this part)
    if "question" not in data:
        return jsonify({"error": "Missing 'question' parameter"}), 400

    question = data["question"]

    # If you have optional 'answer' parameter
    answer = data.get("answer", None)

    # Create Data object
    data_obj = Data(question, answer)

    # Use the chat_bot function
    response = chat_bot(data_obj)

    return jsonify(response)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
