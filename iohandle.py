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

def read():
    with open('PRISONDATA.csv','r') as pD:
        rec = csv.reader(pD)
        for i in rec:
            print(i)
