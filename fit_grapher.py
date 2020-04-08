# fit_grapher.py

import re
import sys
import datetime
import gspread
import matplotlib.pyplot as plt
from oauth2client.service_account import ServiceAccountCredentials


def graphData(workout, d1, d2):

    plt.plot(d1, d2)
    
    plt.xlabel(workout)
    plt.ylabel('Weight')
    
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
    dates = []
    workouts = []
    for c in sheet.findall(crit):

        date = sheet.cell(c.row, c.col-1).value
        workout = re.search(criteria + "\(\d{,3},\s*\d{1},\s*\d{1,2}\)", str(c)).group(0)
        
        weight =  int(workout[workout.find("(")+1 : workout.find(",")])
        dates.append(date)
        workouts.append(weight)
    
    return (dates, workouts)

if __name__ == "__main__":

    if len(sys.argv) == 1:
        print("Error: Arg empty")
    else:
        sheet = getSheet("Fitness Log")
        data = getData(sheet, sys.argv[1])
        graphData(sys.argv[1], data[0], data[1])
    