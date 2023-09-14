import numpy as np
import pandas as pd
import SplinePath as spp

data = pd.read_csv("objectPoses.csv", header=None)

data = np.array(data)

sppath = spp.SplinePathModeler(6)

t_predicted = []
x_predicted = []

l = len(data)
for k, el in enumerate(data):
    if k < l-1:
        next_t = data[k+1][2]
        ret = sppath.predict(np.array([el[0], el[2]]), next_t)
        if not ret is None:
            t_predicted.append(next_t)
            x_predicted.append(ret)
            print("t:", next_t)
            print("actual:", data[k+1][0])
            print("prediction:", ret)
            print('----')
