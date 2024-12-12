from matplotlib import pyplot as plt
import pandas as pd
import random
import numpy as np


df = pd.DataFrame({"number": np.array([random.randint(-10, 10) for i in range(10)]), "number two": [random.randint(-10, 10) for i in range(10)]})
df1 = pd.DataFrame({'first': [random.randint(-10, 10) for i in range(50)]})
df2 = pd.DataFrame({'second': [random.randint(-10, 10) for i in range(50)]})

print(df)

res = df['number'].unique()
res1 = df['number two'].unique()
list = np.concatenate((res, res1))
print(list)



res3 = df1.value_counts()
res3 = res3.reset_index()
plt.bar(res3['first'], res3['count'])
plt.show()


res4 = pd.concat([df1, df2])
print(res4)

df1.insert(1, 'second', df2)
res44 = df1
print(res44.head())



plt.plot(res44['first'], res44['second'])
plt.show()