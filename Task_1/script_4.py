import json
import time
import exceptions
import logging

format_template = ' %(asctime)s - %(name)s - %(levelname)s - %(message)s'

logger = logging.Logger(__name__)

s_handler = logging.StreamHandler()
s_handler.setLevel(logging.DEBUG)
logger.addHandler(s_handler)

f_handler = logging.FileHandler(f"{__file__}_log.txt", mode="w")
f_handler.setLevel(logging.ERROR)
f_handler.setFormatter(logging.Formatter(format_template))
logger.addHandler(f_handler)


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


def time_counter(func):
    def wrap(*args):
        t1 = time.time()
        logger.info(f"Старт виконання функції (get_company_city): {t1}")
        result = func(*args)
        t2 = time.time()
        logger.info(f"Час виконання функції (get_company_city): {(t2 - t1)}")
        return result
    return wrap


@exception_handler
@decorator
@time_counter
def get_company_city(company_id):
    with open("company_db.json", "r") as file:
        dict_comp = json.load(file)
    if dict_comp.get(company_id) is not None:
        return dict_comp[company_id]['city']
    else:
        raise exceptions.NotFound("Company not found.")
