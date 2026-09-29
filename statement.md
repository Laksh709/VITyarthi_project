# Project Statement & Declaration of Originality

**Project:** Live Currency Converter & Portfolio CLI  
**Author:** Laksh Vikas Sinha   
**Registration number:** 26BEC10038 

## Declaration
I hereby declare that this project and the accompanying Python source code are my own original work. All the core business logic, Object-Oriented Programming (OOP) structures, and file-handling mechanisms were written and tested by me for this course submission. 

Where I used external resources (like the live exchange rate API), they have been properly credited below.

## Project Reflection
Building this CLI programme for this project was a massive learning experience. Going from writing simple, single-file scripts to actually splitting my code across multiple modules (`main.py`, `portfolio.py`, `api_handler.py`, etc.) really helped me understand why Object-Oriented Programming is so useful and helped me get a strong grasp on object oriented programming and how it is used in real world. By using the `Wallet` class and keeping the dictionary private, I finally understood how encapsulation protects data from getting accidentally deleted. And also learned abstraction so that the user can only see the four main functions of the programme without ever needing to tangle with the code eunning behind. I did this by making a module named main.py.

The biggest challenge by far was handling the live API. I spent a lot of time just trying to figure out why my network was blocking the requests. Fixing it by writing a `try-except` block that automatically falls back to an offline dictionary is probably the part of the code I am most proud of, because it feels like a real-world solution to a frustrating problem. I also learned a lot about sanitizing inputs—adding `.strip().upper()` saved my program from crashing so many times during testing.

## Acknowledgments
* **Exchange Rate API:** I used the free endpoint from `api.exchangerate-api.com` because it is lightweight and didn't require complex authentication headers.
* **Libraries:** I intentionally stuck to Python's built-in standard libraries (`urllib.request`, `json`) so the project wouldn't require any external `pip` installations to run.

Thank you for reviewing my project!