import csv

def displayAll():
    rec=[]
    with open('..\static\PRISONDATA.csv') as pD:
        reco=csv.reader(pD)
        for i in reco:
            rec.append(i)
        rec.pop(0)
        rec.pop(-1)
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
