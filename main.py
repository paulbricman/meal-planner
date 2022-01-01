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
st.markdown('---')

cols = st.columns(6)
mode = cols[0].selectbox('meal prep format', ['3x2+1', '2x3+1'])
if cols[0].button('generate new plan'):
    st.experimental_rerun()

meals = ['breakfast', 'morning snack', 'lunch', 'afternoon snack', 'dinner']
plan = generate_plan(mode)

cols = st.columns(6)
for day_idx, day in enumerate(calendar.day_abbr[0:6]):
    cols[day_idx].markdown('### ' + day.lower())
    cols[day_idx].markdown('')
    cols[day_idx].markdown('')
    

for meal in meals:
    cols = st.columns(6)
    for day_idx, day in enumerate(calendar.day_abbr[0:6]):
        cols[day_idx].markdown('##### ' + plan[day_idx][meal][0])
        cols[day_idx].markdown(', '.join(plan[day_idx][meal][1]))
        cols[day_idx].markdown('')

st.markdown('---')
st.markdown('#### 🛒 shopping list')
    
cols = st.columns(6)
if mode == '3x2+1':
    for day_idx, day in enumerate(calendar.day_abbr[0:6]):
        if day_idx % 2 == 0:
            cols[day_idx].markdown('#### ' + day.lower())
            all_ingredients = [plan[day_idx][meal][1] for meal in meals]
            all_ingredients = set([elem for sublist in all_ingredients for elem in sublist])
            all_ingredients = '\n'.join(['- [ ] ' + e for e in all_ingredients])
            cols[day_idx].text(all_ingredients)
elif mode == '2x3+1':
    for day_idx, day in enumerate(calendar.day_abbr[0:6]):
        if day_idx % 3 == 0:
            cols[day_idx].markdown('#### ' + day.lower())
            all_ingredients = [plan[day_idx][meal][1] for meal in meals]
            all_ingredients = set([elem for sublist in all_ingredients for elem in sublist])
            all_ingredients = '\n'.join(['- [ ] ' + e for e in all_ingredients])
            cols[day_idx].text(all_ingredients)