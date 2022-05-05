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

def count_digits(n):
    count=0
    while n>0:
        n=n//10
        count=count+1
    print("Total digits:", count)

#def pattern

def reverse_list(lst):
    i = len(lst) - 1
    while i >=0:
        print(lst[i])
        i -= 1

def display_nos():
    for i in range(-10,0):
        print(i)


if __name__ == '__main__':
    nat_nos()
    pyramid()
    n = int(input("Enter the number: "))
    sumofnumbers(n)
    n1 = int(input("Enter the number :"))
    mul_table(n)
    listt = [1, 2, 5, 6]
    print_list(list_1= listt)
    a = int(input("Enter the number: "))
    count_digits(n = a)
    list_11 = [3, 6, 8, 9]
    reverse_list(lst=list_11)
    display_nos()



