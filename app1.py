import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
df = pd.read_csv(r"C:/Users/karth/Downloads/understat_per_game.csv")
st.dataframe(df.sample(100))
#How many matches did a specific team win, while they overperfomed their xG for the same match?
selectbox_a = st.selectbox(
    "Choose the team",
    [i for i in df['team'].unique()]
)

selectbox_b = st.selectbox(
    "Choose the season",
    [i for i in df['year'].unique()]
)

df_original = df[df['team'] == selectbox_a]
df_original = df_original[df_original['year'] == selectbox_b]
df_original['difference'] = df_original['xG'] - df_original['xGA']
df_original['points_based_on_xG'] = np.where(df_original['difference'] > 0, 3, 0)
df_new = pd.melt(df_original, id_vars = ['date'], value_vars = ['pts', 'points_based_on_xG'])
plt.figure(figsize = (100, 50))
x = sns.barplot(df_new, x = 'date', y = 'value', hue = 'variable')
st.pyplot(x.get_figure())
