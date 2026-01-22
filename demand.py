# this calculates the base growth rate g(t) 
import pandas as pd 

def base_growth(start_year, end_year):
    df = pd.read_csv(
        't2data.csv',
        comment='#',
        nrows=5
    )

    df['Year'] = df['Year'].astype(int)

    T_start = df.loc[df['Year'] == start_year, 'Tourist count (million)'].iloc[0]
    T_end   = df.loc[df['Year'] == end_year,   'Tourist count (million)'].iloc[0]

    n = end_year - start_year
    return (T_end / T_start) ** (1 / n) - 1

