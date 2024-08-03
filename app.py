from flask import Flask, render_template, request
from schedule import get_team_schedule

app = Flask(__name__)

@app.route('/')
def home():
    teams = [
        'Cardinals', 'Falcons', 'Ravens', 'Bills', 'Panthers', 'Bears', 
        'Bengals', 'Browns', 'Cowboys', 'Broncos', 'Lions', 'Packers', 
        'Texans', 'Colts', 'Jaguars', 'Chiefs', 'Raiders', 'Chargers', 
        'Rams', 'Dolphins', 'Vikings', 'Patriots', 'Saints', 'Giants', 
        'Jets', 'Eagles', 'Steelers', '49ers', 'Seahawks', 'Buccaneers', 
        'Titans', 'Washington'
    ]
    return render_template('home.html', teams=teams)

@app.route('/team/<team_name>')
def team_schedule(team_name):
    schedule = get_team_schedule(team_name)
    return render_template('team_schedule.html', team_name=team_name, schedule=schedule)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
