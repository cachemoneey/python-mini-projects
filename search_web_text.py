# pip/3 install requests
import requests

def search_website_text():
    response = requests.get(url)
    if search_text.lower() in response.text.lower():
        print(F" '{search_text}' on the website")
    else:
        print(F" '{search_text}' not found on the website")
    
if __name__ == "__main__":
    url = input("Enter website URL: ")
    search_text = input("Enter text to search: ")
    search_website_text()
