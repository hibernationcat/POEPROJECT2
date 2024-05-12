from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
Base = db.Model


# class BaseModel(Base):
#     _abstract_ = True
#     def serialize(self):
#         result = dict()
#         return {result[c.key]:getattr(self, c.key) for c in inspect(self).mapper.column_attrs}

class Coordinate(Base):
    __tablename__ = 'coordinate'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    x = db.Column(db.String, nullable=False,default = 0 )
    y = db.Column(db.String, nullable=False,default = 0 )
    type = db.Column(db.String,default='0')
    is_delete = db.Column(db.Integer,default='0')
    update_time = db.Column(db.DateTime, default=db.func.now())

    def to_dict(self):
        return {'id':self.id,'name':self.name,'x':self.x,"y":self.y,'type':self.type}



class Entry(Base):
    __tablename__ = 'entry'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    value = db.Column(db.String, nullable=False)
    type = db.Column(db.String,default='0')
    is_delete = db.Column(db.String,default='0')
    update_time = db.Column(db.DateTime, default=db.func.now()) 




def addBaseCoordinate():
    initName = ['被强化物品','蜕变石','增幅石','改造石','重铸石','富豪石','门']
    initDatas = [Coordinate(name = i ) for i in initName]
    db.session.add_all(initDatas)
    db.session.commit()



