import json

from flask import Flask, request, render_template

from doctor_assistant.web.doctor_assistant import summarize

app = Flask(__name__)


# URL 에 매개변수를 받아 진행하는 방식입니다.
@app.route('/board/<article_idx>')
def board_view(article_idx):
    return article_idx


# 위에 있는것이 Endpoint 역활을 해줍니다.
@app.route('/boards', defaults={'page': '0'})
@app.route('/boards/<page>')
def boards(page):
    return page + "페이지입니다."


# GET 방식
# URL http://127.0.0.1:5003/board?question=anw
@app.route("/board")
def board_list():
    return f"question 변수의 값은 {request.args.get('question')}"


@app.route("/boards", methods=["POST"])
def board_list2():
    post_result = json.loads(request.get_data())

    return f"question 변수의 값은 {post_result}"


@app.route("/dobule", methods=["POST", "GET"])
def dobule():
    if request.method == "GET":
        return "GET 요청 내용은{}".format(request.args.get('question'))
    if request.method == "POST":
        return "POST 요청 내용은{}".format(json.loads(request.get_data()))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    if request.method == 'POST':
        example_format = request.form['example_format']
        symptom = request.form['symptom']

        summary = summarize(symptom=symptom, example_format=example_format)

        return render_template('result.html', summary=summary)


if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
