from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for your friend's app to access this API

# Language data
languages = [
    {"id": 1, "name": "Hindi", "nativeName": "हिन्दी"},
    {"id": 2, "name": "Bengali", "nativeName": "বাংলা"},
    {"id": 3, "name": "Telugu", "nativeName": "తెలుగు"},
    {"id": 4, "name": "Marathi", "nativeName": "मराठी"},
    {"id": 5, "name": "Tamil", "nativeName": "தமிழ்"},
    {"id": 6, "name": "Gujarati", "nativeName": "ગુજરાતી"},
    {"id": 7, "name": "Kannada", "nativeName": "ಕನ್ನಡ"},
    {"id": 8, "name": "Punjabi", "nativeName": "ਪੰਜਾਬੀ"},
    {"id": 9, "name": "Odia", "nativeName": "ଓଡ଼ିଆ"},
    {"id": 10, "name": "Urdu", "nativeName": "اردو"}
]

@app.route('/')
def home():
    return jsonify({
        "message": "Indian Languages API",
        "endpoints": {
            "GET /api/languages": "Get all languages",
            "GET /api/language/<id>": "Get language by ID",
            "GET /api/language/name/<name>": "Get language by name"
        }
    })

# GET all languages
@app.route('/api/languages', methods=['GET'])
def get_all_languages():
    return jsonify({
        "success": True,
        "data": languages
    })

# GET language by ID
@app.route('/api/language/<int:language_id>', methods=['GET'])
def get_language_by_id(language_id):
    language = next((lang for lang in languages if lang["id"] == language_id), None)
    
    if language:
        return jsonify({
            "success": True,
            "data": language
        })
    else:
        return jsonify({
            "success": False,
            "message": "Language not found"
        }), 404

# GET language by name
@app.route('/api/language/name/<string:name>', methods=['GET'])
def get_language_by_name(name):
    language = next((lang for lang in languages if lang["name"].lower() == name.lower()), None)
    
    if language:
        return jsonify({
            "success": True,
            "data": language
        })
    else:
        return jsonify({
            "success": False,
            "message": "Language not found"
        }), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)