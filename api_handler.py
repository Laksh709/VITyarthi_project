import urllib.request
import json
class Currency_API :
    def __init__(self):
        self.base_url = "https://api.frankfurter.app/latest"
    def fetch_rate(self,base_currency,target_currency):
        
        try:
            url = f"{self.base_url}?from={base_currency}&to={target_currency}"
            with urllib.request.urlopen(url) as response :
                data = json.loads(response.read().decode())

            rate = data['rates'][target_currency]
            return rate
        except urllib.error.URLerror:
            print("Error: Could not connect to the API. Check your internet connection.")
            return None
        except KeyError:
            print("Error: Invalid currency code.")
            return None