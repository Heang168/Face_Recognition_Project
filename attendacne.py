from datetime import datetime
import pandas as pd

def markAttendance(name, acc):
    x = pd.read_csv('attendance.csv')
    with open('attendance.csv', 'r+') as f:
        x = pd.read_csv('attendance.csv')
        myDataList = f.readline()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
                y = name in x['name'].unique()
                if(y != True):
                    now = datetime.now()
                    dtString = now.strftime('%H:%M:%S')
                    f.writelines(f'\n{name}, {dtString}, {acc}')