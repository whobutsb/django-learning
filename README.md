# Django Learning

## Commands

### Creation Commands

- Create Project: `python3 manage.py startproject [project-name]`

- Create App: `python3 manage.py startapp [app-name]`

- Create superuser: `python3 manage.py createsuperuser`

### Migrations

- Show migrations: `python3 manage.py showmigrations`

- Create a migration based on the models: `python3 manage.py makemigrations [app-name]`

- Run the migration on the database: `python3 manage.py migrate [app-name]`
http://interactivepython.org/courselib/static/pythonds/Trees/TreeTraversals.html
## Learn

- Setup View Class

- Learn Tree Traversal 

http://interactivepython.org/courselib/static/pythonds/Trees/TreeTraversals.html
https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/

## Questions

- How to setup multiple databases for projects

## Debugging

Raise an Exception to print out the results:
```
import sys
raise Exception(sys.path)
```

Get the dictionary of the object: `Model.__dict__`
