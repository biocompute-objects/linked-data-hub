import json
import datetime
import os
import glob

def get_EntIri(data):
    return data['object_id']

def get_EntId(data):
    return data['object_id'].split('/')[-2]

def get_time():
    current = datetime.datetime.utcnow()
    return current.isoformat() + 'Z'

def get_EntContent(data):
    content = {}
    try:
        content['provenance'] = data['provenance_domain']
    except KeyError:
        pass
    try:
        content['usability'] = data['usability_domain']
    except KeyError:
        pass
    try:
        content['description'] = data['description_domain']
    except KeyError:
        pass
    try:
        content['execution'] = data['execution_domain']
    except KeyError:
        pass
    try:
        content['io'] = data['io_domain']
    except KeyError:
        pass
    try:
        content['parametric'] = data['parametric_domain']
    except KeyError:
        pass

    return content


def get_id():
    id_list = input("Enter the list of your ids separated by commas").split(',')
    return id_list


def get_id_for():
    id_for_list = input("Enter the list of your IdFors separated by commas").split(',')
    return id_for_list

def create_ldh(jsonfile, name):
    file = open(jsonfile)
    data = json.load(file)
    contents = {}

    contents['id'] = get_id()
    contents['IdFor'] = get_id_for()
    contents['entType'] = 'BioCompute Object'
    contents['entId'] = get_EntId(data)
    contents['entIri'] = get_EntIri(data)
    contents['entAliases'] = [contents['entId'], contents['entIri'], contents['entType']]
    contents['modifier'] = name
    contents['modified'] = get_time()


    contents['entContent'] = get_EntContent(data)

    print(contents)

    with open('example.json', 'w') as f:
        json.dump(contents, f, indent=4)



create_ldh('CIVIC Biomarkers.json', "Aditya Lahiri")