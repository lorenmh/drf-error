# cd to this dir
cd ${0%/*}

virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py shell < error.py
