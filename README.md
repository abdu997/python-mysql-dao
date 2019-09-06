# python-mysql-dao
This script abstracts python execute code from 5-10 lines to 1 general line of code.

## Requirments
* Python 3.x

## Install
```sh
$ pip3 install -r requirments.txt
```

## Setup
Create a `config.py` and insert the bottom code, with your database credentials. This file is git ignored, you will have to create this file for every environment setup.

```python
MYSQL = {
    "host": "localhost",
    "user": "user_name",
    "passwd": "",
    "database": "database_name"
}
```

## Example
```python
from db import fetchone, fetchall, execute, executemany

""" Fetches one row, and returns it as a dict. """"
fetchone("SELECT * FROM customers WHERE customer_id = '1'")

""" Fetches all row results from a query, returns a set of dicts. """
fetchall("SELECT * FROM customers")

""" Executes a single query, returns the MySQL cursor. """
execute("INSERT INTO customers(name, age) VALUES("John", 2)")

""" Executes multiple queries, returns the MySQL cursor. """
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
executemany(sql, val)

```
