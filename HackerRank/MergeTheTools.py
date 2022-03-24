def merge_the_tools(string, k):
    # your code goes here
    arr = list()
    count = 0
    for i in range(0, len(string), k):
        print('Value of i is %d' % i)
        count = count + 1
        print('Loop running %d times' % count)
        currentString = string[i:i + k]
        res = ''
        for item in currentString:
            if item not in res:
                res = res + item
        arr.append(res)

    for string in arr:
        print(string)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
