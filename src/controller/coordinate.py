from flask import Blueprint, jsonify,request,current_app
from models import db,Coordinate
import threading
from pynput import mouse



coordinate_bp = Blueprint('coordinate', __name__)


# 查询坐标列表
@coordinate_bp.route('/list')
def list():
    res = db.session.execute(db.text('select * from coordinate')).fetchall()
    res = [i._asdict() for i in res]
    return res


# 定位坐标 update
@coordinate_bp.route('/location/<id>')
def location(id):
    context = current_app.app_context()
    xy= start_listener(id,context)
    return ','.join(map(str, xy))
     





  
def start_listener(id,context):
    xy = []
    print('开启鼠标监听------')
    def on_click(x, y, button, pressed):
        if pressed:
            nonlocal xy
            xy =[x,y]
            print('Mouse clicked at (x={}, y={})'.format(x, y),"-----")
            with context:
                res = db.session.execute(db.text('select * from coordinate')).fetchall()
                print(res[0])
                db.session.execute(db.text('UPDATE coordinate SET x = :x, y = :y WHERE id = :id'), {'x': str(x), 'y': str(y), 'id': int(id)})
                db.session.commit()
                
            listener.stop() 

    with mouse.Listener(on_click=on_click) as listener:
        listener.join()
    return xy