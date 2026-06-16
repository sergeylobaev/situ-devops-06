from flask import Flask
from redis import Redis
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

redis = Redis(
    host="redis",
    port=6379,
    decode_responses=True
)

# Prometheus counter (в памяти процесса)
VISITS = Counter(
    "flask_visits_total",
    "Total visits"
)


@app.route("/")
def home():
    visits = redis.incr("counter")

    VISITS.inc()

    return f"Visits: {visits}"


@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {
        "Content-Type": CONTENT_TYPE_LATEST
    }


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False,
        use_reloader=False
    )