import secrets
import string
import csv

def inp():
    n = input("Name: ")
    c = input("Class with section: ")
    return n, c

def securerandomstring(length=8):
    securestr = ''.join(secrets.choice(string.ascii_letters + string.digits) for i in range(length))
    return securestr

def csvv():
    headings = ['name', 'class', 'section', 'token']
    with open("data.csv", "a+", newline='') as file:
        writer = csv.writer(file)
        file.seek(0)
        if file.read() == "":
            writer.writerow(headings)
        name, class_section = inp()
        token = securerandomstring()
        writer.writerow([name, class_section.split()[0], class_section.split()[1], token])
        print("Your token is: ", token)
csvv()

    
    


