set = {10, 20, 30, 40, 50}
list={60,70}
set1= {1000,10}


def addlst_2set():
    print("Orignal set:",set)
    set.update(list)
    print("The updated set is:",set)

def common_elements():
    print("The first set:",set)
    print("The second set:",set1)
    print("The common elements from both the sets are:",set.intersection(set1))

if __name__=='__main__':
    addlst_2set()
    common_elements()