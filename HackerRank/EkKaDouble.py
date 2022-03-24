names = ['Manoj', 'Ravi', 'Harish', 'Seema', 'Abhinav']
a = int(input())
b = a / 5
var_big = 1
var_small = 1
big = 1
small = 0
while(True):
    var_big = var_big + pow(2, big)
    if(b < var_big):
        break
    big = big + 1
    small = small + 1
    var_small = var_small + pow(2, small)

var_big = 5 * var_big
var_small = 5 * var_small
deviation = a - var_small
if(deviation == 0):
    to_shrink = 4
else:
    to_shrink = int(deviation / pow(2, big))

print(names[to_shrink])
