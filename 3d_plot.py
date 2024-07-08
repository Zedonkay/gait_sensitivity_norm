import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# prepare some coordinates
x, y, z = np.indices((2000,1600,49))*.006



voxelarray=[[]]
ind = 0
df = pd.read_csv('rounded.csv')
data = df.values
for px in np.arange(-6,6.2,0.2):
        for py in np.arange(-4.8,5,0.2):
                voxelarray.append( (x<px+0.1)&(x>px-0.1)
                                    &(y<py+0.1)&(y>py-0.1)
                                    &(z< data[ind][2])&(z>-0.1) 
                                  )
                ind+=1
if voxelarray[0]==[]:
        voxelarray = np.array(voxelarray[1:])
else:
        voxelarray = np.array(voxelarray)
                

# and plot everything
ax = plt.figure().add_subplot(projection='3d')
ax.voxels(voxelarray, edgecolor='k')

plt.show()