import streamlit as st
import pickle
import pandas as pd

teams = ['Sunrisers Hyderabad',
 'Mumbai Indians',
 'Royal Challengers Bengaluru',
 'Kolkata Knight Riders',
 'Rajasthan Royals',
 'Chennai Super Kings',
 'Delhi Capitals',
 'Punjab Kings',
 'Lucknow Super Giants',
 'Gujarat Titans']

venues = ['M Chinnaswamy Stadium, Bengaluru',
       'Punjab Cricket Association Stadium, Mohali',
       'Arun Jaitley Stadium, Delhi', 'Wankhede Stadium, Mumbai',
       'Sawai Mansingh Stadium, Jaipur',
       'MA Chidambaram Stadium, Chennai', 'Eden Gardens, Kolkata',
       'Dr DY Patil Sports Academy, Mumbai', 'Newlands, Cape Town',
       "St George's Park, Port Elizabeth", 'Kingsmead, Durban',
       'SuperSport Park, Centurion', 'Buffalo Park, East London',
       'New Wanderers Stadium, Johannesburg',
       'De Beers Diamond Oval, Kimberley',
       'OUTsurance Oval, Bloemfontein', 'Brabourne Stadium, Mumbai',
       'Narendra Modi Stadium, Ahmedabad',
       'Himachal Pradesh Cricket Association Stadium, Dharamsala',
       'Maharashtra Cricket Association Stadium, Pune',
       'Rajiv Gandhi International Stadium, Hyderabad',
       'Shaheed Veer Narayan Singh International Stadium, Raipur',
       'JSCA International Stadium Complex, Ranchi',
       'Zayed Cricket Stadium, Abu Dhabi',
       'Sharjah Cricket Stadium, Sharjah',
       'Dubai International Cricket Stadium, Dubai',
       'Barabati Stadium, Cuttack',
       'Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium, Visakhapatnam',
       'Holkar Cricket Stadium, Indore',
       'Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium, Lucknow',
       'Barsapara Cricket Stadium, Guwahati',
       'Maharaja Yadavindra Singh International Cricket Stadium, Mullanpur']

pipe = pickle.load(open('pipe.pkl', 'rb'))

st.title('IPL Win Predictor')

col1, col2 = st.columns(2)
with col1:
    batting_team = st.selectbox('Select the batting team', sorted(teams))

with col1:
 bowling_team = st.selectbox('Select the bowling team', sorted(teams))


selected_venue = st.selectbox("Select the venue", sorted(venues))

target = st.number_input("Target", step=1)
col3, col4, col5 = st.columns(3)

with col3:
    score = st.number_input("Score", step=1)
    
with col4:
    overs = st.number_input("Overs completed", step=1)
    
with col3:
    wickets = st.number_input("Wickets lost", step=1)


if st.button('Predict Probability'):
    runs_left = target - score
    balls_left = 120-(overs*6)
    wickets = 10 - wickets
    crr = score/overs
    rrr = runs_left*6/balls_left

    input_df = pd.DataFrame({'batting_team':[batting_team],'bowling_team':[bowling_team],'venue':[selected_venue],'required_runs':[runs_left],'balls_left':[balls_left],'wickets_left':[wickets],'total_runs_x':[target],'CRR':[crr],'RRR':[rrr]})
    # st.table(input_df)

    result = pipe.predict_proba(input_df)
    loss = result[0][0]
    win = result[0][1]
    st.header(batting_team + "- " +str(round(win*100))+"%")
    st.header(bowling_team + "- " + str(round(loss*100)) + "%")
