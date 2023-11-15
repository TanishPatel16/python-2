def sort_people(list_name, field, direction):
    list_name.sort(key = lambda p: p[f'{field}'], reverse = True if direction == "desc" else False)
    return list_name

def filter_males(list_name):
    filter_list = list(filter(lambda p : p['sex'] == 'male', list_name))
    return filter_list

def transform_list(person):
    person["bmi"] = round(person["weight_kg"]/(person["height_meters"]**2), 1)
    return person

def calc_bmi(list_name):
    new_list= list(map(transform_list, list_name))
    return new_list

def get_people(people_list):
    names = [person['name'] for person in people_list if person["age"]>=15]
    return names
