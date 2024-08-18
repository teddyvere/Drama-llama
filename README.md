# setup venv
python3 -m venv venv
source venv/bin/activate  

# install libraries 

pip3 install Flask --break-system-packages

pip3 install flask_login --break-system-packages

pip install mysqlclient --break-system-packages





# Run main App
python3 main.py