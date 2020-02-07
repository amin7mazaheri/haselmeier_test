## Installation
follow the below steps: 

```bash
virtualenv -p python3 env
source env/bin/activae 
python manage.py migrate 
python manage.py createsuperuser
username:admin
password:admin
python manage.py runserver 127.0.0.1:8000
```

## Test
run tests(test_views , test_models)
```bass
python manage.py test
```

### Go to the admin panel and add some data for testing 
'''
127.0.0.1:8000/admin/
''' 
### I used sqlite3(default of django as relational database )
## Usage
for using API's log in and receive an access token

### Geting access token:
```bash
curl  -X post http://127.0.0.1:8000/api/token/ -d username=admin -d password=admin

```
Answer is Json with two values refresh and access 
select the access.(this token will expire after 5 min)
refresh is used for getting new access token(refresh will expire after 24 hour)

### Using API's

### Adding new book 
```bash
 curl  -X post http://127.0.0.1:8000/api/book/  -H "Content-Type: application/json ,Authorization: Bearer MYTOKEN"  -d '{"name":"xyz","price":"xyz", "author":"xyz", "publisher":"xyz"}'

```

### Getting list of book 
```bash
 curl  -X get http://127.0.0.1:8000/api/book/  -H "Authorization: Bearer MYTOKEN"

```

### Get detail of book 
```bash
 curl  -X get http://127.0.0.1:8000/api/book/id/  -H "Authorization: Bearer MYTOKEN"

```

### Delete rating
```bash
 curl  -X delete http://127.0.0.1:8000/api/rating/id/  -H "Content-Type: application/json ,Authorization: Bearer MYTOKEN" 

```

### Adding new rating 
```bash
 curl  -X post http://127.0.0.1:8000/api/rating/  -H "Content-Type: application/json ,Authorization: Bearer MYTOKEN"  -d '{"user"="xyz", "book"="xyz", "rating":"yxz"}'

```

### Get list of rating 
```bash
 curl  -X get http://127.0.0.1:8000/api/rating/  -H "Authorization: Bearer MYTOKEN"

```

### Get detail of rating 
```bash
 curl  -X get http://127.0.0.1:8000/api/rating/id/  -H "Authorization: Bearer MYTOKEN"

```

### Delete book of stock
```bash
 curl  -X delete http://127.0.0.1:8000/api/stock/id/  -H "Content-Type: application/json ,Authorization: Bearer MYTOKEN" 

```

### Adding new book to stock 
```bash
 curl  -X post http://127.0.0.1:8000/api/stock/  -H "Content-Type: application/json ,Authorization: Bearer MYTOKEN"  -d '{"book":"xyz","in_stock":"xyz","quantity":"xyz"}'

```

### Get detail of stock
```bash
 curl  -X get http://127.0.0.1:8000/api/stock/id/  -H "Authorization: Bearer MYTOKEN"

```

### Get list of stock
```bash
 curl  -X get http://127.0.0.1:8000/api/stock/  -H "Authorization: Bearer MYTOKEN"

```

## Using of Postam is another option
