from flask import Flask
import os
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

import sys

if 'pytest' in sys.modules:
    secret = os.getenv("SECRET_KEY", "test-secret")
else:
    secret = os.getenv("SECRET_KEY")
    if not secret:
        raise RuntimeError("SECRET_KEY environment variable is required")

app.secret_key = secret
CSRFProtect(app)
from app import routes
