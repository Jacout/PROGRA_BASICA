def search(L, item):
    flag = 0
    for i in L:
        if i == item:
            flag = 1
            print('Position ',i)
        if flag == 0:
            print('Not found')


L =[1, 2, 5, 9, 10]
search(L, 5)
search(L, 3)
