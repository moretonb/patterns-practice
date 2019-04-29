from flask import Flask
from app.src.modules.tasks.controllers import tasks_module

app = Flask(__name__)

app.register_blueprint(tasks_module)