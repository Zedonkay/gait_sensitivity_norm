import pandas as pd
import numpy as np

def reorg(df):
    """
    Sorts the data by 'x', 'y', and 'z' columns.
    Saves the reorganized data to 'vertices.csv'.
    
    Parameters:
    - df: pandas DataFrame
        The input DataFrame containing the data to be reorganized.
    
    Returns:
    None
    """
    # Load the data
    # df = df.sort_values(by=['x', 'y', 'z'])
    # xs = np.unique(df['x'].values)
    # ys = np.unique(df['y'].values)
    # data = df.values
    # for x in xs:
    #     for y in ys:
    #         in_data = False
    #         for d in data:
    #             if d[0] == x and d[1] == y:
    #                 in_data = True
    #                 break
    #         if not in_data:
    #             print(f'Adding {x}, {y}')
    #             data = np.append(data, [[x, y, 0]], axis=0)
    data = df.values / 1000
    df = pd.DataFrame(data, columns=['x', 'y', 'z'])
    df = df.sort_values(by=['y', 'x', 'z'])
    df.to_csv('no_bump/vertices_no_bump.csv', index=False)

def round_data(data):
    """
    Rounds the data to the nearest 0.2 and calculates the mean 'z' value for each rounded data point.
    Translates the rounded data points to positive coordinates.
    Saves the rounded data to 'rounded.csv'.
    
    Parameters:
    - data: numpy array
        The input array containing the data to be rounded and processed.
    
    Returns:
    None
    """
    rounded_data = []
    for x in np.arange(-6,6.2,0.2):
        for y in np.arange(-4.8,5,0.2):
            rounded_data.append([np.round(x,1), np.round(y,1), 0])
    for rd in rounded_data:
        zs = []
        for d in data:
            if 0.2*np.round(d[0]/0.2)==rd[0] and 0.2*np.round(d[1]/0.2)==rd[1]:
                zs.append(d[2])
        if len(zs)>0:
            rd[2] = np.mean(zs)
        else:
            rd[2] = 0
    greatest = 0
    for rd in rounded_data:
        if rd[2]>greatest:
            greatest = rd[2]
        rd[0]=np.round(rd[0]+6,1)
        rd[1]=np.round(rd[1]+4.8,1)
    print(greatest)
    rounded_data = np.array(rounded_data)
    df = pd.DataFrame(rounded_data,columns=['x','y','z'] )
    df.to_csv('rounded.csv', index=False)

if __name__ == '__main__':
    # Read the formatted data from 'formatted_data.csv'
    df = pd.read_csv('formatted_data_no_bump.csv')
    
    # Call the reorg function to reorganize the data
    reorg(df)
