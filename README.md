# JeevitKrishi Backend API

A secure backend API for the JeevitKrishi application featuring OTP verification and JWT-based authentication.

## Features

- 🔐 Secure authentication system with OTP verification
- 🔑 JWT token-based session management
- 📧 Email integration for OTP delivery
- 🏗️ Modular architecture for scalability
- 📊 SQLAlchemy database models

## Project Structure

```
backend/
├── app.py              # Application factory and initialization
├── config.py           # Configuration variables
├── models.py           # SQLAlchemy database models
├── routes.py           # API endpoints and blueprints
├── requirements.txt    # Python dependencies
└── .env.example        # Environment variables template
```

## Prerequisites

- Python 3.6+
- pip package manager

## Installation

1. **Navigate to the backend directory:**
    ```bash
    cd backend
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Configure environment variables:**
    - Rename `.env.example` to `.env`
    - Fill in the required details:
      - Generate a `SECRET_KEY` and `JWT_SECRET_KEY`
      - **Important:** Use Gmail App Password for `MAIL_PASSWORD` (not your regular password)
      - [Generate Gmail App Password here](https://support.google.com/accounts/answer/185833)

## Running the Application

```bash
flask run --host=0.0.0.0
```

The API will be available at `http://localhost:5000`
