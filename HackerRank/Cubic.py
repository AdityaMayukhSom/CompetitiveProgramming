if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    my_List = list()
    for i in range(x):
        for j in range(y):
            for k in range(z):
                arr = [x, y, z]
                sum = 0
                for var in range(2):
                    sum = sum + arr[var]
                if (sum != n):
                    list.append(arr)

    print(list)
