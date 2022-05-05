def reverse_tuple(tp):
    rtp = reversed(tp)
    rtp = tuple(rtp)
    print("The reverse of the tuple is:",rtp)

def ac_twenty(tp):
    print(tp[1][1])

def single_item(tp):
    print(tp)


if __name__ == '__main__':
    tpl = (10, 20, 30, 40, 50)
    tp1 = ("Orange", [10, 20, 30], (5, 15, 25))
    reverse_tuple(tp=tpl)
    ac_twenty(tp=tp1)
    single_item(tp=(50,))
