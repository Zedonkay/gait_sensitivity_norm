import pandas as pd
import scipy.stats as stats



def main():
    df = pd.read_csv('vertices.csv')
    zs = df['z'].values
    zs = zs[~pd.isnull(zs)]
    zs = zs[zs != 0]
    print(stats.entropy(zs))
    #7.068082566362332

if __name__ == "__main__":
    main()