from flask import Flask, jsonify, render_template, request
from api_client import get_tirages
from model import analyser_tirages

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/analyse', methods=['GET'])
def analyse():
    try:
        tirages = get_tirages()
        exclude_last_n = int(request.args.get("exclude_last", 0))
        jour = request.args.get("jour")
        start_date = request.args.get("start_date")
        end_date = request.args.get("end_date")
        resultat = analyser_tirages(
            tirages,
            exclude_last_n=exclude_last_n,
            jour=jour,
            start_date=start_date,
            end_date=end_date
        )
        return jsonify(resultat)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)