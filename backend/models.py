from app import db, bcrypt
import datetime

class User(db.Model):
    """
    Represents a farmer user in the database.
    """
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    
    # Farmer specific details
    primary_crop = db.Column(db.String(100), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    
    # For OTP verification
    otp = db.Column(db.String(6))
    otp_expiration = db.Column(db.DateTime)
    is_verified = db.Column(db.Boolean, default=False, nullable=False)
    
    # Relationships
    crop_data = db.relationship('CropData', backref='farmer', lazy=True)

    def set_password(self, password):
        """Hashes the password and stores it."""
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        """Checks if the provided password matches the stored hash."""
        return bcrypt.check_password_hash(self.password_hash, password)

class CropData(db.Model):
    """
    Represents data related to a specific crop image upload.
    """
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    crop_type = db.Column(db.String(100), nullable=False)
    image_path = db.Column(db.String(200), nullable=False)
    upload_time = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    diagnosis = db.Column(db.String(200))
    recommendation = db.Column(db.String(500))

