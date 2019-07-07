from app.model.google_result import GoogleResult

from flask import Flask
from flask_mongoengine import MongoEngine
from flask import abort, request, jsonify, g
from flasgger import Swagger  
from googlesearch import search

app = Flask(__name__)
app.config.from_object('app.config.DevelopmentConfig')
db = MongoEngine(app)
Swagger(app)

@app.route('/api/search/google', methods=['POST'])
def google_search():
    search_str = request.json.get('search_str')
    size = request.json.get('size')
    google_search_results = list(search(search_str, stop=size))
    for result in google_search_results:
        google_result = GoogleResult(url=result)
        try:
            GoogleResult.objects.get(url=result)
        except google_result.DoesNotExist:
            google_result.save()
        
    return jsonify(google_search_results)