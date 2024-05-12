from flask_sqlalchemy import SQLAlchemy
from flask import Flask


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///poe.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True



db = SQLAlchemy(app)

with app.app_context():
    rest = db.session.execute("select * from coordinate")
    print (rest)
app.run()


