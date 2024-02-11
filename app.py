from flask import Flask, render_template, request

import traceback
from palm2_model import Palm2Model
from gpt_model import GptModel
from gemini_model import GeminiModel

app = Flask(__name__)
app.secret_key="klf§5n2314v55a§sfd3as1$s23fdas$$1%2113231!!"


@app.route("/send_message", methods=['POST'])
def send_message():
    print("send_message called")
    data = request.get_json()
    print(data)
    response_data = model.call_chat(data["message"])
    return {"response": response_data}
    
    #return "message received!"


if __name__ == "__main__":
    model = GeminiModel()
    #model = DEFAULT_MODEL
    #print("model", model.model_name)
    #app.run(debug=True, port=5000, ssl_context=('cert.pem', 'key.pem'))
    #app.run('0.0.0.0',debug=True, port=5000, ssl_context=('cert.pem', 'key.pem'))
    #app.run('localhost',debug=True, port=80, ssl_context=('localhost.crt', 'localhost.key'))
    #app.run('127.0.0.1',debug=True, port=80)
    app.run('127.0.0.1',debug=True, port=3000)