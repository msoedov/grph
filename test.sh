python auto_schema.py > spec.py
# autopep8 -ir spec.py

ls data/*.json | Xargs python auto_schema.py
py.test . -v --doctest-modules
