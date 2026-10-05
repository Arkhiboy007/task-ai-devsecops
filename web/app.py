import os
import socket
import redis
from flask import Flask, jsonify

app = Flask(__name__)

cache = redis.Redis(
    host=os.getenv("REDIS_HOST", "redis"),
    port=6379,
    decode_responses=True
)

@app.route("/")
def index():
    visits = cache.incr("visits")

    return (
        "<h1>AI DevSecOps Lab</h1>"
        f"<p>Student: {os.getenv('STUDENT', 'Uday Singh Rawat - 16014124804')}</p>"
        f"<p>Host: {socket.gethostname()}</p>"
        f"<p>Visits: {visits}</p>"
    )

@app.route("/health")
def health():
    try:
        cache.ping()
        return jsonify(status="ok")
    except redis.exceptions.RedisError:
        return jsonify(status="redis down"), 503

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)