# import pandas for dataframe manipulation
import pandas as pd

# import numpy for mathematical calculations
import numpy as np

import os


# acquire data or create dataframe
def acquire_data(use_cache=False):
    """
    The purpose of this function is to acquire the created dataset that stores
    the information obtained on current currency values vs the usd.

    If no such csv exists, a csv will be created.
    
    """
    filename = 'dollarvs_data.csv'

    if os.path.isfile(filename) and use_cache:
        return pd.read_csv(filename)
    else:
        # obtain the csv's
        usd = pd.read_csv('USDINDEX.csv')
        jpy = pd.read_csv('DEXJPUS.csv').copy()
        hk = pd.read_csv('DEXHKUS.csv').copy()
        ch = pd.read_csv('DEXCHUS.csv').copy()
        kr = pd.read_csv('DEXKOUS.csv').copy()
        si = pd.read_csv('DEXSIUS.csv').copy()
        tw = pd.read_csv('DEXTAUS.csv').copy()
        th = pd.read_csv('DEXTHUS.csv').copy()

        # merge the csvs into one dataframe
        merge1 = pd.merge(jpy, hk, on='DATE')
        merge2 = pd.merge(merge1, ch, on='DATE')
        merge3 = pd.merge(merge2, kr, on='DATE')
        merge4 = pd.merge(merge3, si, on='DATE')
        merge5 = pd.merge(merge4, tw, on='DATE')
        merge6 = pd.merge(merge5, th, on='DATE')
        df = pd.merge(merge6, usd, on='DATE')

        df['USD_Actual'] = '1.00'

        # change to proper datatimes and astypes
        df['DATE'] = df['DATE'].astype('datetime64')
        
        for col in df.columns[1:10]:
            df[col] = pd.to_numeric(df[col],errors='coerce')

        # rename columns
        df = df.rename(columns={'DEXJPUS': 'JPYEN', 'DEXHKUS':'HKD',
                        'DEXCHUS':'CHYUAN', 'DEXKOUS':'KRWON',
                        'DEXSIUS':'SPD', 'DEXTAUS':'TWD',
                        'DEXTHUS':'THB', 'DTWEXBGS':'USD_Index'})
        
        df.set_index('DATE', inplace=True)
        
        df['month'] = df.index.strftime('%m-%b')

        #create dataframe
        df.to_csv('dollarvs_data.csv', index=False)
        return df

        
        

        
                

    
    


    
    
