from flask import Flask, jsonify, request

from simple_interest.calculator import calculate_simple_interest
from simple_interest.swagger import get_swagger_spec, swagger_ui_html
from simple_interest.validation import validate_simple_interest_payload

app = Flask(__name__)


@app.route("/simple-interest", methods=["POST"])
def simple_interest():
    if not request.is_json:
        return jsonify(error="Request must be JSON."), 400

    payload = request.get_json(silent=True)
    if payload is None:
        return jsonify(error="Invalid JSON body."), 400

    validated = validate_simple_interest_payload(payload)
    if isinstance(validated, str):
        return jsonify(error=validated), 400

    principal = validated["principal"]
    rate = validated["rate"]
    time = validated["time"]

    interest = calculate_simple_interest(principal, rate, time)
    return jsonify(
        principal=principal,
        rate=rate,
        time=time,
        simple_interest=interest,
    )


@app.route("/openapi.json", methods=["GET"])
def openapi_spec():
    return jsonify(get_swagger_spec())


@app.route("/docs", methods=["GET"])
def swagger_ui():
    return swagger_ui_html("/openapi.json")


if __name__ == "__main__":
    app.run(debug=True)
