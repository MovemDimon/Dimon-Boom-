from flask_socketio import SocketIO, join_room
from flask import request
from app.models import User
from app.core import db

socketio = SocketIO(cors_allowed_origins=["https://your-domain.com"])


def notify_user(user_id, new_balance):
    socketio.emit(
        "balance_update",
        {"userId": user_id, "newBalance": new_balance},
        room=str(user_id),
    )


@socketio.on("connect")
def handle_connect():
    user_id = request.args.get("userId")
    if user_id:
        join_room(user_id)
