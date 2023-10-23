import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import load_data

def validCourseCode(df, string):
    if string is '':
        return True
    else:
        return (df['course_code'] == string)

def validBidWindow(df, string):
    if string is '':
        return True
    else:
        return (df['bidding_window'] == string)

def validProf(df, string):
    if string is None:
        return True
    else:
        return (df['instructor'] == string)
    
def lessThanTen(bidPrice):
    if bidPrice[0][0] < 10:
        return 10.0
    else:
        return bidPrice

def get_analysis_df(course, round, prof, df):
    return df.loc[validCourseCode(df, course) & validBidWindow(df, round) & validProf(df, prof)]

def BidRegression(df):
    #analysis_df = get_analysis_df(course, round, prof, df)
    #analysis_df = df.loc[validCourseCode(df, course) & validBidWindow(df, round) & validProf(df, prof)]

    from sklearn.model_selection import train_test_split

    X = df[["term_idx"]]
    y1 = df[["min_bid"]]
    y2 = df[["median_bid"]]

    from sklearn.linear_model import LinearRegression

    model1 = LinearRegression().fit(X, y1)
    model2 = LinearRegression().fit(X, y2)

    minBid = model1.predict([[df['term_idx'].max()+1]]).tolist()
    medBid = model2.predict([[df['term_idx'].max()+1]]).tolist()

    minBidScore = model1.score(X, y1)
    medBidScore = model2.score(X, y2)

    # Regression Plots

    fig, axs = plt.subplots(ncols=2, figsize=(12,4))

    termsList = ['2020-21 Term 1', '2020-21 Term 2', '2019-20 Term 1', '2019-20 Term 2',
                        '2021-22 Term 1', '2021-22 Term 2', '2022-23 Term 1', '2022-23 Term 2']
        
    sns.regplot(x='term_idx', y='median_bid', data=df, ax=axs[0])
    sns.regplot(x='term_idx', y='min_bid', data=df, ax=axs[1])

    for ax in axs:
        ax.set_xticklabels(termsList)
        ax.set_xlabel("Term")
        plt.setp(ax.get_xticklabels(), rotation=40)

    axs[0].set_ylabel("Median Bid")
    axs[1].set_ylabel("Min Bid")

    return lessThanTen(minBid), lessThanTen(medBid), fig, minBidScore, medBidScore