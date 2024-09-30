import csv
import gspread # pip install gspread
# Must use Google Sheets API using docs
import time

MONTH = 'May' # Choose your month

file = F"hsbc_{MONTH}.csv" # Enter the beginning of the file name off your personal bank

transactions = []

SUBSCRIPTION_NAMES = {} # Enter your subscriptions

sum = 0

def hsbcFin(file, SUBSCRIPTION_NAMES):

    with open(file, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            date = row[0]
            name = row[1]
            amount = float(row[2])
            sum += amount
            category = 'other'
            if name == "O2":
                category = 'PHONE BILL'
            if name in "SUBSCRIPTION_NAMES":
                category = "SUBSCRIPTION"
            transaction = ((date, name, amount, category))
            print(transaction)
            transactions.append(transaction)
        return transactions

sa = gspread.service_account()
sh = sa.open("Personal Finances")

wks = sh.worksheet(f"{MONTH}")

rows = hsbcFin(file, SUBSCRIPTION_NAMES)

for row in rows:
    wks.insert_row([row[0], row[1], row[3], row[2], 8])
    time.sleep(2)
    
wks.insert_row([1,2,3], 10)