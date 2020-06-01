from app import app, socketio
from gevent import monkey; monkey.patch_all()

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5555, use_reloader=False, debug=True)
