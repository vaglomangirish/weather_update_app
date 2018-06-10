import json

from flask import Flask, abort, request

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
    if not request.json:
        abort(400)
    data_json = request.json
    if "email" not in data_json or "city" not in data_json:
        abort(400)

    email = data_json["email"]
    city = data_json["city"]

    record = sub_record.SubscriptionRecord(email, city)

    agent = file_agent.FileAgent()
    agent.add_record(record)

    return "SUCCESS"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)