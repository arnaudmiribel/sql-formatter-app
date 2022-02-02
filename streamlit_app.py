import sqlparse
import streamlit as st

st.title("SQL Formatter")

query = st.text_area("Input SQL to be formatted")
st.caption("Output")
st.code(sqlparse.format(query, reindent=True, keyword_case="lower"), "sql")
