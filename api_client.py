import requests

API_URL = "http://localhost:8000/api/v1/scan"

def scan_message(text: str):
    """Sends text to the backend and returns the JSON response or an error."""
    try:
        response = requests.post(API_URL, json={"content": text, "language": "en"}, timeout=10)
        if response.status_code == 200:
            return response.json(), None
        return None, "Error from backend analysis service."
    except requests.exceptions.ConnectionError:
        return None, "Backend server is not running. Please start the FastAPI backend first."