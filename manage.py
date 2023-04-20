# -*- coding: utf-8 -*-

from app.main import create_app
from app import task_bp, index_bp

app = create_app()
app.register_blueprint(index_bp)
app.register_blueprint(task_bp)

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5050)
