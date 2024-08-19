import os
from website import create_app

app = create_app()
with app.app_context():
    # Your code here that needs to run within the app context
    pass # To avoid indentation error
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)