# CHATBOT




open anaconda prompt

drive c to f

(base) C:\>F:
(base) F:\>dir //work like ls in ubantu in win10 we use dir

(base) F:\anaconda system>conda create -n my_venv python=3.10

(base) F:\anaconda system>conda activate my_venv

(my_venv) F:\anaconda system>pip install Flask torch torchvision nltk

(my_venv) F:\anaconda system\chatbot>pip install nltk

(my_venv) F:\anaconda system\chatbot>python

>>> import nltk
>>> nltk.download('punkt')

(my_venv) F:\anaconda system\chatbot>python train.py


(my_venv) F:\anaconda system\chatbot>flask --app app run
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
127.0.0.1 - - [23/Feb/2023 15:29:32] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [23/Feb/2023 15:29:32] "GET /static/style.css HTTP/1.1" 304 -
127.0.0.1 - - [23/Feb/2023 15:29:32] "GET /static/app.js HTTP/1.1" 304 -
127.0.0.1 - - [23/Feb/2023 15:29:32] "GET /static/images/chatbox-icon.svg HTTP/1.1" 304 -
127.0.0.1 - - [23/Feb/2023 15:29:37] "POST /predict HTTP/1.1" 200 -
127.0.0.1 - - [23/Feb/2023 15:29:45] "POST /predict HTTP/1.1" 200 -
127.0.0.1 - - [23/Feb/2023 15:29:48] "POST /predict HTTP/1.1" 200 -
127.0.0.1 - - [23/Feb/2023 15:30:00] "POST /predict HTTP/1.1" 200 -
127.0.0.1 - - [23/Feb/2023 15:30:04] "POST /predict HTTP/1.1" 200 -
127.0.0.1 - - [23/Feb/2023 15:30:21] "POST /predict HTTP/1.1" 200 -
127.0.0.1 - - [23/Feb/2023 15:30:32] "POST /predict HTTP/1.1" 200 -
127.0.0.1 - - [23/Feb/2023 15:30:44] "POST /predict HTTP/1.1" 200 -


====================================================================================================


in chrome run this 

http://127.0.0.1:5000
