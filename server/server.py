from flask import Flask, request,jsonify
import util

app = Flask(__name__)


@app.route("/get_location_names")
def get_location_names():
    response = jsonify({
        "locations":util.get_location_names()
    })
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route("./predict_home_price",methods=["POST"])
def predict_home_price():
    total_sqft = float(request.form["total_sqft"])
    location = request.form["location"]
    bhk = int(request.form["bhk"])
    bath = int(request.form["bath"])
    # call estimated_price function
    response = jsonify({
        "estimated_price":util.get_estimated_price(location,total_sqft,bhk,bath)
    })
    response.headers.add("Access-Control-Allow-Origin","*")
    return response

# route to return locations
if __name__ == "__main__":
    print("Strating python Flask server for Home price prediction....")
    app.run() # runs the application on a specific port