import json
import exceptions


def get_company_city(company_id):
    with open("company_db.json", "r") as file:
        dict_comp = json.load(file)
    try:
        return dict_comp[company_id]['city']
    except KeyError:
        return exceptions.NotFound
