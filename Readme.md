# GRPH

Generate a python client code from graphql spec

### Usage

```python
python -m grph examples/github.json > examples/github_lib.py
```

```python
from grph.http import guery

import examples.github_lib as gh


def endpoint(q):
    return guery(q, port=443, sufix="/beta/betausers")


def test_gh():
    q = gh.query.repository(owner="foo", repo="bar")
    print(endpoint(q))

    q = gh.query.user(name="bar")
    print(endpoint(q))

test_gh()
```
