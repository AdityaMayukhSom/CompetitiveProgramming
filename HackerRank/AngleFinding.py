import math
c = int(input())
a = int(input())
b = math.sqrt((a * a) + (c * c))
cm = b / 2
bm = math.sqrt((a * a / 4) + (c * c / 4))
cosValue = ((bm * bm + a * a - cm * cm) / (2 * bm * a))
rad = math.acos(cosValue)
deg = math.degrees(rad)
frac = deg - math.floor(deg)
if(frac < 0.5):
    deg = int(math.floor(deg))
else:
    deg = int(math.floor(deg) + 1)
degreesign = chr(176)
print(f'{deg}{degreesign}')
