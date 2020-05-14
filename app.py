from flask import Flask, render_template, request, redirect, url_for
import displayrecords as dr
import detailfetch as df
import VerifyCred as VCr
import iohandle as GOD

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/contact')
def contact_page():
    return render_template('contact.html')

@app.route('/app')
def app_page_main():
    return render_template('app.html',value=dr.displayAll())

@app.route('/qByName',methods=['POST'])
def app_queryByName():
    if request.method == 'POST':
        name = request.form
        return render_template('app.html',value=dr.displayByName(name))

@app.route('/qByID',methods=['POST'])
def app_queryById():
    if request.method == 'POST':
        id = request.form
        return render_template('app.html',value=dr.displayByID(id))

@app.route('/qByCase', methods=['POST'])
def app_queryByCase():
    if request.method == 'POST':
        case = request.form
        return render_template('app.html',value=dr.displayByCase(case))

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
        return render_template('detailed.html',p=pid,n=name,a=age,s=gender,h=height,c=contact,r=release,cr=crime)

@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/del',methods=['POST'])
def del_rec():
    if request.method == 'POST':
        pid = request.form['PP_ID']
        e = request.form['usr']
        p = request.form['pswdsd']
        if VCr.verifyCred(e,p):
            GOD.delRec(pid)
            return redirect(url_for('app_page_main'))
        else:
            return redirect(url_for('app_page_main'))

@app.route('/add',methods=['POST'])
def add_rec():
    return redirect(url_for('app_page_main'))

if __name__ == "__main__":
    app.run(debug=True)
