from src.main.server.server import app
from src.models.settings.db_connection_handler import db_connection_handler

if __name__ == "__main__":
    db_connection_handler.connect()
    app.run(
        host="::1",
        port=5000,
        debug=True
    )
