from flask import Flask,request,jsonify
import util

app = Flask(__name__)

# write route to get location names
@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/predict_home_price',methods = ['POST'])
def predict_home_price():
    # return all the requests from inputs in form of regest.form
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    # now call util.get_estimated_price function
    response = jsonify({
        'estimated_price': util.get_estimated_price(location,total_sqft,bhk,bath)
    })

    response.headers.add('Access-Control-Allow-Origin','*')
    return  response


if __name__ == "__main__":
    print("starting Python Flask server for Home Price Prediction")
    app.run()

# download and install postman for testing (used for creating and testing APIs.)