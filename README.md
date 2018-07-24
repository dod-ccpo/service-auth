# service-auth

This library provides a class and utility functions for injecting secure headers in HTTP requests and responses. It targets Flask applications and can be adapted for any generic HTTP client library. An example for [`requests`](http://docs.python-requests.org/en/master/) is included.

# Run the Demo

```
pipenv install
pipenv run python demo/flask_app.py
```

And then in a new terminal window:

```
pipenv run python demo/flask_client.py
```

The client will try a couple unsuccessful requests, and then a successful request where it also validates the response.

# Run the tests

```
pipenv run pytest
```
