import os
import webbrowser
import time

my_path = "C:\\Users\\azizurrohman\\Desktop"
os.chdir(my_path)
time.sleep(1)
print("Path changed to: {}".format(my_path))

def search_click_link():
    open_file = input("Enter file to open: ")
    click_link = input("Enter link to click: ")
    with open(open_file, "r") as file_object:
        file_content = file_object.read()
        if click_link in file_content:
            webbrowser.open(click_link)
            print(f"Opening link: {click_link}")
        else:
            print(f"Error: '{click_link}' does not exist.")
    
search_click_link()
