def findWhite(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        for x in range(len(lines)-1):
        #for x in range(100):
            items = lines[x+1].rstrip().replace('\t',' ').split(' ')
            if items:
                L, a, b = float(items[7]), float(items[8]), float(items[9])
                if(L > 97 and  a < 1 and a > -1 and b > -1 and b < 1):
                    print(items[0])
findWhite('11msts.txt')
print(000)
