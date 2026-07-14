import streamlit as st

st.title(" DAA Lab Experiments UI")
st.write("Select an experiment from the sidebar to run it.")

# Sidebar dropdown menu
selection = st.sidebar.selectbox("Choose Experiment", ["Experiment 1", "Experiment 2", "Experiment 3", "Experiment 4"])

if selection == "Experiment 1":
    st.header("Experiment 1: Analysis")
    # Paste your exp.1.py code logic right here!
    
elif selection == "Experiment 2":
    st.header("Experiment 2: Analysis")
    # Paste your exp.2.py code logic right here!

# Do the same for 3 and 4!
