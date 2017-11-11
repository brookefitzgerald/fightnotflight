from flask import Flask, request, url_for, render_template

app = Flask(__name__)
app.secret_key = 'This is really unique and secret'

@app.route('/')
def hello_person():
    return """
        <p>What game are you playing?</p>
        <form method="POST" action="%s"><input name="person" /><input type="submit" value="Go!" /></form>
        """ % (url_for('play'),)

@app.route('/play', methods=['POST'])
def play():
    return render_template("index.html", name=form.person['Post'])
