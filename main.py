import streamlit as st
import pandas as pd
import load_data
import regression
import utils

st.header("BOSS Bidding Analysis")
st.write("DISCLAIMER: The predictions are not 100% accurate. Please use them as a reference only.")
st.write("We are not responsible for any unsuccessful bids that you make.")

df = load_data.load_data()

courseList = df['code_title'].sort_values()
selection = st.selectbox("Course", courseList.unique())
courseOption = df.loc[df['code_title'] == selection, 'course_code'].iloc[0]

roundList = df['bidding_window'].sort_values(key=lambda x: x.map(utils.window_sort))
roundOption = st.selectbox("Round", roundList.unique())

profList = df.loc[df['course_code'] == courseOption, 'instructor']
# profList = df['instructor'].sort_values()
#pd.concat([profList, pd.Series(['N/A'])], ignore_index=True)
profOption = st.selectbox("Professor", profList.unique(), index=None)

filtered_df = regression.get_analysis_df(courseOption, roundOption, profOption, df)

try:
    minBid, medBid, fig, minBidScore, medBidScore = regression.BidRegression(filtered_df)
    with st.container():
        try:
            st.write(f"Predicted Minimum Bid: {round(minBid, 2)}")
        except TypeError:
            st.write(f"Predicted Minimum Bid: {minBid}")
        try:
            st.write(f"Predicted Median Bid: {round(medBid, 2)}") 
        except TypeError:
            st.write(f"Predicted Median Bid: {medBid}")
        st.pyplot(fig)
        st.write(f"Min Bid r²: {round(minBidScore, 4)}")
        st.write(f"Med Bid r²: {round(medBidScore, 4)}")

        if minBidScore < 0.5 or medBidScore < 0.5:
            st.write(f":red[Warning]: r² is low (< 0.5). The prediction may be wildly inaccurate.")

except ValueError:
    st.write("Currently no data for this course and round. Choose a different course and/or round.")

st.divider()
st.text("v1.3.2")
