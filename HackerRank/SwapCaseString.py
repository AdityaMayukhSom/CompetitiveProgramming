
def swap_case(string):
    length = len(string)
    newstring = ""
    for i in range(length):
        if(string[i].isalpha()):
            if(string[i].islower()):
                # print('We enter islower block')
                newstring = newstring + string[i].upper()
            else:
                # print('We enter isupper block')
                newstring = newstring + string[i].lower()
        else:
            newstring = newstring + string[i]

    return newstring


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
