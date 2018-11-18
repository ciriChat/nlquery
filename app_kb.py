from nlquery.nlquery import NLQueryEngine
from flask import Flask
from flask import request, jsonify
from json import dumps

app = Flask(__name__)

engine = NLQueryEngine('localhost', 9000)

@app.route("/", methods=['GET'])
def get_answer():
    question = request.args.get("question")
    answer = engine.query(str(question), format_='plain')

    return dumps(answer, ensure_ascii=False)


@app.route("/", methods=['POST'])
def answer_post():
    question = request.form.get('question')

    if not question:
        question = request.json.get('question')

    answer = engine.query(str(question), format_='plain')
    return dumps(answer, ensure_ascii=False)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8081)
