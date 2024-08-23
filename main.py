import os
import logging
from website import create_app, db

# Create and configure the app
app = create_app()

# Set up logging
logging.basicConfig(level=logging.INFO)


with app.app_context():
    if db != None:
        db.create_all()


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False, use_reloader=False)
