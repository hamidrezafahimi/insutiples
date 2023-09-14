import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import scipy.interpolate

import pandas as pd

import SplinePath as spp

data = pd.read_csv("objectPoses.csv", header=None)

data = np.array(data)

# print(data[1])

sppath = spp.SplinePathModeler(7)

for el in data:
    sppath.predict(np.array([el[0], el[2]]), el[2]+0.33)

# print(len(we))
