from datetime import date
from flask import Flask, render_template, request, redirect, url_for
import displayrecords as dr
import detailfetch as df
import VerifyCred as VCr
import iohandle as GOD

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html',bg="GulagHome")

@app.route('/contact')
def contact_page():
    return render_template('contact.html',bg="GulagOffice")

@app.route('/app')
def app_page_main():
    return render_template('app.html',value=dr.displayAll(),bg="TheGulag")

@app.route('/raw',methods=['POST'])
def app_raw_data():
    if request.method == 'POST':
        return render_template('raw.html',value=dr.displayAll())

@app.route('/qByName',methods=['POST'])
def app_queryByName():
    if request.method == 'POST':
        name = request.form
        return redirect('app.html',value=dr.displayByName(name),bg="TheGulag")

@app.route('/qByID',methods=['POST'])
def app_queryById():
    if request.method == 'POST':
        id = request.form
        return render_template('app.html',value=dr.displayByID(id),bg="TheGulag")

@app.route('/qByCase', methods=['POST'])
def app_queryByCase():
    if request.method == 'POST':
        case = request.form
        return render_template('app.html',value=dr.displayByCase(case),bg="TheGulag")

@app.route('/details', methods=['POST'])
def app_dispplayDetails():
    if request.method == 'POST':
        pid = request.form['P_ID']
        name = df.fetchName(pid)
        age = df.fetchAge(pid)
        gender = df.fetchGender(pid)
        height = df.fetchHt(pid)
        contact = df.fetchContact(pid)
        release = df.fetchRel(pid)
        crime = df.fetchCrime(pid)
        return render_template('detailed.html',p=pid,n=name,a=age,s=gender,h=height,c=contact,r=release,cr=crime,bg="TheGulag")

@app.route('/about')
def about_page():
    return render_template('about.html',bg="GulagOffice")

@app.route('/del',methods=['POST'])
def del_rec():
    if request.method == 'POST':
        pid = request.form['PP_ID']
        u = request.form['usr']
        p = request.form['pswdsd']
        if VCr.verifyCred(u,p):
            GOD.delRec(pid,u)
            return redirect(url_for('app_page_main'))
        else:
            return redirect(url_for('app_page_main'))

@app.route('/add',methods=['POST'])
def add_rec():
    if request.method == 'POST':
        if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
            o = (request.environ['REMOTE_ADDR'])
        else:
            o = (request.environ['HTTP_X_FORWARDED_FOR'])
        n = request.form['P-name']
        a = int(request.form['P-age'])
        g = request.form['Gender']
        h = int(request.form['Ht'])
        c = int(request.form['Contact'])
        d = request.form['Date']
        C = request.form['Crime']
        GOD.addRec(n,a,g,h,c,d,C,o)
        return redirect(url_for('app_page_main'))

@app.route('/modlog',methods=['POST'])
def view_modlog():
    if request.method == 'POST':
        u = request.form['devusr']
        p = request.form['pswdwd']
        if VCr.verifyCred(u,p):
            dr.receiveLogs()
            return render_template('modlogs.html',log=GOD.viewLogs())
        else:
            return redirect(url_for('app_page_main'))


if __name__ == "__main__":
    app.run(debug=True)
