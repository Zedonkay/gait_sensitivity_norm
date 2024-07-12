import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def hist(df):
    hist = []
    for data in df:
        if data[2]==0:
            continue
        for i in range(0,int(data[2]*1000)):
            hist.append([data[0],data[1]])
    hist = np.array(hist)
    return hist

def main():
    df = pd.read_csv('vertices.csv')
    histogram = hist(df.values)
    df = pd.DataFrame(histogram, columns=['x','y'])
    df.to_csv('histogram.csv', index=False)

if __name__ == "__main__":
    main()