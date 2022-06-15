import requests
from bs4 import BeautifulSoup as BS
from bs4 import Comment

# Requesting page from the server
url = input("Entre url here: ")
page = requests.get(url)

# Reading page with beautiful soup
soup = BS(page.content , "html.parser")


# **** EXTRACTING LINKS FROM THE SITE *****
# Opening the file link.txt 
link_file = open("link.txt", "w")
# Getting all <a> attributes from the page 
links = soup.find_all("a")
# Looping through the attributes and getting url from the attributes
for link in links:
    # Writing loop output in the file
    link_file.write(link.get("href"))
    link_file.write("\n")
# Closing file
link_file.close()


#  **** EXTRACTING ALL THE TAGS FROM THE SITE **** 
# Opening tags file.txt to store tags
tags = open("tag_file.txt" , "w")
# looping through all the tags
for tag in soup.find_all(True):
    tags.write(tag.name)
    tags.write("\n")
# Closing file here
tags.close()




# **** EXTRACTING TEXT FROM THE SITE ****
# Opening file here
cmt_file = open("comments.txt" , "w")
# getting comments by using lambda and bs4 comment module
comments = soup.find_all(string = lambda text : isinstance(text, Comment))
# looping through all comments
for c in comments:
    cmt_file.write(c)
    cmt_file.write("\n")
cmt_file.close()


#  **** EXTRACTING TEXT FROM THE SITE ****
# Opening a text_file.txt with writing premissions
# we are saving text in the file so we using encoding utf 8 to save everything in normal text
string = open("text.txt" , "w", encoding="utf-8")
# looping through the strings
text = soup.get_text()
string.write(text)
# writing string in text_file.txt
# closing text file here
string.close()
