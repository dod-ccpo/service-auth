from service_auth.http_token import make_token, validate_token

data = ['some', 'random', 'content']

def test_make_token(key):
    token = make_token(key, data)
    # is ascii
    assert all(ord(c) < 128 for c in token)
    token2 = make_token(key, data)
    assert token == token2

def test_validate_token(key):
    token = make_token(key, data)
    assert validate_token(token, key, data)
    assert not validate_token(token, 'abc123', data)
    assert not validate_token('abc123', key, data)
    assert not validate_token(token, key, ['other stuff'])
