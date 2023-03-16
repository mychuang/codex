from flask import Flask, jsonify
from flask import url_for
from flask import redirect
from flask import render_template
from flask import request
from flask_cors import CORS
import openai

openai.api_key = "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"

"""
response = openai.Completion.create(
  model="code-davinci-002",
  prompt="\"\"\"\nUtil exposes the following:\nutil.openai() -> authenticates & returns the openai module, which has the following functions:\nopenai.Completion.create(\n    prompt=\"<my prompt>\", # The prompt to start completing from\n    max_tokens=123, # The max number of tokens to generate\n    temperature=1.0 # A measure of randomness\n    echo=True, # Whether to return the prompt in addition to the generated completion\n)\n\"\"\"\nimport util\n\"\"\"\nCreate an OpenAI completion starting from the prompt \"Once upon an AI\", no more than 5 tokens. Does not include the prompt.\n\"\"\"\n",
  temperature=0,
  max_tokens=64,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0,
  stop=["\"\"\""]
)
"""



#Flask 類別 初始化時 傳入的 __name__ 參數，代表當前模組的名稱。是固定用法，以便讓 Flask 知道在哪裡尋找資源。
app = Flask(__name__)

@app.route('/', methods=['GET'])
def get():
    return 'Hello from CodeX!'

@app.route('/', methods=['POST'])
def postInput():
    
    req = request.get_json()
    print(req["req"])

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=req["req"],
        temperature=0,
        max_tokens=3000,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0,
    )
    
    print(response["choices"][0]["text"])
    return jsonify({'res': response["choices"][0]["text"]})


if __name__ == '__main__':
    app.debug = True
    app.run()

    