import requests as req
import os
import time 
import sys
import pandas as pan

CWD = os.getcwd()


def save_data(content, getUrl):
        f_ext = os.path.splitext(getUrl)[1]
        
        try:
            if not os.path.isdir('data'):
                os.mkdir(os.path.join(CWD, "data"))
        
        except FileExistsError as e:
            print("File Does Not Exist", e)

        
        path = os.path.join(CWD, "data")

        if f_ext == ".csv":
            with open(os.path.join(path, "Tennis_Data" + f_ext), "wb") as file:
                file.write(content)
            file.close()
        
        elif f_ext == ".xls":
            with open(os.path.join(path, "Tennis_Data" + f_ext), "wb") as file:
                file.write(content)
            file.close()

def get_data(url):
    try:
        data = req.get(url)
        if data.status_code == 200:
            content = data.content
            save_data(content, url)
        else:
            sys.exit("Invalid URL Try again! \nStatus Code: {}".format(data.status_code))

    except req.exceptions.Timeout as timeOut:
        time.sleep(5)

        try:
            data = req.get(url)
            content = data.content
            save_data(content, url)

        except req.exceptions.Timeout as timeOut:
            sys.exit("Time Out try again later", timeOut)

    except req.exceptions.InvalidURL as invurl:
        sys.exit("Invalid URL", invurl)

    except req.exceptions.HTTPError as httpErr:
        sys.exit("Client not Availble", httpErr)

        



def import_data():
    for root, dirs, files in os.walk(CWD):
        for Files in files:
            try:
                found = Files.find("Tennis_Data")
                if found != -1:
                    break
            except:
                print("File Not Found!")
    path = root
    tennis = pan.read_excel(os.path.join(path, "Tennis_Data.xls"))
    print(tennis.head(5))

if __name__ == "__main__":
    try:
        url = sys.argv[1]
    except IndexError as e:
        sys.exit("Please Provide URL")
    # url = "http://tennis-data.co.uk/2011/2011.xls"
    if url == "":
        print("URL is not included")
    else:
        get_data(url)
        import_data()