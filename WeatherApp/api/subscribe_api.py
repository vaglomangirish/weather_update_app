import __root_path__, json

from flask import Flask, abort, request, render_template, jsonify
from validate_email import validate_email

from data_access import file_agent, sub_record

app = Flask(__name__)


@app.route('/')
def render():
    return render_template("index.html")


@app.route("/funday/subscribe", methods=["POST"])
def subscribe_weather():
    """
    Request json:-
    {
        "email": <email>
        "city": <city>
    }
    :return:
    """
    # Request with no form data is bad.
    if not request.form:
         print("ERROR: No Form Data")
         abort(400)

    # Request with either email or city not present is bad.
    if "email" not in request.form or "city" not in request.form:
         print("ERROR: email or city not present in data")
         abort(400)

    email = request.form["email"]
    if not validate_email(email):
         print("ERROR: email invalid")
         abort(400)

    city = request.form['city']

    record = sub_record.SubscriptionRecord(email, city)

    agent = file_agent.FileAgent()
    agent.add_record(record)

    return "SUCCESS"


@app.route("/funday/getcities", methods=["GET"])
def get_cities():
    """
    Gets the list of cities.
    :return:
    """
    city_json = {}
    with open(__root_path__.path() + "/data_store/top_city_list.json", "r") as cities:
        city_json = json.load(cities)

    return jsonify(city_json)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)