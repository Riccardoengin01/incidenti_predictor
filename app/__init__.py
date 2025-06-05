from flask import Flask

app = Flask(__name__)
app.secret_key = "chiave-segreta"
from app import routes
