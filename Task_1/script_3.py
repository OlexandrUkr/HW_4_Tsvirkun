import json
import exceptions


def decorator(func):
    def wrap(user_id, company_id):
        with open("users_db.json", "r") as file:
            dict_users = json.load(file)
        try:
            companies = dict_users[user_id]['companies']
        except KeyError:
            return exceptions.NotFound
        company_id_int = int(company_id)
        if company_id_int not in companies:
            return exceptions.NoAccess
        return func(company_id)
    return wrap


def exception_handler(func):
    def wrap(*args):
        try:
            temp = func(*args)
        except:
            pass
        else:
            if temp == exceptions.NoAccess:
                pass
            elif temp == exceptions.NotFound:
                pass
            else:
                return func(*args)
    return wrap


@exception_handler
@decorator
def get_company_city(company_id):
    with open("company_db.json", "r") as file:
        dict_comp = json.load(file)
    try:
        return dict_comp[company_id]['city']
    except KeyError:
        return exceptions.NotFound
