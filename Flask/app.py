from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load Model
with open("HDI.pkl", "rb") as file:
    model = pickle.load(file)


# Home Page
@app.route("/")
def home():
    return render_template("home.html")


# Prediction Form
@app.route("/index")
def index():
    return render_template("index.html")


# Prediction
@app.route("/predict", methods=["POST"])
def predict():
    try:
        life = float(request.form["life"])
        mean = float(request.form["mean"])
        expected = float(request.form["expected"])
        gni = float(request.form["gni"])

        data = np.array([[life, mean, expected, gni]])

        prediction = model.predict(data)
        score = round(float(prediction[0]), 3)

        if score >= 0.800:
            category = "Very High Human Development"
        elif score >= 0.700:
            category = "High Human Development"
        elif score >= 0.550:
            category = "Medium Human Development"
        else:
            category = "Low Human Development"

        return render_template(
            "result.html",
            score=score,
            category=category
        )

    except Exception as e:
        return render_template(
            "result.html",
            score="Error",
            category=str(e)
        )


if __name__ == "__main__":
    app.run(debug=True)