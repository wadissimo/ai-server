from model import Model

import json
from openai import OpenAI

class GptModel(Model):

    def __init__(self, api_key, model_name="gpt-3.5-turbo"):
        
        #self.key_path = key_path
        #self.key = 
        self.model_name=model_name
        
        self.client = OpenAI(
           api_key=api_key
        )
        super().__init__(model_name)


    def get_key(self, key_path):
        with open(key_path, 'r') as f:
            key = f.readline()
            return key


    def call_chat(self, message):
        completion = self.client.chat.completions.create(model=self.model_name, messages=[{"role": "user", "content": message}])
        response_text = completion.choices[0].message.content #response['choices'][0]['message']['content']
        return response_text
    

    def call_chat_history(self, message, history):
        chat_history = []
        for h in history:
            if h[0] == 'user':
                chat_history.append({"role": "user", "content": h[1]})
            else:
                chat_history.append({"role": "assistant", "content": h[1]})
        chat_history.append({"role": "user", "content": message})
        completion = self.client.chat.completions.create(model=self.model_name, messages=chat_history)
        response_text = completion.choices[0].message.content #response['choices'][0]['message']['content']
        return response_text

