import pandas as pd
import numpy as np

import load_data

# myCourse = main.courseOption
# myWindow = main.roundOption
# df = load_data.df

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

# analysis_df = df.loc[validCourseCode(myCourse) & validBidWindow(myWindow)]

# from sklearn.model_selection import train_test_split

# X = analysis_df[["term_idx"]]
# y1 = analysis_df[["min_bid"]]
# y2 = analysis_df[["median_bid"]]

# from sklearn.linear_model import LinearRegression

# model1 = LinearRegression().fit(X, y1)
# model1_r2 = model1.score(X, y1)
# coef1 = model1.coef_
# int1 = model1.intercept_

# model2 = LinearRegression().fit(X, y2)
# model2_r2 = model1.score(X, y2)
# coef2 = model1.coef_
# int2 = model1.intercept_

# print("Linear Regression Model")
# print("--------------------------")
# print("Min Bid")
# print(f"Features : {X.columns.tolist()}")
# print(f"Coefficients: {coef1[0]}")
# print(f"Intercept : {int1[0]}")
# print(f"Coeff of Determination : {model1_r2}")

# print("--------------------------")
# print("Median Bid")
# print(f"Features : {X.columns.tolist()}")
# print(f"Coefficients: {coef2[0]}")
# print(f"Intercept : {int2[0]}")
# print(f"Coeff of Determination : {model2_r2}")
# print()

# predictedMinBid = model1.predict([[analysis_df['term_idx'].max()+1]]).tolist()
# predictedMedianBid = model2.predict([[analysis_df['term_idx'].max()+1]]).tolist()

# print(type(predictedMinBid[0][0]))
# print(type(predictedMedianBid[0][0]))

# print(f"Min Bid: {predictedMinBid}")
# print(f"Median Bid: {predictedMedianBid}")

def BidRegression(course, round, df):
    analysis_df = df.loc[validCourseCode(df, course) & validBidWindow(df, round)]

    from sklearn.model_selection import train_test_split

    X = analysis_df[["term_idx"]]
    y1 = analysis_df[["min_bid"]]
    y2 = analysis_df[["median_bid"]]

    from sklearn.linear_model import LinearRegression

    model1 = LinearRegression().fit(X, y1)
    model1_r2 = model1.score(X, y1)
    coef1 = model1.coef_
    int1 = model1.intercept_

    model2 = LinearRegression().fit(X, y2)
    model2_r2 = model1.score(X, y2)
    coef2 = model1.coef_
    int2 = model1.intercept_

    return model1.predict([[analysis_df['term_idx'].max()+1]]).tolist(), model2.predict([[analysis_df['term_idx'].max()+1]]).tolist()