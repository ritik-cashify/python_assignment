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

if __name__=='__main__':
    list_2dict()
    merge_2dict()


