from app.src.server import app
from app.src.data.client import redis_client

app.testing = True
api_client = app.test_client()