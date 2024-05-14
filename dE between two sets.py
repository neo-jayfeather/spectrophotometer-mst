import numpy as np
MST = 1
def dE76(point1, point2):
    L1, a1, b1 = point1
    L2, a2, b2 = point2
    delta_L = L2 - L1
    delta_a = a2 - a1
    delta_b = b2 - b1
    delta_e = np.sqrt(delta_L**2 + delta_a**2 + delta_b**2)
    return delta_e

def openMST(filename, file2):
    dE_values = []
    tarNumbers = []
    with open(filename, 'r') as file:
        with open(file2, 'r') as file2:
            lines = file.readlines()
            line2 = file2.readlines()
            for x in range(len(lines) - 1):
                items = lines[x + 1].rstrip().replace('\t', ' ').split(' ')
                item2 = line2[x + 1].rstrip().replace('\t', ' ').split(' ')
                #print(10)
                if items:
                    L, a, b = float(items[7]), float(items[8]), float(items[9])                
                    target = (float(item2[7]), float(item2[8]), float(item2[9]))
                    cur_dE = dE76((L, a, b), target)
                    print(cur_dE)
                    
        
        
file = f'10msts/mst{MST}.txt'
otherFile = f'10msts/mst{MST+10}.txt'
openMST(file,otherFile)
