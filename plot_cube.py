from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib import cm
import numpy as np
import pandas as pd
    
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

df = pd.read_csv('rounded.csv')
xs = np.unique(df['x'].values)
ys = np.sort(np.unique(df['y'].values))
def fun(x,y):
    x_index = np.where(xs==x)[0][0]
    y_index = np.where(ys==y)[0][0]
    index = x_index*len(ys)+y_index
    return df.values[index][2], index

cm.rainbow(np.linspace(0, 1, len(xs)*len(ys)))


for x in xs:
    for y in ys:
        x_low = x-0.1
        x_high = x+0.1
        y_low = y-0.1
        y_high = y+0.1
        z_low = 0
        z_high,index = fun(x,y)
        poly_3d=[[(x_low, y_low, z_low), (x_high, y_low, z_low), 
                  (x_high, y_high, z_low), (x_low, y_high, z_low)], 
                 
                 [(x_high, y_low, z_low), (x_high, y_low, z_high),
                   (x_high, y_high, z_high), (x_high, y_high, z_low)], 

                 [(x_low, y_high, z_low), (x_high, y_high, z_low), 
                  (x_high, y_high, z_high), (x_low, y_high, z_high)], 

                 [(x_low, y_low, z_high), (x_low, y_low, z_low), 
                  (x_low, y_high, z_low), (x_low, y_high, z_high)], 

                 [(x_high, y_low, z_high), (x_low, y_low, z_high), 
                  (x_low, y_high, z_high), (x_high, y_high, z_high)], 

                 [(x_low, y_low, z_high), (x_high, y_low, z_high), 
                  (x_high, y_low, z_low), (x_low, y_low, z_low)]]
        ax.add_collection3d(Poly3DCollection(poly_3d, facecolors='#eeeeee', linewidths=1, edgecolors='#bbbbbb'))


plt.show()