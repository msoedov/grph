python auto_schema.py > spec.py
python auto_schema.py data/test.json > data/test.py
autopep8 -ir data/test.py

# ls data/*.json | Xargs python auto_schema.py
py.test -vvv -q -s . --doctest-modules
python test_spec.py