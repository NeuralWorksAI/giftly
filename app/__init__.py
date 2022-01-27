from flask import Flask

app = Flask(__name__)
app.config["SECRET_KEY"] = "key"

from app import routes