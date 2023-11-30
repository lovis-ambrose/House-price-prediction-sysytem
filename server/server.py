from flask import Flask, request, jsonify, render_template
import os
import util

app = Flask(__name__)

# render html template
@app.route('/')
def home():
    return render_template('app.html')

# Call load_saved_artifacts when the Flask app starts
util.load_saved_artifacts()


# write route to get location names
@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    # return all the requests from inputs in form of regest.form
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    # now call util.get_estimated_price function
    response = jsonify({
        'estimated_price': util.get_estimated_price(location, total_sqft, bhk, bath)
    })

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


# if __name__ == "__main__":
#     print("Starting Python Flask server for Home Price Prediction")
#     # Run the Flask app on all available network interfaces and port 5000
#     app.run(host='localhost', port=5000)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
