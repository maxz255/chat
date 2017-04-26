from flask import session
from flask_socketio import (
    emit,
    join_room,
    leave_room,
)
from .. import socketio
from cache import RedisCache
import time
import json


cache = RedisCache()


@socketio.on('joined', namespace='/chat')
def joined(message):
    room = message['msg']
    join_room(room)
    session['room'] = room
    msg_record = [json.loads(cache.get(k).decode('utf-8')) for k in cache.sort()]
    msg_record = [m for m in msg_record if m['room'] == room]
    data = {
        'time': int(time.time()),
        'msg': session.get('name') + '加入了' + session.get('room'),
    }
    emit('record', msg_record, room=room)
    emit('status', data, room=room)


@socketio.on('text', namespace='/chat')
def text(message):
    room = message.get('room')
    data = {
        'time': int(time.time()),
        'name': session.get('name'),
        'msg': message['msg'],
        'room': room,
    }
    cache.set(time.time(), json.dumps(data))
    emit('message', data, room=room)


@socketio.on('left', namespace='/chat')
def left(message):
    room = session.get('room')
    session.pop('room')
    leave_room(room)
    data = {
        'time': int(time.time()),
        'msg': session.get('name') + '离开了房间',
    }
    emit('status', data, room=room)
