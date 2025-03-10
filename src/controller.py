from flask import Flask, request, jsonify

from src.fizzbuzz import generate_fizzbuzz

app = Flask(__name__)


@app.route('/fizzbuzz', methods=['POST'])
def fizzbuzz():
    data = request.json
    fizz_nb = int(data.get('fizz_nb'))
    buzz_nb = int(data.get('buzz_nb'))
    start = int(data.get('start'))
    end = int(data.get('end'))
    result = generate_fizzbuzz(fizz_nb, buzz_nb, start, end)
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True, port=8000)
