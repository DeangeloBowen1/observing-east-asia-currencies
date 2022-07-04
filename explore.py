import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

import warnings
warnings.filterwarnings('ignore')

from itertools import combinations

import wrangle as w


def set_percentages(df):
    '''Sets gain or loss percentages based on current currency data '''
    df['USD_YEN']= (df['JPYEN'] - 100)
    df['USD_HKD'] = (df['HKD'] - 10) * 10
    df['USD_YUAN'] = (df['CHYUAN'] - 10) * 10
    df['USD_WON'] = (df['KRWON']/1000) * 10
    df['USD_SPD'] = (df['SPD'] - 1) * 100
    df['USD_TWD'] = (df['TWD'] - 30) * 10
    df['USD_THB'] = (df['THB'] - 30)


def split_data(df):
    '''splits data into train and test splits for time series analysis'''
    train_size = 0.70 # 70% train, 30% test
    n = df.shape[0]
    test_start_index = round(train_size * n)

    train = df[:test_start_index] # Everything up to but not including the test_start_index
    test = df[test_start_index:] # Everything from the test_start_index to the end
    return train, test



def visualize_splits(df):
    '''Visualizes the 70%/30% split on graph of the specified columns'''
    for col in train.columns[0:7]:
        plt.figure(figsize=(10,8))
        plt.title(f'{col} to US Dollar')
        plt.plot(train[col])
        plt.plot(test[col])
        plt.show()
        

def get_boxplots(df):
    plt.figure(figsize=(15,20))
    
    for cnt, col in enumerate(df.columns[0:7]):
        plt.subplot(4,2, cnt+1)
        ax = sns.boxplot(data=train, x='month', y=train[col], order=np.sort(df['month'].unique()))
        plt.title(f'2017-2021 Average USD to {col} % on Conversion')
        ax.set_xticklabels([t.get_text()[3:] for t in ax.get_xticklabels()],
                   rotation=0);
        plt.xlabel(' ')
        plt.ylabel(' ')
        #ax.get_figure().autofmt_xdate()
    plt.tight_layout()


def plot_cot(df):
    plt.figure(figsize=(20,20))
    
    for cnt, col in enumerate(df.columns[9:16]):
        y = df[col]
        
        plt.subplot(4,2, cnt+1)
        
        y.plot(alpha=.2, label='Hourly')
        y.resample('D').mean().plot(alpha=0.5, label='Daily')
        y.resample('W').mean().plot(alpha=0.8, label='Weekly')
        y.resample('M').mean().plot(label='Monthly')
        y.resample('Y').mean().plot(label='Yearly',  xlabel=' ')
        plt.title(f'{col} Percent (%) Change Over Time')
        plt.tight_layout()
        plt.legend()


def get_volatility(df):
    plt.figure(figsize=(15,15))
    
    for cnt, col in enumerate(df.columns[0:7]):
        y = df[col]
        
        plt.subplot(4,2, cnt+1)
        y.resample('M').mean().diff().plot(title=f'Volitility of the USD to {col} Over Time', xlabel= ' ')
    plt.tight_layout()


def get_autocorrelation(df):
    plt.figure(figsize=(15,15))
    for cnt, col in enumerate(df.columns[0:7]):
        y = df[col]
        plt.subplot(4,2, cnt+1)
        pd.plotting.autocorrelation_plot(y.resample('W').mean())
        plt.title(f'Identifying Seasonality in {col}')
    plt.tight_layout()



def get_yen_autocorrelation(df):
    plt.figure(figsize=(15,15))
    for cnt, col in enumerate(df.columns[1:7]):
        plt.subplot(4,2, cnt+1)
        y = train.JPYEN
        x = train[col]

        y.resample('M').mean().diff().plot(title=f'Volitility of the Japanese Yen vs {col} Over Time', xlabel= ' ')
        x.resample('M').mean().diff().plot(title=f'Volitility of the Japanese Yen vs {col} Over Time', xlabel= ' ')
        plt.legend()
        plt.tight_layout()
            

        
                

    
    


    
    
