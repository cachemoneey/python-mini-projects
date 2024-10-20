# pip/3 install pythonping
from pythonping import ping

def ping_website():
    try:
        url = input("Domain www. ")
        response = ping(url, count=1)
        print(f"{url} responded")
    except:
        print(f"{url} No response")
        
ping_website()