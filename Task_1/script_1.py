import json
import exceptions


def get_company_city(company_id):
    with open("company_db.json", "r") as file:
        dict_comp = json.load(file)
    if dict_comp.get(company_id) is not None:
        return dict_comp[company_id]['city']
    else:
        raise exceptions.NotFound("Company not found.")
