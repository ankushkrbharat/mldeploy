from flask import Flask, request, jsonify,render_template
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
from flask_cors import CORS

app=Flask(__name__)

CORS(app)

with open('model_pickle','rb') as f:
   mp= pickle.load(f)



@app.route('/')
def Home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def postit():
     # Extract data from the POST request
    data = request.get_json()

    # Extract specific fields from the JSON data
    area = data.get('area')
    br = data.get('br')
    bt = data.get('bt')
    n = data.get('n')
    age = data.get('age')

    # Process the data or perform any necessary operations
    # For demonstration, let's just return the extracted data in a response
    
    price=mp.predict([[area,br,bt
                       ,n,age]])[0]
    
        
    response_data = {
            "price":price
        }
    
    

    # Return the extracted data in a JSON response
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)


# {
#    "area":265456,
#    "br":2,
#    "bt":1,
#    "n":0,
#    "age":1995
# }