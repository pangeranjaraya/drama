from flask import Flask, render_template, jsonify, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# Proxy API Universal
@app.route('/api/proxy')
def api_proxy():
    url = request.args.get('url')
    if not url:
        return jsonify({"error": "No URL provided"}), 400
    
    try:
        # Forward header jika diperlukan, tapi kebanyakan API publik open
        res = requests.get(url)
        return jsonify(res.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
