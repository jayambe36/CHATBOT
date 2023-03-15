from flask import Flask, render_template , request , jsonify

from chat import get_response

app = Flask(__name__)

@app.route("/")
def index_get():
    return render_template("base.html")

@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    
    response = get_response(text)
    message = {"answer":response}
    
    return jsonify(message)

if __name__ == "__main__":
    app.run(debug=True)
    
    
# =============================================





# from flask import Flask, render_template, request, jsonify
# from google.cloud import translate_v2 as translate
# from chat import get_response

# app = Flask(__name__)

# # Initialize the translation client
# translate_client = translate.Client()

# @app.route("/")
# def index_get():
#     return render_template("base.html")

# @app.post("/predict")
# def predict():
#     text = request.get_json().get("message")

#     # Translate the user's message from English to Gujarati
#     translation = translate_client.translate(text, target_language='gu')
#     gujarati_text = translation['translatedText']

#     # Generate the chatbot's response in English
#     english_response = get_response(text)

#     # Translate the chatbot's response from English to Gujarati
#     translation = translate_client.translate(english_response, target_language='gu')
#     gujarati_response = translation['translatedText']

#     # Return the chatbot's response in Gujarati as a JSON object
#     response = {"answer": gujarati_response}
#     return jsonify(response)

# if __name__ == "__main__":
#     app.run(debug=True)