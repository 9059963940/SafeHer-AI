from flask import Flask, render_template, request, jsonify
import joblib
import requests

app = Flask(__name__)

model = joblib.load('models/distress_model.pkl')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/predict', methods=['POST'])
def predict():

    data = request.json
    text = data['message']

    prediction = model.predict([text])[0]

    if prediction == 1:
        result = "🚨 HIGH RISK ALERT"
    else:
        result = "✅ SAFE"

    return jsonify({"result": result})


@app.route('/nearby')
def nearby():

    try:

        lat = request.args.get('lat')
        lon = request.args.get('lon')

        hospitals_url = (
            f"https://nominatim.openstreetmap.org/search?"
            f"q=hospital&format=jsonv2&limit=5"
        )

        police_url = (
            f"https://nominatim.openstreetmap.org/search?"
            f"q=police station&format=jsonv2&limit=5"
        )

        headers = {
            "User-Agent": "SafeHerAI"
        }

        hospitals = requests.get(
            hospitals_url,
            headers=headers
        ).json()

        police = requests.get(
            police_url,
            headers=headers
        ).json()

        return jsonify({
            "success": True,
            "hospitals": hospitals,
            "police": police
        })

    except Exception as e:

        print("ERROR:", e)

        return jsonify({
            "success": False,
            "message": str(e)
        })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)