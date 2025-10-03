import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # API Keys
    OPENWEATHER_API_KEY = os.getenv('OPENWEATHER_API_KEY')
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    
    # Paths
    MODEL_PATH = os.getenv('MODEL_PATH', './models/crop_recommendation_model.pkl')
    DATA_PATH = './data'
    
    # Model Settings
    RANDOM_STATE = 42
    TEST_SIZE = 0.2
    
    # LLM Settings
    LLM_MODEL = "gpt-3.5-turbo"
    MAX_TOKENS = 500
    TEMPERATURE = 0.7