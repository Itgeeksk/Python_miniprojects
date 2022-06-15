# Importing os module
import os.path


#Checking file is present or not 
def checking_file():
    # Checking that file exists or not
    if os.path.exists("Creds.txt"):
        pass
    else:
        # Creating file with write permissions
        file = open("Creds.txt" , "w")
        # Cloing file
        file.close()



# Taking data from user
# Adding to the file
def append_to_file():
    # Opening file with appending permissions
    file = open("Creds.txt" , "a")
    # Taking details to file
    username = str(input("Enter username here: "))
    password = str(input("Entre password here: "))
    site = str(input("Enter the site here: "))
    
    # Writing -- to file to separate 
    file.write("-------------------------------------------------------------------------------------------")
    # Adding new line to file to make in pretty
    file.write("\n")
    # Storing the inputs as a string in variable's
    user = f"Username : {username}"
    pwd = f"Password :{password}"
    st = f"Site : {site}"
    # Writing Stored variables to file 
    file.write(user)
    file.write("\n")
    file.write(pwd)
    file.write("\n")
    file.write(st)
    file.write("\n")
    file.write("--------------------------------------------------------------------------------------------")
    file.write("\n")
    # Closing file
    file.close()


# Reading file
def reading_file():
    # Opening file with read permissions
    file = open("Creds.txt", "r")
    # Reading file data to content varible
    Content = file.read()
    # Closing file
    file.close()
    print(Content)


# Calling functions
check = checking_file()
append = append_to_file()
content = reading_file()