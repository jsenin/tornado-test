#Tornado web server test demo

Based on tornadoweb test documentation
http://www.tornadoweb.org/en/stable/testing.html

## install 
```
sudo apt-get install --yes python3 python3-dev python3-pip python-virtualenv
virtualenv -p /usr/bin/python3 venv
source venv/bin/activate
pip install pip --upgrade
pip install -r requirements.txt --upgrade
```

## execute 
run test
```
python -m unittest test_tornado_hello.py 
```
