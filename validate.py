def validate_login(username, password):
    valid_users = {
        "alice": "pass123",
        "bob": "hello456",
    }

    return valid_users.get(username) == password