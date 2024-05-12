from DataBase import session ,text,Base


from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Enum,
    DECIMAL,
    DateTime,
    Boolean,
    UniqueConstraint,
    Index,
    text,
    func
)
# Base = db.Model

class Coordinate(Base):
    __tablename__ = 'coordinate'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    x = Column(String, nullable=False,default = 0 )
    y = Column(String, nullable=False,default = 0 )
    type = Column(String,default='0')
    is_delete = Column(Integer,default='0')
    update_time = Column(DateTime, default=func.now())

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.db.Columns}

# class Entry(Base):
#     __tablename__ = 'entry'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String, nullable=False)
#     value = db.Column(db.String, nullable=False)
#     type = db.Column(db.String,default='0')
#     is_delete = db.Column(db.String,default='0')
#     update_time = db.Column(db.DateTime, default=db.func.now()) 




# def addBaseCoordinate():
#     initName = ['被强化物品','蜕变石','增幅石','改造石','重铸石','富豪石','门']
#     initDatas = [Coordinate(name = i ) for i in initName]
#     db.session.add_all(initDatas)



rest = session.execute(text("select * from coordinate"))
print(rest)