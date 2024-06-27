from flask import Flask, jsonify, render_template,request
import os
from gpt import gpt

def html_value():
    return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello World API</title>
</head>
<body>
    <h1>Hello World API</h1>
    <button onclick="fetchHello()">kaetemita</button>
    <p id="result"></p>


    <script>
    function fetchHello() {
        fetch('/api/hello')
            .then(response => response.json())
            .then(data => {
                document.getElementById('result').textContent = data.message;
            })
            .catch(error => console.error('Error:', error));
    }
    </script>
</body>
</html>"""

app = Flask(__name__)

# プログラムがアクセスする用のルート
@app.route('/api/chat', methods=['POST'])
def chat_api():
    print(request.json)
    question = request.json['question']
    # ここで実際のチャットボットロジックを実装します
    # 今回はシンプルなエコーレスポンスを返します
    gpt_response = gpt(question=question)
    return jsonify({"response": gpt_response})

@app.route('/api/hello', methods=['GET'])
def hello_api():
    return jsonify({"message": "Hello, みなさんこんにちは"})
# TODO: 
# HTTPメソッドのGET/POSTとは何かを知る
# GETとPOSTの実装方法をQiitaの記事やAIを利用して知って、実装してみる


# 人がアクセスするためのルート
@app.route('/')
def index():
    # return render_template('index.html')
    
    return html_value()

@app.route('/chat')
def chat():
    # HTMLファイルを読み込む
    html_path = os.path.join(app.root_path, 'templates', 'chat.html')
    with open(html_path, 'r', encoding='utf-8') as file:
        html_content = file.read()
    return html_content

@app.route('/a')
def a():
    return render_template('chat.html')
    
if __name__ == '__main__':
    app.run(debug=True)

