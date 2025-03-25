# 📊 Simple Tax Calculation App  

This project is a simple tax calculation application built using Python. It follows **Object-Oriented Programming (OOP)** principles to manage orders and calculate tax rates based on total amounts.  

The application is divided into **two sections**:
1. **DataGenerator.py** – Generates sample order data.
2. **SimpleTaxCalculator.py** – Processes tax calculations based on the generated data.

## **DataGenerator.py**
1. Name
- The random name generated with list of first_name & last_name 
- continue by random choice & concated two random choice of it for 100 times
2. Amount
- Each order has a random amount between 1 and 10,000,000
- Since IDR is often represented in thousands, the amount is multiplied by 1,000.
3. Order
- The order number generated with for function for seuqntially numbered from 1 to 100.
4. DateTime
- A random date is assigned to each order, ranging from January 1, 2023, to December 31, 2025.
- The function random_date_time() calculates a random timestamp within the range.

## **SimpleTaxCalculator.py**
This project is a simple tax calculation application built in Python. It follows Object-Oriented Programming (OOP) principles to manage orders and calculate tax rates based on total amounts. The application:
1. Generates random customer orders (ID, name, amount, date).
2. Calculates tax rates (11% or 12%) based on the order amount.
3. Computes total revenue after tax deduction.
4. Displays order details and summarized reports.
