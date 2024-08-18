from website import create_app

app = create_app()
with app.app_context():
    # Your code here that needs to run within the app context
    pass # To avoid indentation error
if __name__ == '__main__':
    app.run(debug=True)