chalteRaho = True
addKarlo = 0
while(chalteRaho):
    inputDedo = input()
    if(inputDedo == 'socio'):
        chalteRaho = False
    else:
        addKarlo = addKarlo + int(inputDedo)

print(addKarlo)
