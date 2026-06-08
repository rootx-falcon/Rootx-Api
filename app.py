from flask import Flask, request, Response
import requests
import json

app = Flask(__name__)

ORIGINAL_URL = "https://leakosint-by-noneusr.vercel.app/@None_usernam3/free/public/api/search"

@app.route('/@Kasa.7z/free/public/api/search')
def proxy():
    phone = request.args.get('search')
    if not phone:
        return {"error": "Missing 'search' param"}, 400
    
    resp = requests.get(f"{ORIGINAL_URL}={phone}", timeout=15)
    original_data = resp.json()
    
    # Watermark
    original_data["developer"] = "@FALCON_HU"
    
    return Response(
        response=json.dumps(original_data, indent=2),
        status=resp.status_code,
        mimetype='application/json'
    )

@app.route('/')
def home():
    return {"status": "RootX Falcon API Active", "developer": "@FALCON_HU"}

if __name__ == '__main__':
    app.run()