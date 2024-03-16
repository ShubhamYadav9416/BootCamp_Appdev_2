from .model import *


from application.cache import cache

@cache.cached(timeout=1, key_prefix='get_all_users')
def get_all_users():
    users = User.query.all()
    all_user = []
    for user in users:
        all_user.append({'user_id': user.user_id,
                             'user_mail': user.user_mail,
                             'password': user.password})
    return all_user