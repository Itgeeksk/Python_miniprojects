import os
import os.path

def save(text):
    if os.path.exists('notes.txt'):
        print('File saved to an existing file named notes.txt')
    else:
        file = open("notes.txt",'a')
        file.write(text)
        file.close()

def new_file(note):
    file_name = input("Enter file name: ")
    file  = open(file_name,'w')
    file.write(note)
    file.close()
    print(f"Your file is save in {os.getcwd()} by name {file_name}")



data = input("Write you notes here: \n")

want_to_do = input("Do you want to save the file or make a new one for new one enter n or for save to existing file enter s : ").lower()
if want_to_do == "y":
    save(data)
if want_to_do == 'n':
    new_file(data)