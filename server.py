import streamlit as st
import pickle

with open('mushroom_classification.pkl','rb') as f:
    model = pickle.load(f)

st.title("Mushroom Classification")
st.write("This is a Mushroom classification model that can predict 'Weather the mushroom is poisonous or Edible.'")