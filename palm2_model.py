from model import Model
from vertexai.preview.language_models import TextGenerationModel
import json
from vertexai.preview.generative_models import GenerativeModel, Content, Part

class Palm2Model(Model):

    def __init__(self):
        super().__init__("Palm2")

    

    def call_chat(self, message):
        model = GenerativeModel("chat-bison-32k")
        chat = model.start_chat()
        response = chat.send_message(message)
        #print(chat.history)
        return response.text
    
    def call_chat_history(self, message, history):
        model = GenerativeModel("chat-bison-32k")
        # init chat history
        chat_history = []
        for h in history:
            if h[0] == 'user':
                chat_history.append(Content(role="user", parts=[Part.from_text(h[1])]))
            else:
                chat_history.append(Content(role="model", parts=[Part.from_text(h[1])]))
        #print("chat history", chat_history)
        chat = model.start_chat(history=chat_history)
        response = chat.send_message(message)
        #print(chat.history)
        return response.text
    


    def call_palm2(self, prompt):
        parameters = {
            "temperature": 0.2,
            "max_output_tokens": 256,   
            "top_p": .8,                
            "top_k": 40,                 
        }
        #model = TextGenerationModel.from_pretrained("text-bison@001")
        model = TextGenerationModel.from_pretrained("text-bison")
        response = model.predict(prompt, **parameters)
        return response


