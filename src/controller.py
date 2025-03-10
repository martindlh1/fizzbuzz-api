from flask import Flask, request, jsonify
from flask_cors import CORS
from src.fizzbuzz import generate_fizzbuzz
import logging
import time

app = Flask(__name__)
CORS(app)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@app.route('/fizzbuzz', methods=['POST'])
def fizzbuzz():
    data = request.json
    fizz_nb = int(data.get('fizz_nb'))
    buzz_nb = int(data.get('buzz_nb'))
    start = int(data.get('start'))
    end = int(data.get('end'))

    start_time = time.time()
    result = generate_fizzbuzz(fizz_nb, buzz_nb, start, end)
    end_time = time.time()

    logger.info(f"Execution time: {end_time - start_time:.4f} seconds for range size: {end - start + 1}")
    return jsonify(result)
