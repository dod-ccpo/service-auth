# service-auth

This library provides a class and utility functions for injecting secure headers in HTTP requests and responses. It targets Flask applications and can be adapted for any generic HTTP client library. An example for [`requests`](http://docs.python-requests.org/en/master/) is included.

### Cloning

This project contains git submodules. Here is an example clone command that will
automatically initialize and update those modules:

    git clone --recurse-submodules git@github.com:dod-ccpo/service-auth.git

### Setup

This library uses Pipenv to manage Python dependencies and a virtual
environment. Instead of the classic `requirements.txt` file, pipenv uses a
Pipfile and Pipfile.lock, making it more similar to other modern package managers
like yarn or mix.

To perform the installation, run the setup script:

```
./script/setup
```

The setup script creates the virtual environment, and then calls script/bootstrap
to install all of the Python dependencies.


# Run the Demo

```
./script/demo_server
```

And then in a new terminal window:

```
./script/demo_client
```

The client will try a couple unsuccessful requests, and then a successful request where it also validates the response.

# Run the tests

```
./script/test
```
