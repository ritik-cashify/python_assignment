set = {10, 20, 30, 40, 50}
list={60,70}
set1= {1000,10}


def addlst_2set():
    print("Orignal set:",set)
    set.update(list)
    print("The updated set is:",set)

if __name__=='__main__':
    addlst_2set()