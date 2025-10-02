import os
from datetime import timedelta

# This file contains the configuration variables for the Flask app.

# --- General Config ---
SECRET_KEY = os.environ.get('SECRET_KEY', 'a-very-secret-key-that-you-should-change')

# --- Database Config ---
SQLALCHEMY_DATABASE_URI = 'sqlite:///jeevitkrishi.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# --- JWT Config ---
# Sets the expiration time for JWTs. Users will need to re-login after this period.
JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 'another-super-secret-key')
JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=7)

# --- Mail Config for OTP ---
# Configuration for sending emails via Gmail SMTP.
# IMPORTANT: You must set the MAIL_USERNAME and MAIL_PASSWORD environment variables.
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = os.environ.get('MAIL_USERNAME') # Your Gmail address
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') # Your Gmail App Password
MAIL_DEFAULT_SENDER = os.environ.get('MAIL_USERNAME')
