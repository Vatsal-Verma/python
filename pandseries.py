import pandas as pseries
import numpy as np
data=np.array(['a','b','c','d'])
s=pseries.Series(data,index=[101,102,103,104])
print(s)