#list tasks

list0=["ritik","cashify"]
list1=["company","good"]
list2=[8,56,9,89]
list3=[9,10,80,55,10]
list4=["ritik", "", "ok", "", "cashify"]



def rev_list(list):
    list0.reverse()
    return list0

print("The original list:",list0)
print("The reverse list:",rev_list(list))

def concat_index():
    res_list = [y for x in [list2, list3] for y in x]
    print("First list:",list2)
    print("Second list:",list3)
    print("The concatenated list:",res_list)

concat_index()

def square_list():
    sq_list = [x ** 2 for x in list2]
    print("List to be sqaured:",list2)
    print("The square of the above list is:",sq_list)

square_list()

def concat_forder():
    concat_list = [x + y for x in list0 for y in list1]
    print("The First list to be concatenated by order is:",list0)
    print("The Second list to be concatenated by order is:",list1)
    print("The list after concatenation by order is:",concat_list)

concat_forder()

def it_2list():
    print("The First list to be iterated is:", list0)
    print("The Second list to be iterated is:", list1)

    for i,j in zip(list0,list1):
        print(i+j)
it_2list()

def remove_empstrings():
    print("The test list is:",list4)
    new_list = list(filter(None, list4))
    print(new_list)

remove_empstrings()

def add_nitem():
    print("The list in which item is to be added:",list2)
    list2.insert(2,"ok") #element added according to the index mentioned
    list2.append(99) #element added at the end

    print(list2)

add_nitem()

#def nested_list
#to get index of the element id=list.index("element")
def replace_element():
    list2[2] = 79
    print(list2)

replace_element()

def remove_element():
    while 10 in list3:
        list3.remove(10)

print("The list from which duplicate elements have to be removed:",list3)
remove_element()
print(list3)








