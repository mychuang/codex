from flask import Flask, jsonify
from flask import url_for
from flask import redirect
from flask import render_template
from flask import request
from flask_cors import CORS
import openai
import os
from dotenv import load_dotenv

load_dotenv()  # 自動從 .env 載入變數到 os.environ

# 使用變數
openai.api_key = os.getenv("OPENAI_API_KEY")


#Flask 類別 初始化時 傳入的 __name__ 參數，代表當前模組的名稱。是固定用法，以便讓 Flask 知道在哪裡尋找資源。
app = Flask(__name__)

@app.route('/', methods=['GET'])
def get():
    return 'Hello from CodeX!'

@app.route('/', methods=['POST'])
def postInput():
    try:
        req = request.get_json()
        prompt = req.get("req", "")
        if not prompt:
            return jsonify({'error': 'Missing prompt'}), 400

        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0,
            max_tokens=1000,
        )

        result = response.choices[0].message.content.strip()
        return jsonify({'res': result})

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # 必須讓 Render 控制 PORT
    app.run(host="0.0.0.0", port=port)

    