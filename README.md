# AirBnB clone - MySQL
The goal of the project is to deploy on server a simple copy of the AirBnB website. 
This includes command interpreter to manipulate data without a visual interface, 
like in a Shell.

## Features
- Create data modal
- Manage (create, update, destroy, e.t.c) object via console / command interpreter
- Store and persist objects to a file (JSON file).

---

## Background Context
Environment variables to create:
- ```HBNB_ENV```: running environment. It can be “dev” or “test” for the moment (“production” soon!)
- ```HBNB_MYSQL_USER```: the username of your MySQL
- ```HBNB_MYSQL_PWD```: the password of your MySQL
- ```HBNB_MYSQL_HOST```: the hostname of your MySQL
- ```HBNB_MYSQL_DB```: the database name of your MySQL
- ```HBNB_TYPE_STORAGE```: the type of storage used. It can be “file” (using FileStorage) or db (using DBStorage)

## Execution
Interactive Mode:
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

Non-interactive mode:
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
---



## Contributor
- Mikearoworade (Michael Aroworade)

