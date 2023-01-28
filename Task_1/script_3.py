import json
import exceptions


def decorator(func):
    def wrap(user_id, company_id):
        with open("users_db.json", "r") as file:
            dict_users = json.load(file)
        if dict_users.get(user_id) is not None:
            companies = dict_users[user_id]['companies']
        else:
            raise exceptions.NotFound("User not found.")
        company_id_int = int(company_id)
        if company_id_int not in companies:
            raise exceptions.NoAccess(f"User ({user_id}) not have access to company ({company_id}).")
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
                return temp
    return wrap


@exception_handler
@decorator
def get_company_city(company_id):
    with open("company_db.json", "r") as file:
        dict_comp = json.load(file)
    if dict_comp.get(company_id) is not None:
        return dict_comp[company_id]['city']
    else:
        raise exceptions.NotFound("Company not found.")