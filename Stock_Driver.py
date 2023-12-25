"""
The driver for the program
"""

from Stock_Grapher import stock_printer

# Define the file path
file_name = 'Apple.txt'  # Replace with your file's path

with open(file_name, 'r') as file:
    stock_printer(file)

