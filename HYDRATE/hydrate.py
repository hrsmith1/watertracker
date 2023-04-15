from flask import Flask, render_template, g
import sqlite3

hydrate = Flask(__name__)

def get_db():
    create = """CREATE TABLE IF NOT EXISTS tracker(
email TEXT UNIQUE NOT NULL,
name TEXT NOT NULL,
password TEXT NOT NULL,
week TEXT DEFAULT ("0|0|0|0|0|0|0"),
total REAL DEFAULT (0),
avg REAL DEFAULT (0),
createTS datetime NOT NULL CONSTRAINT createTS_DF DEFAULT CURRENT_TIMESTAMP,
updateTS datetime,
PRIMARY KEY email
)"""

    g.db = sqlite3.connect('database.db')
    g.db.row_factory = sqlite3.Row
    g.db.execute(create)
    return g.db

@hydrate.teardown_appcontext
def close_db(exception):
    db = g.pop('db', None)
    if db is not None:
        db.close()

@hydrate.route('/', methods=('GET', 'POST'))
def hello():
    db = get_db()

    if request.method == 'POST':
        db.execute('INSERT INTO tracker (email)')

    return render_template('login.html', name='name')

@hydrate.route('/', methods=('GET', 'POST'))
def home():
    return render_template('home.html')

@hydrate.route('/login', methods=('GET', 'POST'))
def login():
    return render_template('login.html')

@hydrate.route('/register', methods=('GET', 'POST'))
def login():
    return render_template('register.html')

@hydrate.route('/login', methods=('GET', 'POST'))
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run()