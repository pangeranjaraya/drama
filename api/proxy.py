from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/api/proxy')
def api_proxy():
    url = request.args.get('url')
    if not url:
        return jsonify({"error": "No URL provided"}), 400
    
    try:
        res = requests.get(url, timeout=10)
        return jsonify(res.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Vercel handler
handler = app
