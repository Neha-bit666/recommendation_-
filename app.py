from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load the dataset
df = pd.read_csv("herbal_remedies_expanded.csv")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/recommend", methods=["POST"])
def recommend():
    user_input = request.form["user_input"].strip().lower()
    recommendations = df[df["Disease"].str.lower().str.contains(user_input) | 
                       df["Symptoms"].str.lower().str.contains(user_input)]
    
    if not recommendations.empty:
        return render_template("recommendations.html", recommendations=recommendations)
    else:
        return render_template("no_results.html")

if __name__ == "__main__":
    app.run(debug=True)