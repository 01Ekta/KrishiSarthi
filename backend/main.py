import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_mail import Mail
from datetime import timedelta

# Initialize extensions
db = SQLAlchemy()
bcrypt = Bcrypt()
jwt = JWTManager()
mail = Mail()

def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)

    # --- Configuration ---
    # Load configuration from a config file
    app.config.from_pyfile('config.py')

    # --- Initialize Extensions with App Context ---
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    mail.init_app(app)

    # --- File Upload Configuration ---
    UPLOAD_FOLDER = 'uploads'
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    with app.app_context():
        # --- Import and Register Blueprints (Routes) ---
        from routes import auth_bp, main_bp
        app.register_blueprint(auth_bp, url_prefix='/auth')
        app.register_blueprint(main_bp)

        # --- Create Database Tables ---
        # This will create tables for all models defined in models.py
        db.create_all()

    return app

if __name__ == '__main__':
    app = create_app()
    # Runs the Flask app. Host 0.0.0.0 makes it accessible on your local network
    app.run(debug=True, host='0.0.0.0')

