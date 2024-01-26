import streamlit as st
st.title("Hello this is my page")
number = st.radio("click", {1,2})
if number == 1:
    st.write("1 is selected")
else:
    st.write("two")