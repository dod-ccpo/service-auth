import os
import pytest
from flask import Flask

@pytest.fixture
def app():
    return Flask("test_app")

@pytest.fixture
def key():
    return os.urandom(24).hex()
