from flask import Flask, request, url_for, render_template, redirect

app = Flask(__name__)
app.secret_key = 'This is really unique and secret'
app.config["DEBUG"] = True

games = {}
position = 0

@app.route('/', methods=["GET", "POST"])
def start():
    if request.method == "POST":
        return redirect(url_for('play', gameid=request.form.get('gameid'),username = request.form.get('username')),code=307)
    else:
        return render_template('pickgame.html', )

@app.route('/play', methods=["GET", "POST"])
def play():
    gameid = request.form.get('gameid')
    username = request.form.get('username')
    player = 0
    if gameid in games:
        if games[gameid]['p1']==None:
            games[gameid]['p1'] = username
            player=1
        elif games[gameid]['p2']==None:
            games[gameid]['p2'] = username
            player=2
    else:
        games[gameid]={
            "p1": username,
            "p2": None
        }
        player=1

    return render_template("play.html", gameid=gameid, username=username, player=player)



