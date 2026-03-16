import requests

def check_breach(email):
    url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
    
    headers = {
        "User-Agent": "DigitalFootprintAnalyzer"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        breaches = response.json()
        sites = [b['Name'] for b in breaches]
        return True, sites

    elif response.status_code == 404:
        return False, []

    else:
        return None, []
