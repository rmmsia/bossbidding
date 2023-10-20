import streamlit as st
import pandas as pd
import load_data
import regression

st.header("BOSS Bidding Analysis")
st.write("DISCLAIMER: The predictions are not 100% accurate. Please use them as a reference only.")
st.write("We are not responsible for any unsuccessful bids that you make.")
courseList = load_data.df['course_code'].sort_values()
courseOption = st.selectbox("Course", courseList.unique())

roundList = load_data.df['bidding_window'].sort_values()
roundOption = st.selectbox("Round", roundList.unique())

minBid, medBid = regression.BidRegression(courseOption, roundOption, load_data.df)

st.write(f"Predicted Minimum Bid: {round(minBid[0][0], 2)}")
st.write(f"Predicted Median Bid: {round(medBid[0][0], 2)}")