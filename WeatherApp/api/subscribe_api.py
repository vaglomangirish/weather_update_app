from flask import Flask, abort, request
from validate_email import validate_email

from data_access import file_agent, sub_record

app = Flask(__name__)
# app.config["APPLICATION_ROOT"] = "/fundayweather"


@app.route("/subscribe", methods=["POST"])
def subscribe_weather():
    """
    Request json:-
    {
        "email": <email>
        "city": <city>
    }
    :return:
    """
    # Request with no json is bad.
    if not request.json:
        abort(400)
    data_json = request.json

    # Request with either email or city not present is bad.
    if "email" not in data_json or "city" not in data_json:
        abort(400)

    email = data_json["email"]

    # Request with invalid email is bad.
    if not validate_email(email):
        abort(400)

    city = data_json["city"]

    record = sub_record.SubscriptionRecord(email, city)

    agent = file_agent.FileAgent()
    agent.add_record(record)

    return "SUCCESS"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)