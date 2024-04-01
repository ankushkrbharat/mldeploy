from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

app=Flask(__name__)

with open('model_pickle','rb') as f:
   mp= pickle.load(f)


@app.route('/', methods=['POST'])
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
    try:
        price=mp.predict([[area,br,bt
                       ,n,age]])[0]
    except:
        print("error in prediction")
        
    response_data = {
            "price":price
        }
    
    

    # Return the extracted data in a JSON response
    return jsonify(response_data)




# {
#    "area":265456,
#    "br":2,
#    "bt":1,
#    "n":0,
#    "age":1995
# }