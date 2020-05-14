import LegalBounds as LB
from datetime import date
import csv
import os


def delRec(id):
    with open('PRISONDATA.csv','r') as pD:
        rec = csv.reader(pD)
        with open('gulag.csv','w',newline="") as gulag:
            log = csv.writer(gulag)
            for i in rec:
                if not i[0]==id:
                    log.writerow(i)
    with open('gulag.csv','r') as ungulag:
        unrec = csv.reader(ungulag)
        with open('PRISONDATA.csv','w',newline="") as unpD:
            log = csv.writer(unpD)
            for j in unrec:
                log.writerow(j)
    os.remove('gulag.csv')


def addRec(n,a,g,h,c,dy,C):
    with open("PRISONDATA.csv",'r') as pIn:
        csv_loader = csv.reader(pIn)
        P_ID = 0
        pids = []
        for i in csv_loader:
            pids.append(i)
        pids.pop(0)
        for i in pids:
            P_ID = i[0]

    with open("PRISONDATA.csv",'a',newline='') as pOut:
        csv_console = csv.writer(pOut, delimiter=',')
        Name = n
        Age = a
        Sex = g
        Ht = h
        Contact = c
        d = int(dy[-2:])
        m = int(dy[-5:-3])
        y = int(dy[:4])
        CID = C
        Case = LB.returnCase(int(C))
        pD = LB.returnPd(int(C))
        Rel = str(date(day = d, month = m, year = y + pD))

        row=[int(P_ID)+1,Name,Age,Sex,Ht,Contact,Rel,CID,Case]

        csv_console.writerow(row)

    return True
