def addlst_2set(set_to_add_to, list_to_add):
    updated_set = set_to_add_to.update(list_to_add)
    print("The updated set is:", updated_set)
    return updated_set

def common_elements(set_1, set_2):
    print("The common elements from both the sets are:",set_1.intersection(set_2))

def unique_elements(Fset, Sset):
    print("The unique elements from both the set are:",Fset.union(Sset))

def difference_bw2sets(Fiset, Seset):
    Fiset.difference_update(Seset)
    print("Items in first set and not in second are:",Fiset)

def remove_elements(set_1):
    set_1.difference_update({10,20,30})
    print("Set after deletion:",set_1)

def print_elements(set_1, set_2):
    print("Elements present in first set or second set but not both are:", set_1.symmetric_difference(set_2))

def check_commonelements(set_1, set_2):
    if set_1.isdisjoint(set_2):
        print("Two sets have nothing in common")
    else:
        print("Two sets have elements in common")
        print(set_1.intersection(set_2))

def add_elementsnotcommon(set_1, set_2):
    set_1.symmetric_difference_update(set_2)
    print("Elements in two given set except common items:",set_1)

def remove_notcommon(set_1, set_2):
    set_1.intersection_update(set_2)
    print(set_1)


if __name__=='__main__':
    sett = {10, 20, 30, 40, 50}
    set1 = {1000, 10}
    listt = {60, 70}
    sett1 = {30, 40, 50}
    sett2 = {50, 60, 100}
    sett3= {50, 80, 90, 60}
    addlst_2set(set_to_add_to=sett, list_to_add=listt)
    common_elements(set_1=sett, set_2=set1)
    unique_elements(Fset=sett, Sset=set1)
    difference_bw2sets(Fiset=sett, Seset=set1)
    remove_elements(set_1=sett)
    print_elements(set_1=sett, set_2=set1)
    check_commonelements(set_1=sett, set_2=sett1)
    add_elementsnotcommon(set_1=sett1, set_2=sett2)
    remove_notcommon(set_1=sett2, set_2=sett3)




