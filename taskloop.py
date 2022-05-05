def nat_nos():
    i = 1
    while i <= 10:
        print(i)
        i += 1

def pyramid():
    rows = 4
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end=' ')
        print('')

if __name__ == '__main__':
    nat_nos()
    pyramid()