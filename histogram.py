import pandas as pd
import numpy as np
import scipy.stats as stats

def main():
    # Read the data from the CSV file
    df = pd.read_csv('/Users/ishayu/Documents/GitHub/gait_sensitivity_norm/sim_terrain/vertices.csv')
    
    # Extract the 'z' column values from the DataFrame
    zs = df['z'].values
    
    # Remove any NaN values from the 'zs' array
    zs = zs[~pd.isnull(zs)]
    
    # Remove any zero values from the 'zs' array
    zs = zs[zs != 0]
    
    # Calculate the histogram of the 'zs' array to get the probability distribution
    hist, bin_edges = np.histogram(zs, bins='auto', density=True)
    
    # Calculate the entropy of the probability distribution
    entropy = stats.entropy(hist)
    
    # Print the calculated entropy
    print(entropy)

    
    #2.662514259040231 for sim terrain
    #With bump terrain, the entropy is 1.9617905504963942
    #Without bump terrain, the entropy is 1.8801592023022458

if __name__ == "__main__":
    main()
