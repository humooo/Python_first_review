#1/bin/bash

sudo apt-get install python3 python3-pip

python3 -m venv venv
source venv/bin/activate

pip freeze > requirements.txt

pip install -r requirements.txt
