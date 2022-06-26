import re
import requests


url = input("Enter the url here: ")
try:
    page = requests.get(url)
    for line in page:
        print(line.decode().strip())
except:
    print("[This is our error which will prompted when client didn't get any response]Server seems to down right at the moment so we need to wait a while.")