import streamlit as st
import json
from Myfunction import Api

with open("possibles_values_2.json", "r") as json_file:
    possibles_values = json.load(json_file)


st.title("Welcome to Data Job Salary Estimator by Super-Hughhh")

st.write("#")
st.write("##")

col1, col2, col3 = st.columns(3)
col4, col5, col6 = st.columns(3)


with col1:
    experience_level_choice = st.selectbox('EXPERIENCE LEVEL', possibles_values['experience_level_choice'])
with col2:
    remote_ratio_choice = st.selectbox('REMOTE RATIO', possibles_values['remote_ratio_choice'])
with col3:
    company_size_choice = st.selectbox('COMPANY SIZE', possibles_values['company_size_choice'])
with col4:
    job_title_choice = st.selectbox('JOB', possibles_values['job_title_choice'])
with col5:
    company_country_location_choice = st.selectbox('COMPANY LOCATION', possibles_values['company_country_location_choice'])
with col6:
    employee_country_residence_choice = st.selectbox('EMPLOYEE LOCATION', possibles_values['employee_country_residence_choice'])

st.write("#")

button = st.button("SALARY ESTIMATION", type="primary")

if button:
    res = Api.get_data2(job_title=job_title_choice,
                        company_size=company_size_choice,
                        company_country_location=company_country_location_choice,
                        experience_level=experience_level_choice,
                        employee_country_residence=employee_country_residence_choice,
                        remote_ratio=remote_ratio_choice)
    st.write("#")
    st.subheader(f'According to our estimate...')
    st.subheader(f'you can expect a salary of:green[ $ {res}]')
