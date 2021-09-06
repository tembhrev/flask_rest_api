from models.user import UserModel
from werkzeug.security import safe_str_cmp



# function to authenticate the user
def authenticate(username, password):
    user = UserModel.find_by_username(username)
    # if user and user.password == password:
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload):
    """   
    payload contains the content of JWT token and extraxts the user if from payload
    """
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
