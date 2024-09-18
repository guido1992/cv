# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 09:29:03 2021

@author: Alex
"""
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from wordcloud import WordCloud
import datetime as dt

# Title App
#st.image(r'C:\Users\Alex\Desktop\Laduma_Analytics\Laduma.png', use_column_width=True)

# Title my App
st.title("Alex Rathke CV")

# Personal details
st.markdown('Data Analyst | rathkealex@gmail.com')

# Profile header
st.subheader("Profile:" )
st.markdown('A motivated & energetic professional analyst working in elite performance environments. Analytically minded with a high level of initiative and comprehensive communication skills.\n Holds the ability to produce high-quality reports, visualisations under pressure and experience in numerous sectors of business.')

# Gantt chart header
st.subheader('My Career')
st.markdown("Below is the breakdown of my career so far. Please hover over each bar to find out more about the role in that position." )

# Create df for Gantt chart
df = pd.DataFrame([
    dict(Task1="Manipulate data through Alteryx and/or Python.",
         Task2='Design & maintain Tableau dashboards for customers & colleagues.',
         Task3='General incoming reporting tasks.',
         Start='2018-06-01', Finish='2021-12-31', Sector='Business', Job_Title="Data Analyst", Employer='Aon Analytics Centre'),
    
    dict(Task1="Team & Player analysis.",
         Task2='Statistical modelling and explanation of data.',
         Task3='Data visualisation.',
         Start='2019-06-01', Finish='2021-12-31', Sector='Sport', Job_Title="Data Journalist", Employer='Bet Central'),
    
    dict(Task1="Player recruitment analysis.",
         Task2='SWOT analysis of team.',
         Task3='Champions & Europa League opposition analysis.',
        Start='2019-06-01', Finish='2019-10-30', Sector='Sport', Job_Title="Data Analyst", Employer='Dundalk FC'),
    
    dict(Task1="Player recruitment analysis.",
         Task2='League, Team & Player playing styles.',
         Task3='Data visualisation and report writing.',
        Start='2019-01-01', Finish='2019-08-01', Sector='Sport', Job_Title="Data Analyst", Employer='Brand Athlete Management'),
    
    dict(Task1="Match day statistical collection.",
         Task2='Data analysis & Team + Player post-match statistical visualisation.',
         Task3='Opposition analysis through video & data analysis.',
         Start='2019-06-30', Finish='2017-09-01', Sector='Sport', Job_Title="Performance & Data Analyst", Employer='Tipperary Football'),
    
    dict(Task1="Opposition scouting & set-piece analysis.",
         Task2='Player profiling for recruitment.',
         Task3='xxxx',
         Start='2018-05-18', Finish='2017-09-01', Sector='Sport', Job_Title="Performance Analyst", Employer='Doha, Qatar'),
    
    dict(Task1="Analyse media content to help websites and business make better business decisions.",
         Task2='Using a variety of Google based tools.',
         Start='2017-04-18', Finish='2018-05-31', Sector='Business', Job_Title="Content Analyst", Employer="Arvato"),
    
    dict(Task1="Talk show analysing teams & players from the German Bundesliga.",
         Task2='Presented statistical metrics.',
         Task3='Wrote script and collated video, data, and script.',
         Start='2016-05-01', Finish='2017-06-30', Sector='Sport', Job_Title="Guest TV Analyst", Employer='StarTimes Media'),
    
    dict(Task1="Build a system of analysis for school to perform adhoc duties after contract ended.",
         Task2='Analysis of different sports.',
         Task3='Use of Excel, Tableau, Hudl and video analysis.',
         Start='2016-11-16', Finish='2017-04-01', Sector='Sport', Job_Title="Performance Analyst", Employer='Rydal Penrhos School'),
    
    dict(Task1="Build analysis system for academy coaches to use.",
         Task2='Video of academy games and first-team matches.',
         Task3='Opposition set piece analysis for first-team on game by game basis.',
         Start='2016-05-15', Finish='2016-09-30', Sector='Sport', Job_Title="Performance Analyst", Employer='Houston Dynamo'),
    
    dict(Task1="Football coach on summer camps in Germany.",
         Task2='Supervision of children on a weekly summer camp.',
         Task3='Organised activities, session plans and ensuring order at camp.',
         Start='2015-07-01', Finish='2015-08-30', Sector='Sport', Job_Title="Football Coach", Employer='FerienFussball'),
    
    dict(Task1="Football coach on summer camps in Germany.",
         Task2='Supervision of children on a weekly summer camp.',
         Task3='Organised activities, session plans and ensuring order at camp.',
         Start='2014-07-01', Finish='2014-08-30', Sector='Sport', Job_Title="Football Coach", Employer='FerienFussball'),
    
    dict(Task1="Video recorded first-team games.",
         Task2='Used SportsCode to clip games into technical and tactical aspects.',
         Start='2014-01-07', Finish='2014-06-30', Sector='Sport', Job_Title="Performance Analyst", Employer='UCD Rugby Club'),
    
    dict(Task1="Developed a club database of former & current players/board members.",
         Task2='Co-ordinated and lead organisation of Irish University Championships.',
         Start='2013-06-01', Finish='2014-04-30', Sector='Sport', Job_Title="Club Administrator", Employer="UCD Women's Soccer Club")
])

# Gantt chart of employment
fig = px.timeline(df, x_start="Start", x_end="Finish", y="Employer",
                  hover_data=["Task1", "Task2", "Task3", "Job_Title"],
                  title='Employment history')

# Sort gantt chart
#fig.update_yaxes(autorange="reversed")

# Size of figure set
fig.update_layout(
    width=1000,
    height=500
)

# Plot Plotly figure
st.plotly_chart(fig)

# Header
st.subheader('My Skills')

# Text about skills
st.markdown('Below are the skills I have gained so far in my experience as a Data Analyst professional.')

# Add Skills - Create skills in text format
text = 'Tableau, Alteryx, Python, SQL, Excel, Trifacta, AWS, SportsCode, NacSport, Opta, Statsbomb, InStat, Wyscout'

# Create and generate a word cloud image:
wordcloud = WordCloud().generate(text)

# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()

# References
st.markdown('References avaiable on request')
