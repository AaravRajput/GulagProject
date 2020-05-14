import pickle

global d

def reWrite():
    d = {}
    while True:
        usrn = input("\nEnter Username\n")
        pwd = input("\nEnter Password\n")
        d[usrn]=pwd
        ch=input("\nContinue ? Y/N \n")
        if ch=="N":
            break

def disp():
    for i in d.keys():
        print(i," : ",d.get(i),"\n")


def pickCred():
    with open("GulagCreds.bin",'wb') as pf:
        pickle.dump(d,pf)

def verifyCred(e,p):
    dS={}
    usrn = e
    pwd = p
    with open("GulagCreds.bin",'rb') as pf:
        dR = pickle.load(pf)
        if usrn in dR.keys() and dR[usrn]==pwd:
            return True

def dispCred():
    dRC={}
    li=""
    with open("GulagCreds.bin",'rb') as pf:
        dRC = pickle.load(pf)
        for i in dRC.keys():
            li += (i+" : "+dRC.get(i)+"\n")
        return li
