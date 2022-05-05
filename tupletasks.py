def reverse_tuple(tp):
    rtp = reversed(tp)
    rtp = tuple(rtp)
    print("The reverse of the tuple is:",rtp)

def ac_twenty(tp):
    print(tp[1][1])

def single_item(tp):
    print(tp)

def unpack_tp(tp):
    q, x, y, z = tp
    print(q)
    print(x)
    print(y)
    print(z)

def swap_2tuple(tp, tp_1):
    print("before swapping")
    print("first tuple:", tp)
    print("second tuple:", tp_1)
    temp = tp
    tp = tp_1
    tp_1 = temp
    print("After swapping")
    print("First tuple:", tp)
    print("second tuple:", tp_1)

def copy_tuple(tp):
    result = tp[1:3]
    result = tuple(result)
    print("The sliced tuple is:", result)

#def modify
#def sort

def count_item(tp):
    print(tp.count(1))

def all_same(tp):
    rt = tp.count(tp[0]) == len(tp)
    if (rt):
        print("all same")
    else:
        print("all not some or not at all same")



if __name__ == '__main__':
    tpl = (10, 20, 30, 40)
    tpl1 = (40, 50)
    tp1 = ("Orange", [10, 20, 30], (5, 15, 25))
    tpl2 = (1, 5, 6, 7, 0, 1, 1, 4, 1)
    tpl3 = (10, 10, 10, 10)
    reverse_tuple(tp=tpl)
    ac_twenty(tp=tp1)
    single_item(tp=(50,))
    unpack_tp(tp=tpl)
    swap_2tuple(tp=tpl, tp_1=tpl1)
    copy_tuple(tp=tpl)
    count_item(tp=tpl2)
    all_same(tp=tpl3)
