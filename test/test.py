from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///poe.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)


class Coordinate(db.Model):
    __tablename__ = 'coordinate'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    x = db.Column(db.String, nullable=False,default = 0 )
    y = db.Column(db.String, nullable=False,default = 0 )
    type = db.Column(db.String,default='0')
    is_delete = db.Column(db.Integer,default='0')
    update_time = db.Column(db.DateTime, default=db.func.now())


@app.route('/list')
def shutdown_session(exception=None):
    initName = ['被强化物品','蜕变石','增幅石','改造石','重铸石','富豪石','门']
    initDatas = [Coordinate(name = i ) for i in initName]
    db.session.add_all(initDatas)


