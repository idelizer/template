from flask import Flask, render_template, request, redirect, flash, session, jsonify, json

app = Flask(__name__)

@app.route("/")
@app.route('/home')
def view_home():

    return render_template('home.html')


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
