import os
import logging
from website import create_app, db
from sqlalchemy import inspect
from website.models import Users, Prompt, Poem

# Create and configure the app
app = create_app()

# Set up logging
logging.basicConfig(level=logging.INFO)

with app.app_context():
    try:
        # Ensure the database is properly initialized
        db.init_app(app)
        
        # Check database connection
        db.session.execute('SELECT 1')
        logging.info("Database connection successful")
    except Exception as e:
        logging.error("Database connection failed: %s", e)
    
    # Inspect the database for the presence of tables
    inspector = inspect(db.engine)
    table_models = {
        'users': Users,
        'prompt': Prompt,
        'poem': Poem
    }
    
    # Create tables if they do not exist
    for table_name, model_class in table_models.items():
        if not inspector.has_table(table_name):
            model_class.__table__.create(bind=db.engine)
            logging.info(f"Created table {table_name}")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
