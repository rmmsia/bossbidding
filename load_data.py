import os
import xlrd
import pandas as pd
import numpy as np
import streamlit as st

import warnings
warnings.filterwarnings('ignore')

path = os.getcwd() + '/BOSS Results'
files = os.listdir(path)
files_xls = [f for f in files if f[-3:] == 'xls']
files_xls

@st.cache_data
def load_data():
    df = pd.DataFrame()

    for f in files_xls:
        data = pd.read_excel(path + '/' + f, 'sheet1')
        df = df._append(data)
    
    # Cleaning

    df.columns = df.columns.str.replace(' ', '_')
    df = df.rename(columns=str.lower)
    df['instructor'] = df['instructor'].str.lstrip()

    df['term'] = df['term'].astype('category')
    df['term_idx'] = df['term'].cat.codes

    print(f"No. of rows before: {len(df.index)}")
    df = df.dropna()
    df = df[df.median_bid != 0.0]
    print(f"No. of rows after: {len(df.index)}")

    return df

df = load_data()