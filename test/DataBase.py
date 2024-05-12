import datetime

from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
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
    text
)
from sqlalchemy.ext.declarative import declarative_base



connection_str = f'sqlite:///poe.db'
# SQLAlchemy engine
engine = create_engine(connection_str,isolation_level = 'AUTOCOMMIT')

# 绑定引擎
Session = sessionmaker(bind=engine, )
# 基础类
Base = declarative_base()
# 创建数据库链接池，直接使用session即可为当前线程拿出一个链接对象conn
# 内部会采用threading.local进行隔离
session = scoped_session(Session)




