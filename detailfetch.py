import csv
import displayrecords as disr

def RecordsMain():
    return disr.displayAll()

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
