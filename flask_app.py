from flask import Flask, request, url_for, render_template, redirect

app = Flask(__name__)
app.secret_key = 'This is really unique and secret'
app.config["DEBUG"] = True

games = {}

@app.route('/')
def start():
    #if request.method=='POST':
    #    return redirect(url_for('play'))
    return render_template('start.html', )

@app.route('/play', methods=['POST'])
def play():
    gameid = request.form['gameid']
    username = request.form['username']
    player = 0
    template = "play.html"
    message = ""
    if gameid in games:
        if games[gameid]['p1']==None:
            games[gameid]['p1'] = username
            player=1
        elif games[gameid]['p2']==None:
            games[gameid]['p2'] = username
            player=2
        else:
            template = "error.html"
            message = "No open player spots! Choose another game."
    else:
        games[gameid]={
            "p1": username,
            "p2": None
        }
        player=1
    return render_template(template, gameid=gameid, username=username, player=player, message=message)



