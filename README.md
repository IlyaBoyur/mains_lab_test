# mains_lab_test
DRF endpoints to parse Excel

---

### Technologies
Python 3, Django 4, Django Rest Framework 3.13, SQLite

---

### Install requirements
```shell
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

### Start project
```shell
python backend/manage.py migrate
python backend/manage.py runserver
```

---

### Test Endpoints

#### POST -> /parse_bills/ - to start bill parsing (local 'bills.xlsx' file)
#### GET -> /bills/

Filtering via path variables:
* client_name - by client`s name
* client_org - by client`s organisation

### Author
[Ilya Boyur](https://github.com/IlyaBoyur)
