
ids = [302,456,278,349,221,107,445]
crimes = ['Murder','Hacking','Drug Trafficking','Robbery','Burglary','Assault on officer','Kidnapping']
pds=[60,25,40,5,3,2,10]

def returnCase(k):
    n = 0
    for i in ids:
        if i == k:
            return crimes[n]
        n += 1

def returnPd(k):
    n = 0
    for i in ids:
        if i == k:
            return pds[n]
        n += 1
