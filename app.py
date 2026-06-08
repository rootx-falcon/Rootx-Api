from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

ORIGINAL_URL = "https://leakosint-by-noneusr.vercel.app/@None_usernam3/free/public/api/search"

@app.route('/api/search')
def search():
    phone = request.args.get('phone')
    if not phone:
        return jsonify({"error": "Missing 'phone' param"}), 400
    
    resp = requests.get(f"{ORIGINAL_URL}={phone}", timeout=15)
    original_data = resp.json()
    original_data["developer"] = "@FALCON_HU"
    
    return jsonify(original_data)

@app.route('/')
def home():
    return jsonify({"status": "RootX Falcon API Active", "developer": "@FALCON_HU"})

if __name__ == '__main__':
    app.run()
