import os
from website import create_app, db
from sqlalchemy import inspect


app = create_app()
with app.app_context():
    inspector = inspect(db.engine)
    if not inspector.has_table('user'):
        db.create_all()
    pass 
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port,debug=True)