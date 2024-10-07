import time
import webbrowser

banned_websites = ["https://yahoo.com", "https://bing.com"] # choose the websites you want to block

def open_websites():
    url = input("Enter websote: ")
    if url not in banned_websites:
        webbrowser.open(url)
    else:
        print("Cannot access site, on banned list.")
        update_banned_list()
        
def update_banned_list():
    update_list = input("Add a URL to the blacklist: ")
    banned_websites.append(update_list)
    print("List updated.")
    time.sleep(1)
    open_websites()
    
open_websites()