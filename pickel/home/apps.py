from django.apps import AppConfig
from flask import Flask, render_template, request, jsonify
import openai

class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'



app = Flask(__name__)
openai.api_key  = "<place your openai_api_key>"

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]
@app.route("/")
def home():    
    return render_template("index.html")
@app.route("/get")
def get_bot_response():    
    userText = request.args.get('msg')  
    response = get_completion(userText)  
    #return str(bot.get_response(userText)) 
    return response
if __name__ == "__main__":


