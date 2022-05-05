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



if __name__ == '__main__':
    tpl = (10, 20, 30, 40)
    tpl1= (40, 50)
    tp1 = ("Orange", [10, 20, 30], (5, 15, 25))
    reverse_tuple(tp=tpl)
    ac_twenty(tp=tp1)
    single_item(tp=(50,))
    unpack_tp(tp=tpl)
    swap_2tuple(tp=tpl, tp_1=tpl1)
