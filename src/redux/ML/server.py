from flask import Flask, jsonify
import requests
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/dynamic-prices", methods=["GET"])
def dynamic_prices():
    response = requests.get("https://fakestoreapi.com/products/")
    products = response.json()

    df = pd.DataFrame(products)
    df["rating_value"] = df["rating"].apply(lambda r: r["rate"])

    X = df[["rating_value"]].values
    y = (df["price"] / df["price"].mean()).values

    model = LinearRegression()
    model.fit(X, y)

    adjustment_factors = model.predict(X)

    adjustment_factors = np.clip(adjustment_factors, 0.85, 1.15)

    df["suggested_price"] = (df["price"] * adjustment_factors).round(2)

    result = df[["id", "suggested_price"]].to_dict(orient="records")
    
    return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)

