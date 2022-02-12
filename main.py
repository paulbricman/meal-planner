import streamlit as st
import calendar
from util import *


st.set_page_config(
    page_title='🥗 meal planner')


hide_streamlit_style = '''
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                </style>
                '''
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
st.markdown('# 🥗 meal planner')

st.session_state['season'] = st.selectbox('season', ['winter', 'summer'])

if st.button('generate new plan'):
    st.experimental_rerun()

st.markdown('---')
meals = ['breakfast', 'lunch', 'dinner', 'morning snack']
plan = generate_prune_plan('1x1')

for meal in meals:
    st.markdown('##### ' + plan[0][meal][0])
    for ingredient in plan[0][meal][1]:
        st.text('- [ ] ' + ingredient)
    st.markdown('')
