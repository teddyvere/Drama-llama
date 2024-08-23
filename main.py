import os
import logging
import traceback
from website import create_app, db
from sqlalchemy import inspect, text
from website.models import Users, Prompt, Poem

# Create and configure the app
app = create_app()

# Set up logging
logging.basicConfig(level=logging.INFO)



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
