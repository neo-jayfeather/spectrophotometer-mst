import numpy as np

MST = 2

def dE76(point1, point2):
    L1, a1, b1 = point1
    L2, a2, b2 = point2
    delta_L = L2 - L1
    delta_a = a2 - a1
    delta_b = b2 - b1
    delta_e = np.sqrt(delta_L**2 + delta_a**2 + delta_b**2)
    return delta_e

def openMST(filename, file2, output_filename):
    dE_values = []
    tarNumbers = []
    with open(filename, 'r') as file:
        with open(file2, 'r') as file2:
            lines = file.readlines()
            line2 = file2.readlines()
            for x in range(len(lines) - 1):
                items = lines[x + 1].rstrip().replace('\t', ' ').split(' ')
                item2 = line2[x + 1].rstrip().replace('\t', ' ').split(' ')
                if items:
                    L, a, b = float(items[7]), float(items[8]), float(items[9])
                    target = (float(item2[7]), float(item2[8]), float(item2[9]))
                    cur_dE = dE76((L, a, b), target)
                    dE_values.append(cur_dE)
                    tarNumbers.append(items[0])

    # Save the results to a text file, ignoring blank lines
    with open(output_filename, 'w') as output_file:
        for x in range(len(dE_values)):
            if tarNumbers[x].strip():  # Ignore blank lines
                output_file.write(f"Patch {tarNumbers[x]}: dE = {dE_values[x]:.4f}\n")
    print(f"Results saved to {outputFile}")

file = f'10msts/mst{MST}.txt'
otherFile = f'10msts/mst{MST+10}.txt'
outputFile = f'MST {MST} comparison_output.txt'
for e in range(10):
    MST = e + 1
    file = f'10msts/mst{MST}.txt'
    otherFile = f'10msts/mst{MST+10}.txt'
    outputFile = f'MST {MST} comparison_output.txt'
    openMST(file, otherFile, outputFile)
