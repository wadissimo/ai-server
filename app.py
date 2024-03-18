from flask import Flask, render_template, request
import sys
import traceback
from palm2_model import Palm2Model
from gpt_model import GptModel
from gemini_model import GeminiModel
from mistral_model import MistralModel

app = Flask(__name__)
app.secret_key="klf§5n2314v55a§sfd3as1$s23fdas$$1%2113231!!"
DEFAULT_MODEL = "gemini"


def choose_model(model, api_key=""):
    if len(model) == 0:
        model = DEFAULT_MODEL
    if "gpt" in model:
        return GptModel(api_key=api_key, model_name=model)
    elif "palm2" in model or "bison" in model:
        return Palm2Model()
    elif "gemini" in model:
        return GeminiModel()
    elif "mistral" in model:
        return MistralModel(model_name=model)

@app.route("/send_message", methods=['POST'])
def send_message():
    print("send_message called")
    data = request.get_json()
    #print(data)
    api_key = ""
    if "api_key" in data:
        api_key = data["api_key"]
    if "model" in data:
        model = choose_model(data["model"], api_key=api_key)
    else:
        model = choose_model(DEFAULT_MODEL, api_key=api_key)

    print("model", model)
    history = data["history"]
    if len(history) > 0:
        response_data = model.call_chat_history(data["message"], history)
    else:
        response_data = model.call_chat(data["message"])
    
    return {"response": response_data}
    
    #return "message received!"


if __name__ == "__main__":
    # usage python app.py host port ssl cert1 cert2
    # e.g. for a server: python app.py 0.0.0.0 5000 ssl cert.pem key.pem
    # e.g. for a local server: python app.py 127.0.0.1 5000

    arg_len = len(sys.argv)
    if arg_len > 1:
        host = sys.argv[1]
    else:
        host = '127.0.0.1'
    if arg_len > 2:
        port = int(sys.argv[2])
    else:
        port = 5000
    ssl = False
    if arg_len > 3:
        if sys.argv[3] == "ssl" and arg_len > 5:
            ssl = True
            cert1 = sys.argv[4]
            cert2 = sys.argv[5]
            
    debug_mode = True
    #model = DEFAULT_MODEL
    #print("model", model.model_name)
    #app.run(debug=True, port=5000, ssl_context=('cert.pem', 'key.pem'))
    #app.run('0.0.0.0',debug=True, port=5000, ssl_context=('cert.pem', 'key.pem'))
    #app.run('localhost',debug=True, port=80, ssl_context=('localhost.crt', 'localhost.key'))
    #app.run('127.0.0.1',debug=True, port=80)
    if ssl:
        app.run(host,debug=debug_mode, port=port, ssl_context=(cert1, cert1))
    else:
        app.run(host,debug=debug_mode, port=port)
    
    model = choose_model(DEFAULT_MODEL)