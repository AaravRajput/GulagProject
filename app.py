from flask import Flask, render_template
import csv

app = Flask(__name__)

def readTable():
    rec=[]
    with open('PRISONDATA.csv') as pD:
        reco=csv.reader(pD)
        for i in reco:
            rec.append(i)
        rec.pop(0)
        rec.pop(-1)
    return rec

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/contact')
def contact_page():
    return render_template('contact.html')

@app.route('/app')
def app_page():
    return render_template('app.html',value=readTable())

@app.route('/about')
def about_page():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)
