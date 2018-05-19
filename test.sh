set -e
python auto_schema.py data/github.json > data/gh.py
python auto_schema.py data/test.json > data/test.py
python auto_schema.py data/ph.json > data/ph.py
python auto_schema.py data/leecode.json > data/leecode.py
black data/test.py
black data/leecode.py
black data/ph.py
black data/gh.py

py.test -vvv -q -s . --doctest-modules
python test_spec.py

py.test -vv -s gclient.py