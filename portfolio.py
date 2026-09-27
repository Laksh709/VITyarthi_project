class Wallet:
    def __init__(self , initial_balances=None):
        self.__balances = initial_balances if initial_balances else {}

    def get_balance(self):
       return self.__balances.copy()
    
    def deposit(self,currency, amount):
       currency = currency.strip().upper()
       if amount <= 0:
           return False
       currency = currency.strip().upper()
       self.__balances[currency]= self.__balances.get(currency,0.0) + round(amount,2)
       return True, f"Successfully deposited {amount:.2f} {currency}."

    def withdraw_with_conversion(self, source_curr, target_curr, source_amount, api_client, fee_percent=0.02):
        source_curr = source_curr.strip().upper()
        target_curr = target_curr.strip().upper()

        if source_amount <= 0:
            return False, "Withdrawal amount must be greater than zero.", 0.0
        current_balance = self.__balances.get(source_curr,0.0)
        if current_balance< source_amount:
            return False , f"Insufficient funds. Available: {current_balance:.2f} {source_curr}.", 0.0
        if source_curr== target_curr:
            rate = 1.0
        else:
            rate = api_client.fetch_rate(source_curr,target_curr)
            if rate is None :
                return False , f"Could not retreive exchange rates for {source_curr} to {target_curr}" , 0.0

        fee = round(source_amount*fee_percent,2)
        net_source = source_amount-fee
        converted_payout = round(net_source*rate  ,2)

        self.__balances[source_curr]-= source_amount
        success_message = (
            f"Withdrew {source_amount:.2f} {source_curr}. "
            f"Fee: {fee:.2f} {source_curr}, Net converted: {net_source:.2f} {source_curr} at rate {rate:.2f}"
        )
        return True , success_message, converted_payout