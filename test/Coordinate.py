from flask import Blueprint, jsonify
from main import db

coordinate_bp = Blueprint('coordinate', __name__)




@coordinate_bp.route('/list22')
def list():
    result = db.session.execute(db.text("select * from coordinate"))
    # print(result)
    return "123"
    # # 执行原生 SQL 查询
    # result = db.session.execute(db.text("select * from coordinate where is_delete = 0")).fetchall()
    # # 获取列名
    # columns = result[0].keys() if result else []
    # print(columns)

