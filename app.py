
from flask import Flask

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = " hello"