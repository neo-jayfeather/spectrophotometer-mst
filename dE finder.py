import numpy as np
from scipy.sparse.csgraph import minimum_spanning_tree

# MST targets (Lab color values)
target = [
    (94.211, 1.503, 5.422),
    (92.275, 2.061, 7.28),
    # ... (other targets for mst2 to mst10)
]

# Load your data (32 patches) and store it in a matrix (e.g., 'patches_matrix')

def dE76(point1, point2):
    L1, a1, b1 = point1
    L2, a2, b2 = point2
    delta_L = L2 - L1
    delta_a = a2 - a1
    delta_b = b2 - b1
    delta_e = np.sqrt(delta_L**2 + delta_a**2 + delta_b**2)
    return delta_e

def compute_min_dE_for_MST(patches_matrix, MST_target):
    num_patches = patches_matrix.shape[0]
    min_dE_values = np.zeros(num_patches)

    for i in range(num_patches):
        min_dE = float('inf')  # Initialize with positive infinity
        for j in range(num_patches):
            cur_dE = dE76(patches_matrix[i], MST_target)
            min_dE = min(min_dE, cur_dE)  # Update minimum dE
        min_dE_values[i] = min_dE

    return min_dE_values

# Example usage:
# Load your patches_matrix (shape: (32, 3)) here
# Compute min_dE for each MST (e.g., MST1, MST2, ..., MST10)
for mst_num in range(1, 11):
    MST_file = f'10msts/mst{mst_num}.txt'
    MST_patches_matrix = load_patches_from_file(MST_file)  # Implement this function
    min_dE_values = compute_min_dE_for_MST(MST_patches_matrix, target[mst_num - 1])
    print(f"MST{mst_num}: Lowest dE = {np.min(min_dE_values):.4f}")
