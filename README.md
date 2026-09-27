# Live Currency Converter & Portfolio CLI
This is my python project. It allows a user to check their balance,deposit and withdraw money across different 
currencies. It is a simple CLI interface project and can be easliy run using command line .

---

## Overview

It tries to mimic a wallet which stores and simulates operations across user's accounts having multiple
currencies stored acoss diffenent account. It uses live exchnage rates for conversions too.
.

---

## Features

- **Multi-Currency Wallet Management:** Helps the user to balances across multiple world currencies (e.g., USD, INR, EUR).
- **Live Exchange Rates:** Fetches up-to-date conversion rates dynamically via a lightweight foreign exchange API (`api.exchangerate-api.com`).
- **Offline backup** In case of loss of network access and api cannot be fetched , it has a inbuilt
databse for most famous and widley used currencies acorss the world for emergency situations
- **Transaction Fee**  I tried to make it seem like a real bank,so it automatically deducts a transparent 0.02% processing fee before executing currency conversions.
- **Usage of object oriented Programming** Made the whole project around multiple classes and objects to make 
it clean and proffessiobnal and used abstraction and encapsulation to reduce complexity for the user.
- **Flexible storage** Automatically writes and loads wallet states to/from a local `transactions.json` file
- **Error Handling** Uses .strip()and .upper() to prevent the program from crashing due to random human error
---

## Technologies & Tools Used

- **Language:** Python 3.10+
- **Standard Libraries:**
  - `urllib.request` & `urllib.error` 
  - `json` 
  - **Version Control:** Git & GitHub

---

## Project Structure

```text
CSE VITyarthi_project/
│
├── main.py              # CLI entry point and menu control loop
├── portfolio.py         # Wallet class and core business logic
├── storage.py           # JSON file persistence handler
├── api_handler.py       # API integration and offline fallback logic
├── .gitignore           # Git ignore rules for cache and data files
├── README.md            # Project documentation
└── screenshots/         # Terminal execution screenshots
## Steps to Install & Run

Since I only used built-in Python libraries, there is no need to run any complicated `pip install` commands. You just need Python installed on your computer.

1. Download or clone this project folder to your PC.
2. Open your terminal or command prompt inside the folder.
3. Type `python main.py` and press Enter.

---

## Instructions for Testing

Once the menu pops up in the terminal, here is a quick guide to test all the features:

1. **Deposit Money:** Press `2`. Type a currency like `usd` (you can try typing in lowercase, my code will automatically fix it to uppercase!) and enter an amount like `2500`.
2. **Check Balance:** Press `1`. You should see your updated balance printed out.
3. **Test the Conversion (Withdrawal):** Press `3`. Try withdrawing `200` from `USD` to `INR`. You will see it calculate the 0.02% fee and fetch the live exchange rate. (If your college Wi-Fi is blocking the connection, it will print a warning and safely use my hardcoded backup rates instead).
4. **Test the Save Feature:** Press `4` to exit the program gracefully. This is important because it triggers the save function. If you run `python main.py` again and press `1`, you will see your money is still safely stored there!