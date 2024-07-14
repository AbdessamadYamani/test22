import streamlit as st
import subprocess

def run_powershell_command(command):
    # This function would need to be adapted based on your chosen approach
    result = subprocess.run(["powershell", "-Command", command], capture_output=True, text=True)
    return result.stdout

st.title("My Azure CLI App")

if st.button("Run Azure Command"):
    result = run_powershell_command("az login")
    st.text(result)