import json
import sqlite3

from flask import Flask, render_template, request, send_from_directory
app = Flask(__name__)


DB_FILE_NAME = 'database.sqlite3'


def get_connection():
    return sqlite3.connect(DB_FILE_NAME)


@app.route('/teams')
def get_teams():
    with get_connection() as conn:
        cursor = conn.cursor()
        teams = cursor.execute('SELECT * FROM `teams`').fetchall()
        teams = {'team-%s' % id: {'id': id, 'name': name, 'laps': laps} for (id, name, laps) in teams}

    return json.dumps(teams)


@app.route('/add_lap', methods=['POST'])
def add_lap():
    print(request.form)
    with get_connection() as conn:
        cursor = conn.cursor()

        team_id, count, time = request.form['team'], 1, request.form['time']

        cursor.execute('SELECT * FROM `laps` WHERE `team_id` = ? AND `time` = ?', (team_id, time))
        if cursor.rowcount > 0:
            return '1'

        cursor.execute('INSERT INTO `laps` (`team_id`, `value`, `time`) VALUES (?, ?, ?)', (team_id, count, time))
        cursor.execute('UPDATE `teams` SET `laps` = `laps` + ? WHERE `id` = ?', (count, team_id))

    return '1'  # App expects 1 to be returned, whatever...


@app.route('/static/<path:path>')
def send_js(path):
    return send_from_directory('static', path)

if __name__ == "__main__":
    app.run()


@app.route('/')
def index():
    return render_template('index.html', teams=get_teams())
