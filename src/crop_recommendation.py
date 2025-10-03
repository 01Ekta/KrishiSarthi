import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import accuracy_score
import joblib
import os
import sys

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config.settings import Config

class CropRecommendationSystem:
    def __init__(self):
        self.model = None
        self.scaler = StandardScaler()
        self.label_encoder = LabelEncoder()
        self.region_encoder = LabelEncoder()
        self.config = Config()
    
    # ... (Keep all your existing methods from previous code)
    # Generate sample data, train model, recommend crop, etc.
    
    def save_model(self):
        """Save the trained model and preprocessors"""
        os.makedirs(os.path.dirname(self.config.MODEL_PATH), exist_ok=True)
        
        model_data = {
            'model': self.model,
            'scaler': self.scaler,
            'label_encoder': self.label_encoder,
            'region_encoder': self.region_encoder
        }
        joblib.dump(model_data, self.config.MODEL_PATH)
        print(f"Model saved to {self.config.MODEL_PATH}")
    
    def load_model(self):
        """Load the trained model and preprocessors"""
        if os.path.exists(self.config.MODEL_PATH):
            model_data = joblib.load(self.config.MODEL_PATH)
            self.model = model_data['model']
            self.scaler = model_data['scaler']
            self.label_encoder = model_data['label_encoder']
            self.region_encoder = model_data['region_encoder']
            print(f"Model loaded from {self.config.MODEL_PATH}")
            return True
        else:
            print("No saved model found. Please train a new model.")
            return False