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

def sumofnumbers(num):
    sum = 0
    for x in range(1, num + 1):
        sum = sum + x

    print(sum)

def mul_table(num):
    for x in range(1, num+1):
        print(num, 'x', x, '=', num * x)

def print_list(list_1):
    x = 0

    while (x < len(list_1)):
        print(list_1[x])
        x = x + 1

if __name__ == '__main__':
    nat_nos()
    pyramid()
    n = int(input("Enter the number: "))
    sumofnumbers(n)
    n1 = int(input("Enter the number :"))
    mul_table(n)
    listt = [1, 2, 5, 6]
    print_list(list_1= listt)

