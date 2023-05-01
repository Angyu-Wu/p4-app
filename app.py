from flask import Flask, request, jsonify
import joblib
import pickle
import pandas as pd
app = Flask(__name__)


directory = rf'C:\Users\Wu\Desktop\book\stock dataset'
filename = directory+r'\finalized_model.sav'
loaded_model = joblib.load(open(filename, 'rb'))

@app.route('/predict', methods=['GET'])
def respond():
    # Retrieve the name from the url parameter /getmsg/?name=
    vol_moving_avg = request.args.get("vol_moving_avg",None)
    adj_close_rolling_med = request.args.get("adj_close_rolling_med", None)
   
    d = [{'vol_moving_avg': vol_moving_avg, 'adj_close_rolling_med': adj_close_rolling_med}]
   
    X = pd.DataFrame(data=d)
    y_predicted = loaded_model.predict(X)
    result = f''+str(y_predicted[0])
   
    

    
    response = {}
    
    response["Prediction"] = f'vol_moving_avg is  {vol_moving_avg} and adj_close_rolling_med {adj_close_rolling_med} then result is {result}'
    # Check if the user sent a name at all

    # Return the response in json format
    return jsonify(response)

@app.route('/')
def index():
    # A welcome message to test our server
    return "<h1>Welcome to our medium-greeting-api!</h1>"




if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000, debug=True)