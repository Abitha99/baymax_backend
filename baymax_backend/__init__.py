from flask import Flask
from baymax_backend.database import init_db
from flask_cors import CORS

app = Flask(__name__)
CORS(app ,expose_headers=['api_key', 'Content-Disposition','filename', 'attachment'])

init_db()

import baymax_backend.views