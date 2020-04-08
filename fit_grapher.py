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

def getData(sheet_name):

    # use creds to create a client to interact with the Google Drive API
    scope = ['https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)

    # Find a workbook by name and open the first sheet
    # Make sure you use the right name here.
    sheet = client.open(sheet_name).sheet1

    return sheet

def getCells(sheet, criteria):
    
    criteria = re.compile(r'chest press')
    return sheet.findall(criteria)

if __name__ == "__main__":

    # sheet = getData("Fitness Log")
    # print(sheet.get_all_records())
    # print(getCells(sheet, "chest press"))
    graphData("bicep curls", [1,1,1,1], [1,2,3,4])