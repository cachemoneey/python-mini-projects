import os
import time
import calendar

def calendar1():
    this_year = 2024
    this_month = 10
    
    this_year = int(input("Enter year: "))
    this_month = int(input("Enter month: "))
    
    print(calendar.month(this_year, this_month))
    
calendar1()
                     