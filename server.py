from flask import Flask, render_template, request, redirect, flash, session, jsonify, json

app = Flask(__name__)

@app.route("/")
@app.route('/home')
def view_home():

    return render_template('home.html')


@app.route("/about")
def view_about():

    return render_template('about.html')

@app.route("/linktree")
def view_linktree():

    return render_template('linktree.html')

@app.route("/projects")
def view_projects():

    return render_template('projects.html')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
