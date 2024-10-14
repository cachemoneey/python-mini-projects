import socket

def get_ip_address():
    try:
        ip = socket.gethostbyname('www.google.com')
        print(f"Domain IP Address is: {ip}")
    except socket.error as e:
        print(f"Error occurred! {e}")
        
get_ip_address()