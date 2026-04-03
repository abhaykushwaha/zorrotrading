# keep_alive.py — Updated version
from flask import Flask
from threading import Thread
import logging

app = Flask(__name__)
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)   # Flask ke chatty logs band karo

@app.route('/')
def home():
    return "Zorro Bot is alive! 🟢", 200

@app.route('/health')
def health():
    return "OK", 200

def keep_alive():
    t = Thread(
        target=lambda: app.run(
            host='0.0.0.0',
            port=8080,
            debug=False,
            use_reloader=False
        )
    )
    t.daemon = True
    t.start()
