import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from sys import argv
from wolframclient.evaluation import WolframLanguageSession
from wolframclient.language import wl, wlexpr

def plot_histogram(data):
    session = WolframLanguageSession()
    wd = session.WeightedData[data[[All, ;; 2]], data[[All, -1]]]; 
    session.Histogram3D[wd, {1}, ColorFunction -> "Rainbow"]

def main():
    # Load the data
    data = pd.read_csv('vertices.csv')
    positions = data[['pos x', 'pos y', 'pos z']]
    plot_histogram(positions)

if __name__ == '__main__':
    main()
