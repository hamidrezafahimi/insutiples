import numpy as np

p = np.getbuffer(np.arange(10))
pp = np.frombuffer(p, dtype=int)