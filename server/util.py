import json
import pickle
import numpy as np

# create global variables
__locations = None
__data_columns = None
__model = None


# function to return location,bhk,sqft,bath
def get_estimated_price(location, sqft, bhk, bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1
    # return the estimated price rounded to 2dp
    return round(__model.predict([x])[0], 2)


def get_location_names():
    return __locations


# will return global variables
def load_saved_artifacts():
    print("Loading saved artifacts.... start")
    global __data_columns
    global __locations

    with open("./artifacts/columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']
        # load data_columns from index 3
        __locations = __data_columns[3:]

    # load model
    global __model
    with open("./artifacts/Bengaluru_Home_prices_model.pickle", 'rb') as f:
        __model = pickle.load(f)
    print("Loading saved artifacts....done")


if __name__ == '__main__':
    load_saved_artifacts()
    # print(get_location_names())
    # call get_estimated price function
    # print(get_estimated_price('1st Phase Jp Nagar', 1000, 3, 3))
    # print(get_estimated_price('1st Phase Jp Nagar', 1000, 2, 2))
    # print(get_estimated_price('kalhalli', 1000, 2, 2))  # other location
    # print(get_estimated_price('Ejipura', 1000, 2, 2))  # other location
