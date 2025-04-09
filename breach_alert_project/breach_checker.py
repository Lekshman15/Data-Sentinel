# breach_checker.py
import requests

def check_leak(email):
    url = f"https://leakcheck.io/api/public?email={email}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if data.get("success"):
            return data.get("sources", [])
        else:
            return []
    else:
        return []
