from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/v1.0/predict', methods=['GET'])
def predict():
    v1 = request.args.get("v1", 0)
    v2 = request.args.get("v2", 0)

    try:
        v1 = float(v1)
    except (ValueError, TypeError):
        v1 = 0.0

    try:
        v2 = float(v2)
    except (ValueError, TypeError):
        v2 = 0.0

    prediction = 1 if v1 + v2 > 5.8 else 0
    response = {
        "features": [v1, v2],
        "prediction": prediction
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
