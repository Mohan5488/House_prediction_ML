import pickle
import numpy as np
import json
import os
from django.conf import settings
from django.shortcuts import render

# Load the trained model
if os.path.exists("static/prediction.pickle"):
    with open("static/prediction.pickle", "rb") as f:
        model = pickle.load(f)
else:
    model = None 

    
columns_path = "static/columns.json"    
if os.path.exists(columns_path):
    with open(columns_path, "r") as f:
        data_columns = json.load(f)["data_columns"]
else:
    data_columns = []
    
def predict_home_price(request):
    estimated_price = None

    if request.method == "POST":
        location = request.POST.get("location")
        sqft = request.POST.get("sqft")
        bath = request.POST.get("bath")
        bhk = request.POST.get("bhk")

        try:
            sqft = float(sqft)
            bath = float(bath)
            bhk = int(bhk)

            input_data = np.zeros(len(data_columns))
            input_data[0] = bhk
            input_data[1] = sqft
            input_data[2] = bath

            if location in data_columns:
                loc_index = data_columns.index(location)
                input_data[loc_index] = 1

            estimated_price = round(model.predict([input_data])[0], 2)
            

        except Exception as e:
            estimated_price = f"Error: {str(e)}"

    return render(request, "prediction.html", {"estimated_price": estimated_price, "locations": data_columns[3:]})


def home(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")