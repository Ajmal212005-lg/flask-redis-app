from flask import Flask
import redis
import os

app = Flask(__name__)
# Connect to redis service defined in docker-compose
cache = redis.Redis(host=os.getenv('REDIS_HOST', 'redis'), port=6379)

@app.route('/')
def hello():
    count = cache.incr('hits')
    return f'<h1>Hello from Flask & Redis!</h1><p>This web page has been viewed <b>{count}</b> times (managed via Docker Compose).</p>'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
