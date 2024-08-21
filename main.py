import os
from website import create_app, db
from sqlalchemy import inspect
from website.models import User, Prompt, Poem

app = create_app()
with app.app_context():
    inspector = inspect(db.engine)
    # Map model classes to table names
    table_models = {
        'user': User,
        'prompt': Prompt,
        'poem': Poem
    }
    for table_name, model_class in table_models.items():
        if not inspector.has_table(table_name):
            model_class.__table__.create(bind=db.engine)
            
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
