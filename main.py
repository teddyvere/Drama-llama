import os
import logging
from website import create_app, db
from sqlalchemy import inspect
from website.models import Users, Prompt, Poem

# Create and configure the app
app = create_app()

# Set up logging
logging.basicConfig(level=logging.INFO)


# Inspect the database for the presence of tables
# with app.app_context():
#     try:
#         inspector = inspect(db.engine)
#         table_models = {
#             'users': Users,
#             'prompt': Prompt,
#             'poem': Poem
#         }
        
#         # Create tables if they do not exist
#         for table_name, model_class in table_models.items():
#             if not inspector.has_table(table_name):
#                 model_class.__table__.create(bind=db.engine)
#                 logging.info(f"Created table {table_name}")
#     except Exception as e:
#         logging.error(f"Error inspecting or creating tables: {e}")
with app.app_context():
    db.create_all()


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
