# hb-workshop-jsunit

Some code for showing how to use jsunit/karma


## Python functional tests

Use `pytest`. E.g., `py.test test/functional/test_amazon_web.py`.

Or use `pytest-xdist`. E.g., `py.test -n2 --boxed test/functional/test_amazon_web_sauce.py` (two processes in parallel).
