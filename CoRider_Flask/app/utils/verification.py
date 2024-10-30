import re
def validate_email(email):
    """Validates the email format."""
    email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(email_regex, email) is not None

def validate_password(password):
    """Validates the password (e.g., minimum length of 6 characters)."""
    return len(password) >= 6

def validate_user_data(data):
    """to validate user data"""
    if "name" not in data or not data["name"].strip():
        return False, "required field"
    if "email" not in data or not validate_email(data["email"]):
        return False, "wrong format"
    if "password" not in data or not validate_password(data["password"]):
        return False, "password must be 6 charac long"
    return True, "Successful Validation"
