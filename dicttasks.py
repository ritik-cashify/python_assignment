head = ['name', 'age', 'company']
value = ['Ritik', '22', 'cashify']
dict_1 = {'good': 100, 'bad': 0, 'fair' : 50 }
dict_2 = {'ritik': 1, 'purvansh': 2, 'avtar' : 3 }
nested_dict = {
    'member1': {'name': 'Ritik', 'age': 22},
    'member2': {'name': 'Purvansh', 'age': 80},
    'member3': {'name': 'Avtar', 'age': 50}
}

def list_2dict():
    print("The first list:",head)
    print("The second list",value)
    dict_converted=dict(zip(head,value))
    print(dict_converted)

def merge_2dict():
    print("The first dict:",dict_1)
    print("The second dict:",dict_2)
    dict_1.update(dict_2)
    print(dict_1)

def print_history():
    sampleDict = {
        "class": {
            "student": {
                "name": "Mike",
                "marks": {
                    "physics": 70,
                    "history": 80
                }
            }
        }
    }

    print(sampleDict['class']['student']['marks']['history'])

def def_values():
    employees = ['Kelly', 'Emma']
    defaults = {"designation": 'Developer', "salary": 8000}
    result = dict.fromkeys(employees, defaults)
    print(result)

def key_extract():
    key_2extract = ['good','avtar']
    dict_new = {k: dict_1[k] for k in key_2extract}
    print(dict_new)

def delete_key():
    key_2del = ['good','bad']
    for k in key_2del:
        dict_1.pop(k)
    print(dict_1)

def check_presence():
    if 60 in dict_1.values():
        print("is present")
    else:
        print("not present")

def change_key():
    dict_1['amit'] = dict_1.pop('purvansh')
    print(dict_1)

def key_minvalue():
    print(min(dict_1, key=dict_1.get))


if __name__=='__main__':
    list_2dict()
    merge_2dict()
    print_history()
    def_values()
    key_extract()
    delete_key()
    check_presence()
    change_key()
    key_minvalue()


