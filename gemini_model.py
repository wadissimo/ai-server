from model import Model
from vertexai.preview.generative_models import GenerativeModel, Content, Part

import json

class GeminiModel(Model):

    def __init__(self):
        super().__init__("Gemini")

    def call_model(self, prompt):
        # parameters = {
        #     "temperature": 0.2,
        #     "max_output_tokens": 256,   
        #     "top_p": .8,                
        #     "top_k": 40,                 
        # }
        #model = TextGenerationModel.from_pretrained("text-bison@001")
        model = GenerativeModel("gemini-pro")
        response = model.generate_content(prompt)
        return response
    

    def call_chat(self, message):
        model = GenerativeModel("gemini-pro")
        chat = model.start_chat()
        response = chat.send_message(message)
        #print(chat.history)
        return response.text
    
    def call_chat_history(self, message, history):
        model = GenerativeModel("gemini-pro")
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
    