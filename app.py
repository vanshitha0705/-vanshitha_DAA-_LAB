import subprocess
import sys
import streamlit as st

# Configure the page layout
st.set_page_config(page_title="DAA Lab UI", page_icon="🧠", layout="centered")

st.title("Design & Analysis of Algorithms Lab")
st.write(
    "Select an experiment from the sidebar to view and execute its analysis."
)

# Sidebar dropdown configuration
option = st.sidebar.selectbox(
    "Choose DAA Experiment",
    [
        "Experiment 1",
        "Experiment 2",
        "Experiment 3",
        "Experiment 4",
        "Experiment 5",
        "Experiment 6",
    ],
)

st.divider()


# Helper function to safely execute your python scripts and capture output
def run_script(script_name):
    try:
        # sys.executable ensures it runs using the current Python environment
        result = subprocess.run(
            [sys.executable, script_name],
            capture_output=True,
            text=True,
            check=True,
        )
        return (
            result.stdout
            if result.stdout
            else "Script executed successfully with no console output."
        )
    except subprocess.CalledProcessError as e:
        return f"Error running script:\n{e.stderr}"
    except FileNotFoundError:
        return f"File {script_name} not found in repository."


# Execution Logic Routing
experiments = {
    "Experiment 1": "exp.1.py",
    "Experiment 2": "exp.2.py",
    "Experiment 3": "exp.3.py",
    "Experiment 4": "exp.4.py",
    "Experiment 5": "exp.5.py",
    "Experiment 6": "exp.6.py",
}

if option in experiments:
    script_file = experiments[option]
    st.subheader(f"{option} Execution Output")
    if st.button(f"Run {option} Code"):
        with st.spinner("Calculating..."):
            output = run_script(script_file)
            st.code(output, language="text")
