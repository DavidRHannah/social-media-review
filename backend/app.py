from flask import Flask
from api.routes import api
import logging

def create_app():
    """
    Create and configure the Flask application.
    """
    app = Flask(__name__)
    
    # Set up basic logging.
    logging.basicConfig(level=logging.INFO)
    
    # Register the API blueprint with the '/api' prefix.
    app.register_blueprint(api, url_prefix='/api')
    
    @app.route('/')
    def index():
        return "Welcome to the Recommendation API"
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)
