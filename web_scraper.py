# pip/3 install google
from googlesearch import search
import os
import requests
import time

def website_text():
    path = "C:\\Users\\azizurrohman\\Desktop"
    os.chdir(path)
    url = input("Enter full URL: ")
    response = requests.get(url)
    if response.status_code == 200:
        print("All is good!")
        time.sleep(1)
        with open("html.txt", "wb") as file_object:
            file_object.write(response.content)
            print("Stored data in file on desktop.")
            get_site_url()
            
def get_site_url():
    search_query = input("Enter full URL: ")
    results = search(search_query, num=5, stop=5, pause=2)
    for result in results:
        print("URL:: ", result)
        
get_site_url()