from flask import Flask, render_template, url_for, request, session, redirect, g, jsonify

app = Flask(__name__)
app.secret_key='d7afcbc8d55d6266483a4d1f2b6ee8599e2543b45f3c4c2d'

@app.route('/')
def index():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=False)