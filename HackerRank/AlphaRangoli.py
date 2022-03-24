def print_rangoli(n):
    # Loop for upper half
    for lineNumber in range(n):
        for j in range(0, (n - lineNumber - 1) * 2):
            print('-', end="")

        # The alphabet printing starts here
        # print('xxx', end="")
        for k in range(n, 0, -1):
            print(f'{chr(96+k)}', end="")
        # The alphabet printing ends here

        for j in range(0, (n - lineNumber - 1) * 2):
            print('-', end="")

        print()


'''
    # Loop for lower half
    for lineNumber in reversed(range(n - 1)):
        for j in range(0, ((4 * n) - 3 - (2 * lineNumber) - 1) // 2):
            print('-', end="")

        # The alphabet printing starts here
        # print('xxx', end="")
        for k in range(n, 0, -1):
            print(f'{chr(96+k)}-', end="")
        # The alphabet printing ends here

        for j in range(0, ((4 * n) - 3 - (2 * lineNumber) - 1) // 2):
            print('-', end="")
        print()
        # for k in range(n, 0, -1):
        #     print(f'{chr(96+k)}-')
'''

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
