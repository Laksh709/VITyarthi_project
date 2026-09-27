import urllib.request
import json
import urllib.error
class Currency_API :
    def __init__(self):
        self.base_url = "https://api.exchangerate-api.com/v4/latest"
    def fetch_rate(self,base_currency,target_currency):
        
        try:
            url = f"{self.base_url}/{base_currency}"
            with urllib.request.urlopen(url) as response :
                data = json.loads(response.read().decode())

            rate = data['rates'][target_currency]
            return rate
        except urllib.error.URLError:
            print("\n[Warning] Network blocked or offline. Using backup exchange rates.")
            backup_rates = {
                "INR": 83.50,
                "EUR": 0.92,
                "GBP": 0.79,
                "AUD": 1.52,
                "CAD": 1.36
            }
            return backup_rates.get(target_currency)
            
        except KeyError:
            print("Error: Invalid currency code.")
            return None