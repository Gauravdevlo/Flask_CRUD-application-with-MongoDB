import os
from app import create_app
from dotenv import load_dotenv
load_dotenv()
config_type = os.getenv("FLASK_CONFIG", "development")
app = create_app(config_type)
@app.route('/')
def home():
    return "Welcome to the User API!"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
