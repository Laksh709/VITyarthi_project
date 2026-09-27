import json 
class File_Handler:
    def save_data(self,wallet_dict , file_name =  "transactions.json"):
        
        with open(file_name , "w") as f:
            json.dump(wallet_dict , f)
    
    def load_data(self,file_name =  "transactions.json"):
        try:
            with open(file_name , "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}



