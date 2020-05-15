import csv
import pickle
import os
import ftplib

Fusr = 'unaux_25781641'
Fhost = 'ftp.unaux.com'
Fpwd = 'FTPxxGulag56'

def receiveData():
    with ftplib.FTP(Fhost, Fusr, Fpwd) as ftp:
        file = 'DATA.bin'

        with open(file, 'wb') as foo:
            f = ftp.retrbinary('RETR '+'/htdocs/DataFiles/'+file, foo.write)

        with open(file,'rb') as oof:
            global li
            li=[]
            a=pickle.load(oof)
            for j in a:
                li.append(j)

        with open("PRISONDATA.csv",'w',newline='') as inp:
            log = csv.writer(inp)
            for i in li:
                log.writerow(i)

def receiveLogs():
    with ftplib.FTP(Fhost, Fusr, Fpwd) as ftp:
        file = 'LOG_DATA.bin'

        with open(file, 'wb') as foo:
            f = ftp.retrbinary('RETR '+'/htdocs/DataFiles/'+file, foo.write)

        with open(file,'rb') as oof:
            global li
            li=[]
            a=pickle.load(oof)
            for j in a:
                li.append(j)

        with open("PrisonLogs.csv",'w',newline='') as inp:
            log = csv.writer(inp)
            for i in li:
                log.writerow(i)


def displayAll():
    receiveData()
    rec=[]
    with open('PRISONDATA.csv') as pD:
        reco=csv.reader(pD)
        for i in reco:
            rec.append(i)
        rec.pop(0)
    return rec

def displayByName(name):
    n = name['Name']
    allRecs=displayAll()
    queriedRecs=[]
    for i in allRecs:
        if n in i[1]:
            queriedRecs.append(i)
    return queriedRecs

def displayByCase(id):
    case=id['Case']
    allRecs=displayAll()
    queriedRecs=[]
    for i in allRecs:
        if i[7] == case:
            queriedRecs.append(i)
    return queriedRecs

def displayByID(id):
    pid=id['ID']
    allRecs=displayAll()
    queriedRecs=[]
    for i in allRecs:
        if i[0] == pid:
            queriedRecs.append(i)
    return queriedRecs
