Dolls House Flask App
=====================

# Setup - Do this once
http://docs.python-guide.org/en/latest/dev/virtualenvs/
```
pip install virtualenv

cd <the folder where this readme file is>
virtualenv venv
virtualenv -p /usr/bin/python3 venv

source venv/bin/activate
pip install -r requirements.txt
```

# To Run in Debug
```
cd <the folder where this readme file is>
source venv/bin/activate
python app.py

http://localhost:5000
```

# Run with production web server
* Port `8000` by default, can be changed in `run.sh`
```
./run.sh
http://localhost:8000
```