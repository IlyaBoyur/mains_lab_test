# mains_lab_test
DRF endpoints to parse Excel

---

### Install requirements
```shell
pip install -r requirements.txt
```

---

### Start project
```shell
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
