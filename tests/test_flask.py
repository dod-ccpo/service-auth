import os
import flask
import pytest
import logging
from collections import namedtuple
import werkzeug.exceptions as flask_exceptions
from flask._compat import StringIO
from service_auth.flask import AuthHeader
from service_auth.http_token import make_token


@pytest.fixture(scope="module")
def service_auth():
    return AuthHeader("some-random-key")


@pytest.fixture
def log_stream(app):
    stream = StringIO()
    handler = logging.StreamHandler(stream)
    app.logger.addHandler(handler)
    return stream


def test_rejects_unauthorized_with_missing_headers(app, log_stream, service_auth):
    with app.test_request_context():
        with pytest.raises(flask_exceptions.Unauthorized) as excinfo:
            service_auth.authenticate_request()
        assert "missing required headers" in log_stream.getvalue()


def test_reject_unauthorized_with_bad_token(app, log_stream, service_auth):
    with app.test_request_context(
        headers={
            "Date": "2 June, 1968", "Host": "testing.com", "X-Token-Auth": "abc123"
        }
    ):
        with pytest.raises(flask_exceptions.Unauthorized) as excinfo:
            service_auth.authenticate_request()
        assert "invalid token" in log_stream.getvalue()


def test_accepts_valid_request(app, service_auth):
    date = "2 June 1968"
    host = "testing.com"
    token = make_token(service_auth._secret, [date, host, ""])
    with app.test_request_context(
        headers={"Date": date, "Host": host, "X-Token-Auth": token}
    ):
        assert service_auth.authenticate_request()

MockResponse = namedtuple('MockResponse', 'headers status_code data')

def test_apply_auth_header(service_auth):
    mock_response = MockResponse(headers={}, status_code=200, data=b'hello there')
    service_auth.apply_auth_header(mock_response)
    date = mock_response.headers["Date"]
    assert date
    token = make_token(service_auth._secret, [date, "200", "hello there"])
    assert mock_response.headers["X-Token-Auth"] == token
