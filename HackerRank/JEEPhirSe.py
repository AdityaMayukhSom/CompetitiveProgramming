my_str = input()
length = len(my_str)
JCount = 0
ECount = 0
for i in range(length):
    if (my_str[i] == 'J'):
        JCount = JCount + 1
    if(my_str[i] == 'E'):
        ECount = ECount + 1

if(ECount == (2 * JCount)):
    print('Yes')
else:
    print('No')
