import csv

def RecordsMain():
    rec=[]
    with open('..\static\PRISONDATA.csv') as pD:
        reco=csv.reader(pD)
        for i in reco:
            rec.append(i)
        rec.pop(0)
        rec.pop(-1)
    return rec

def fetchName(pid):
    for i in RecordsMain():
        if i[0]== pid:
            return i[1]

def fetchAge(pid):
    for i in RecordsMain():
        if i[0]== pid:
            return i[2]

def fetchGender(pid):
    for i in RecordsMain():
        if i[0]== pid:
            return i[3]

def fetchHt(pid):
    for i in RecordsMain():
        if i[0]== pid:
            return i[4]

def fetchContact(pid):
    for i in RecordsMain():
        if i[0]== pid:
            return i[5]

def fetchRel(pid):
    for i in RecordsMain():
        if i[0]== pid:
            return i[6]

def fetchCrime(pid):
    for i in RecordsMain():
        if i[0]== pid:
            return i[8]
