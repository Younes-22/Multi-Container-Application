from flask import Flask, render_template, request, redirect, url_for
import redis
import os

app = Flask(__name__)

redis_host = os.getenv("REDIS_HOST", "localhost")
r = redis.Redis(host=redis_host, port=6379)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/count', methods=['GET'])
def count():
    r.incr('counter')  # Increment on GET
    count_value = r.get('counter')
    count_value = int(count_value) if count_value else 0
    return render_template('count.html', count=count_value)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)