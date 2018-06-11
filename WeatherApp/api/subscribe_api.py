import __root_path__, json

from flask import Flask, abort, request, render_template, jsonify
from validate_email import validate_email

from data_access import file_agent, sub_record
from utils import app_logger

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

    # try:
    # Request with no form data is bad.

    logger = app_logger.AppLogger().get_logger()

    if not request.form:
        logger.error("No Form Data")
        abort(400)

    # Request with either email or city not present is bad.
    if "email" not in request.form or "city" not in request.form:
        logger.error("email or city not present in data")
        abort(400)

    email = request.form["email"]
    if not validate_email(email):
        logger.error("email invalid")
        abort(400)

    city = request.form['city']
    if len(city) == 0:
        logger.error("city is empty")

    record = sub_record.SubscriptionRecord(email, city)

    agent = file_agent.FileAgent()
    agent.add_record(record)

    return "SUCCESS"
    # except:
    #    logger.error("Could not register the subscription for user email {0} and city {1}".format(email, city))
    #    abort(500)


@app.route("/funday/getcities", methods=["GET"])
def get_cities():
    """
    Gets the list of cities.
    :return:
    """

    logger = app_logger.AppLogger().get_logger()

    city_json = {}
    # try:
    with open(__root_path__.path() + "/data_store/top_city_list.json", "r") as cities:
        city_json = json.load(cities)

    return jsonify(city_json)
    # except:
    #    logger.error("Could not retrieve top 100 cities")
    #    abort(500)

if __name__ == '__main__':
    #try:
    props_path = __root_path__.path() + "/resources/properties.json"
    properties = {}
    with open(props_path, "r") as props:
        properties = json.load(props)
    app.run(host='0.0.0.0', port=properties["http_server_port"], debug=True)
    # except:
    # app_logger.AppLogger().get_logger().error("Error while starting the web application")
