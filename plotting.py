import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from sys import argv
from wolframclient.evaluation import WolframLanguageSession
from wolframclient.language import wl, wlexpr

def plot_3d(data):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_trisurf(data['x'], data['y'], data['z'], cmap=cm.jet, linewidth=0)
    fig.colorbar(surf)

    ax.xaxis.set_major_locator(plt.MaxNLocator(5))
    ax.yaxis.set_major_locator(plt.MaxNLocator(6))
    ax.zaxis.set_major_locator(plt.MaxNLocator(5))

    fig.tight_layout()
    plt.show()
def reorg():
    # Load the data
    df = pd.read_csv('vertices.csv')
    df = df.sort_values(by=['x', 'y', 'z'])
    df.to_csv('vertices.csv', index=False)
def main():
    data = pd.read_csv('vertices.csv')
    plot_3d(data)

if __name__ == '__main__':
    main()
