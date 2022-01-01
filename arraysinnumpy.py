import numpy as np

# Three lists, one for GK heights, one for GK weights, one for names

GKNames = ["Kaller", "Fradeel", "Hayward", "Honeyman"]
GKHeights = [184, 188, 191, 193]
GKWeights = [81, 85, 103, 99]

# Create an array of names

print(np.array(GKNames))

# Create a matrix of all three lists, start with a list of lists

GKMatrix = [GKNames, GKHeights, GKWeights]
print(np.array(GKMatrix))
