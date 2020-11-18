#Import libraries
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from pickle import load

#
st.title('2016 Election Modeling')
st.markdown('See how your county voted in the 2016 election relative to its regression predicted vote proportion')

#
df = pd.read_csv('Data/election_full_dataset.csv')
counties = df['countystate'].values

#
label = 'Select a county name from the dropdown menu below (785 largest US counties only)'
county = st.selectbox(label, counties)

#
county_datapoint = df[df['countystate']==county]
features = ['incomeroot','medianageroot','unemployment','bachelorsdegree','white','hispanic',
           'popdensityroot','veteran%root','disability%root','manufacturing/capitaroot',
           'agriculture/capita','mining/capita']
x = county_datapoint[features]
y = county_datapoint['voteproportion'].values[0]*100

#
ss = load(open('Pickles/standard_scaler.pickle', 'rb'))
x = ss.transform(x)

#
lr = load(open('Pickles/linear_regression.pickle', 'rb'))
y_pred = lr.predict(x)[0]*100

#
columns = ['County', 'State', 'Predicted Trump Vote %', 'Actual Trump Vote %']
output = pd.DataFrame(columns=columns)
output.loc[0] = [county.split(',')[0], county.split(',')[-1], y_pred, y]
output.index = [' ']


#
st.table(output)