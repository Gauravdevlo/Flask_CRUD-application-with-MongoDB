# app/config.py
import os
class Config:
    MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://Gaurav:8420979681@cluster0.l8zlb.mongodb.net/flask_mongo_crud?retryWrites=true&w=majority")
    SECRET_KEY = os.getenv("SECRET_KEY", "secret")
    DEBUG = False
class DevelopmentConfig(Config):
    DEBUG = True
class ProductionConfig(Config):
    DEBUG = False
config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig
}
