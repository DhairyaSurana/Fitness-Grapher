# fit_grapher.py

import re
import gspread
import matplotlib.pyplot as plt
from oauth2client.service_account import ServiceAccountCredentials


def graphData(workout, d1, d2):

    plt.plot(d1, d2)
    
    plt.xlabel(workout)
    plt.ylabel('some numbers')
    
    plt.title(workout)
    plt.show()

def getSheet(sheet_name):

    # use creds to create a client to interact with the Google Drive API
    scope = ['https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)

    # Find a workbook by name and open the first sheet
    # Make sure you use the right name here.
    sheet = client.open(sheet_name).sheet1

    return sheet

def getData(sheet, criteria):
    
    crit = re.compile(criteria)
    #return sheet.findall(criteria)
    data_dict = {}
    for c in sheet.findall(crit):

        date = sheet.cell(c.row, c.col-1).value
        workout = re.search(criteria + "\(\d{,3},\s*\d{1},\s*\d{1,2}\)", str(c)).group(0)
        
        data_dict[date] = workout
        
    print(data_dict)
    return data_dict
if __name__ == "__main__":

    sheet = getSheet("Fitness Log")
    data = getData(sheet, "asdf")
    # print(sheet.get_all_records())
    #print(getCells(sheet, "chest press"))
    #graphData("bicep curls", [1,1,1,1], [1,2,3,4])