from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/about')
def app_page():
    return render_template('about.html')

@app.route('/app')
def about_page():
    return render_template('app.html')


if __name__ == "__main__":
    app.run(debug=True)
