# pip/3 install google
from googlesearch import search
import os

def google_search():
    path = "C:\\Users\\azizurrohman\\Desktop"
    os.chdir(path)
    search_query = input("Enter URL: ")
    results = search(search_query, num=3, stop=3, pause=2)
    for result in results:
        with open("url.txt", "a") as file_object:
            file_object.write(result + "\n")
            print("File has been created.")
            
google_search()