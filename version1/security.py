from user import User
from werkzeug.security import safe_str_cmp

users = [
    User(1, 'bob', 'asdf')
]


username_mapping = {u.username: u for u in users}

userid_mapping = {u.id: u for u in users}

# function to authenticate the user
def authenticate(username, password):
    user = username_mapping.get(username, None)
    # if user and user.password == password:
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload):
    """   
    payload contains the content of JWT token and extraxts the user if from payload
    """
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)
