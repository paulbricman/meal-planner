import streamlit as st
import calendar
from util import *


st.set_page_config(
    page_title='🥗 meal planner',
    layout='wide')


hide_streamlit_style = '''
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                </style>
                '''
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
st.markdown('# 🥗 meal planner')

cols = st.columns(2)

st.session_state['season'] = cols[0].selectbox('season', ['winter', 'summer'])

if cols[0].button('generate new plan'):
    st.experimental_rerun()

st.markdown('---')
cols = st.columns(2)
meals = ['breakfast', 'morning snack', 'lunch', 'afternoon snack', 'dinner']
plan = generate_prune_plan('1x1')

for meal in meals:
    cols[0].markdown('##### ' + plan[0][meal][0])
    cols[0].markdown(', '.join(plan[0][meal][1]))
    cols[0].markdown('')

cols[1].markdown('#### 🛒 shopping list')
all_ingredients = [plan[0][meal][1] for meal in meals]
all_ingredients = set(
    [elem for sublist in all_ingredients for elem in sublist])
all_ingredients = '\n'.join(['- [ ] ' + e for e in all_ingredients])
cols[1].text(all_ingredients)

st.markdown('---')
