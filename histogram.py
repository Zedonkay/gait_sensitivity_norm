import pandas as pd
import numpy as np
from scipy.stats import binned_statistic_2d, entropy

def main():
    # Read the data from the CSV file
    df = pd.read_csv('/Users/ishayu/Documents/GitHub/gait_sensitivity_norm/no_bump/vertices_no_bump.csv')

    zs = df['z'].values  
    zs = zs[~np.isnan(zs) & (zs != 0)]

    zs = zs/zs.sum()
    ent = -np.sum(zs*np.log(zs))    
    print(f"Entropy:{ent}")


if __name__ == "__main__":
    main()
