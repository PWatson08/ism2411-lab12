#Author : Patrick Watson
#Lab 12 -

import csv
from datetime import datetime

SALES_FILE = "sales.csv"
CLEANED_FILE = "data/cleaned_sales.csv"
LOG_FILE = "data/run_log.txt"

print("---Exercise 1---")
with open(SALES_FILE, "r") as f:
    print(f"Opened {SALES_FILE}.")

print("---Exercise 2---")

with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)



#Reflection 1: []
#Reflection 2: []
