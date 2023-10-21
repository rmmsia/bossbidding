import os
import xlrd
import pandas as pd
import streamlit as st
import gcsfs
import json

import warnings
warnings.filterwarnings('ignore')

# path = os.getcwd() + '/BOSS Results'
# files = os.listdir(path)
# files_xls = [f for f in files if f[-3:] == 'xls']
# files_xls

@st.cache_data
def load_data():
    df = pd.DataFrame()

    das_json = dict(st.secrets["toAuth"]["settings"])
    project_id = st.secrets["the_secret"]

    gcs = gcsfs.GCSFileSystem(project=project_id, token=das_json)

    bucket_name = 'boss-streamlit'
    folder_path = 'BOSS Results'

    file_list = gcs.glob(f'{bucket_name}/{folder_path}/*.xls')

    print(file_list)

    for file in file_list:
        with gcs.open(file, 'rb') as f:
            print(f"Now reading: {file}")
            data = pd.read_excel(f, 'sheet1')
            df = df._append(data)
            print(f"Finished reading: {file}")
    
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

    df["code_title"] = df["course_code"].astype(str) + " - " + df["description"].astype(str)

    return df

df = load_data()
