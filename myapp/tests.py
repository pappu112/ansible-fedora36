import pandas as pd 
import requests 

df = pd.read_csv("../experiment-tracking/kc_house_data.csv")

# choose features
features = ["bedrooms","bathrooms","sqft_living","sqft_above","grade",
            "floors","view",'sqft_lot','floors','waterfront','zipcode'] 

feature_df = df[features]
row = list(feature_df.loc[7,:])

r = requests.post("http://67.205.137.200:5002/predict", json={"data":{"ndarray":[row]}})
print(r.content)
