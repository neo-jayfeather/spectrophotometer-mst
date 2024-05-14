import numpy as np

MST = 10
target = [
    (94.211, 1.503, 5.422),
    (92.275, 2.061, 7.28),
    (93.091, 0.216, 14.205),
    (87.573, 0.459, 17.748),
    (77.902, 3.471, 23.136),
    (55.142, 7.783, 26.74),
    (42.47, 12.325, 20.53),
    (30.678, 11.667, 13.335),
    (21.069, 2.69, 5.964),
    (14.61, 1.482, 3.525)
]

def dE76(point1, point2):
    L1, a1, b1 = point1
    L2, a2, b2 = point2
    delta_L = L2 - L1
    delta_a = a2 - a1
    delta_b = b2 - b1
    delta_e = np.sqrt(delta_L**2 + delta_a**2 + delta_b**2)
    return delta_e

def openMST(filename, numT):
    dE_values = []
    tarNumbers = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for x in range(len(lines) - 1):
            items = lines[x + 1].rstrip().replace('\t', ' ').split(' ')
            if items:
                L, a, b = float(items[7]), float(items[8]), float(items[9])                
                cur_dE = dE76((L, a, b), target[numT])
                dE_values.append(cur_dE)
                tarNumbers.append(items[0])
    mindE = np.min(dE_values)
    tar = 0
    for x in range(len(dE_values)):
        if(dE_values[x] == mindE):
            tar = tarNumbers[x]
    if(mindE <= 5):
        print(f'MST {MST} has a min dE of {mindE} compared to MST {numT+1}')
        print(f'patch : {tar}')
    
# Example usage:
for e in range(10):
    for i in range(10):
        MST = e+1
        file = f'10msts/mst{MST}.txt'
        openMST(file,i)
