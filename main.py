from api_handler import Currency_API
from portfolio import Wallet 
from storage import File_Handler

file_handler = File_Handler()
saved_data = file_handler.load_data()

wallet = Wallet(saved_data)

rate = Currency_API()
while True:
    print("Services offered : \n 1)View Balance \n 2)Deposit Money \n 3) Withdraw money \n 4)Exit")
    choice = int(input("Please enter your preffered service "))
    if choice == 1:
        result = wallet.get_balance()
        print(f"Your current balance is {result}")
    elif choice ==2 :
        currency = input("Enter your preffered currency")
        amount = int(input("Enter your desiered amount "))
        result1 = wallet.deposit()
        print(result1)
    elif choice ==3:
        print("For your information - We deduct a fee of 0.02 percent of your amount as processing charges ")
        source_currency = input("Which currency do you want to withdraw from?")
        target_currency = input("Which currency you want your withdrawn money in??")
        result_2 = wallet.withdraw_with_conversion()
        print(result_2)
    


