# hb-workshop

Some code for showing JavaScript unit testing (with Jasmine and Karma) and 
Python functional tests (with PyUnit and PyUnit).

## JavaScript unit tests

Install `gulp` globally

```shell
npm install -g gulp
```

Then install the dependencies

```shell
npm install
```

Run `Karma` in a separate window

```shell
karma start local.karma.conf.js
```

This will, by default, run karma on "watch", waiting for changed files.

To run the tests on Sauce Labs, use
```shell
karma start sauce.karma.conf.js
```

This will run the tests once on Sauce Labs, and exit.

## Python functional tests

Install the required libraries

```shell
pip install -r requirements.txt
```

Use `pytest`. E.g., 

```shell
py.test test/functional/test_amazon_web.py
```

Or use `pytest-xdist` to run in parallel (set parallelism with `-nN` where `N` is the number of parallel sessions). E.g., 

```shell
py.test -n2 --boxed test/functional/test_amazon_web_sauce.py
```
