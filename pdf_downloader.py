import requests

def download_pdf():
    url_pdf = input("Enter full url: ")
    saved_download = "C:\\Users\\azizurrohman\\Desktop\\downloaded.pdf" # location where you want the PDF to be downloaded and rename PDF as you like
    response = requests.get(url_pdf)
    if response.status_code == 200:
        print("Downloading PDF Please Wait...")
        with open(saved_download, "wb") as file_object:
            file_object.write(response.content)
            print(f"Content downloaded to {saved_download}")
    else:
        print("Couldn't download file.")
        
download_pdf()