import pandas as pd
import numpy as np

a = [1, 2, 3]
df2 = pd.DataFrame(np.array([a, [4, 5, 6], [7, 8, 9]]), columns=['a', 'b', 'c'])

print(df2)