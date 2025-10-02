from flask import Blueprint, request, jsonify
from app import db, mail
from models import User
from werkzeug.utils import secure_filename
import random
import string
from datetime import datetime, timedelta
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from flask_mail import Message
import os

# --- Blueprints Setup ---
# Separates authentication routes from main application routes.
auth_bp = Blueprint('auth', __name__)
main_bp = Blueprint('main', __name__)

# --- Helper Function ---
def send_otp_email(user):
    """Generates and sends an OTP to the user's email."""
    otp = ''.join(random.choices(string.digits, k=6))
    user.otp = otp
    user.otp_expiration = datetime.utcnow() + timedelta(minutes=10) # OTP valid for 10 minutes
    db.session.commit()

    msg = Message(
        'Your JeevitKrishi Verification Code',
        recipients=[user.email]
    )
    msg.body = f'Your verification code is: {otp}\nIt will expire in 10 minutes.'
    try:
        mail.send(msg)
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False

# --- Authentication Routes ---
@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    email = data.get('email')

    if User.query.filter_by(email=email).first():
        return jsonify({'error': 'Email address already registered'}), 409

    new_user = User(
        full_name=data.get('full_name'),
        email=email,
        primary_crop=data.get('primary_crop'),
        latitude=data.get('latitude'),
        longitude=data.get('longitude')
    )
    db.session.add(new_user)
    db.session.commit()

    if send_otp_email(new_user):
        return jsonify({'message': 'Signup successful. Please check your email for an OTP.'}), 201
    else:
        return jsonify({'error': 'Failed to send OTP email.'}), 500

@auth_bp.route('/verify-otp', methods=['POST'])
def verify_otp():
    data = request.get_json()
    email = data.get('email')
    otp_received = data.get('otp')
    password = data.get('password')

    user = User.query.filter_by(email=email).first()

    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    if user.is_verified:
        return jsonify({'message': 'Account already verified. Please log in.'}), 200

    if user.otp == otp_received and user.otp_expiration > datetime.utcnow():
        user.set_password(password)
        user.is_verified = True
        user.otp = None # Clear OTP after use
        user.otp_expiration = None
        db.session.commit()
        return jsonify({'message': 'Account verified successfully. You can now log in.'}), 200
    else:
        return jsonify({'error': 'Invalid or expired OTP'}), 400

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    
    user = User.query.filter_by(email=email).first()

    if not user or not user.is_verified:
        return jsonify({'error': 'User not found or not verified'}), 401
    
    if user.check_password(password):
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token)
    
    return jsonify({'error': 'Invalid credentials'}), 401

# --- Main Application Routes (Protected) ---
@main_bp.route('/profile', methods=['GET'])
@jwt_required()
def profile():
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
        
    return jsonify({
        'id': user.id,
        'full_name': user.full_name,
        'email': user.email,
        'primary_crop': user.primary_crop,
        'location': {'lat': user.latitude, 'lon': user.longitude}
    })

# The crop image upload and other endpoints would go here.
# For simplicity, they are omitted but would be similar to the profile route.
