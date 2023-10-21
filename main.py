import streamlit as st
import pandas as pd
import load_data
import regression

st.header("BOSS Bidding Analysis")
st.write("DISCLAIMER: The predictions are not 100% accurate. Please use them as a reference only.")
st.write("We are not responsible for any unsuccessful bids that you make.")

df = load_data.load_data()

courseList = df['code_title'].sort_values()
selection = st.selectbox("Course", courseList.unique())
courseOption = df.loc[df['code_title'] == selection, 'course_code'].iloc[0]

roundList = df['bidding_window'].sort_values()
roundOption = st.selectbox("Round", roundList.unique())

try:
    minBid, medBid, fig = regression.BidRegression(courseOption, roundOption, df)
    with st.container():
        st.write(f"Predicted Minimum Bid: {round(minBid[0][0], 2)}")
        st.write(f"Predicted Median Bid: {round(medBid[0][0], 2)}")
        st.pyplot(fig)

except ValueError:
    st.write("Currently no data for this course and round. Choose a different course and/or round.")

st.divider()
st.text("v1.1.0")
