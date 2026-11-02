from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/places')
def places():
    return render_template('places.html')


@app.route('/tips')
def tips():
    return render_template('tips.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
