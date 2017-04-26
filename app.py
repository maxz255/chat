from chatroom import (
    create_app,
    socketio,
)
import config

app = create_app(
    debug=True,
    secret_key=config.secret_key,
)


if __name__ == '__main__':
    socketio.run(app, **config.config)
