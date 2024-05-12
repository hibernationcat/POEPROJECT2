from flask import Blueprint, jsonify,request,current_app
from models import db,Coordinate
import threading
from pynput import mouse



coordinate_bp = Blueprint('coordinate', __name__)



@coordinate_bp.route('/list')
def list():
    res = db.session.execute(db.text('select * from coordinate')).fetchall()
    res = [i._asdict() for i in res]
    return res


@coordinate_bp.route('/location/<id>')
def location(id):
    print('-----进入方法-----')
    context = current_app.app_context()

    xy= start_listener(id,context)
    return ','.join(map(str, xy))
     





  
# 异步启动监听器
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
                
            listener.stop()  # 停止监听器

    with mouse.Listener(on_click=on_click) as listener:
        listener.join()
    return xy