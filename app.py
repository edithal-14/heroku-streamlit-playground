import streamlit as st

st.write("""
# Divide two number
""")

st.header('User Input Parameters')

def user_input():
  numerator = st.number_input("NUMERATOR", min_value=-999999.0, max_value=999999.0)
  denominator = st.number_input("DENOMINATOR", min_value=-999999.0, max_value=999999.0)

  return {"numerator": numerator, "denominator": denominator}

data = user_input()

st.subheader('User Input parameters')
st.write(data)

st.subheader('Division result')
if data["denominator"] == 0:
  st.write("Denominator cannot be 0")
else:
  st.write(data["numerator"]/data["denominator"])
