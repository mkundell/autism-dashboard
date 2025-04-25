import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(layout="wide")
st.title("🧠 Autism Screening Dashboard")

# Load the dataset directly (assuming it's uploaded to your GitHub repo)
df = pd.read_csv("autism_data.csv")  # Make sure this matches your actual file name

st.subheader("Data Overview")
st.dataframe(df.head())

st.write("Shape:", df.shape)

st.subheader("Value Counts (Ethnicity & Relation)")
col1, col2 = st.columns(2)
with col1:
    st.bar_chart(df['ethnicity'].value_counts())
with col2:
    st.bar_chart(df['relation'].value_counts())

df = df.replace({'yes': 1, 'no': 0, '?': 'Others', 'others': 'Others'})

st.subheader("Target Distribution")
fig1, ax1 = plt.subplots()
ax1.pie(df['Class/ASD'].value_counts(), autopct='%1.1f%%', labels=['No', 'Yes'])
st.pyplot(fig1)

st.subheader("Feature-wise Distribution by Class/ASD")

ints = [col for col in df.columns if df[col].dtype.kind in 'i']
objects = [col for col in df.columns if df[col].dtype == object]

if 'ID' in ints: ints.remove('ID')
if 'Class/ASD' in ints: ints.remove('Class/ASD')

st.markdown("### Integer Columns")
for col in ints:
    st.write(f"**{col}**")
    fig2, ax2 = plt.subplots()
    sns.countplot(x=col, hue='Class/ASD', data=df, ax=ax2)
    st.pyplot(fig2)

st.markdown("### Categorical Columns")
for col in objects:
    st.write(f"**{col}**")
    fig3, ax3 = plt.subplots()
    sns.countplot(x=col, hue='Class/ASD', data=df, ax=ax3)
    ax3.tick_params(axis='x', rotation=45)
    st.pyplot(fig3)
