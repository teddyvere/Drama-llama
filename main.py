import os

from flask import logging
from website import create_app, db
from sqlalchemy import inspect
from website.models import Users, Prompt, Poem

app = create_app()

with app.app_context():
    try:
        # Check database connection
        db.engine.execute('SELECT 1')
        logging.info("Database connection successful")
    except Exception as e:
        logging.error("Database connection failed: %s", e)
    
    inspector = inspect(db.engine)
    table_models = {
        'users': Users,
        'prompt': Prompt,
        'poem': Poem
    }
    for table_name, model_class in table_models.items():
        if not inspector.has_table(table_name):
            model_class.__table__.create(bind=db.engine)
            
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
