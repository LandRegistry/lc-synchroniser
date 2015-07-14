import os
from flask import Flask
import threading


app = Flask(__name__)
app.config.from_object(os.getenv('SETTINGS', "config.DevelopmentConfig"))


from application.server import run
process_thread = threading.Thread(name='synchroniser', target=run)
process_thread.daemon = True
process_thread.start()