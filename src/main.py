from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import db,addBaseCoordinate
from controller.coordinate import coordinate_bp


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///poe.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.ensure_ascii = False
db.init_app(app)

app.register_blueprint(coordinate_bp, url_prefix='/coordinate')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        # addBaseCoordinate()
    app.run()