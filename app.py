import streamlit as st
import joblib
import numpy as np

# Load the trained model using joblib
model = joblib.load('model.pkl')

# Centered title using HTML
st.markdown("""
    <h1 style='text-align: center;'>
        Student Dropout Prediction<br>
        <span style='font-size: 36px;'>Jaya Jaya Institute</span>
    </h1>
""", unsafe_allow_html=True)

st.markdown("##### ")

st.write("Please enter the student's information:")

# Input form for top 10 features
Age_at_enrollment = st.number_input("Age at Enrollment", min_value=0)
Admission_grade = st.number_input("Admission Grade", min_value=0.0, format="%.2f")
Tuition_fees_up_to_date = st.selectbox("Tuition Fees Up to Date", ["No", "Yes"])
Previous_qualification_grade = st.number_input("Previous Qualification Grade", min_value=0.0, format="%.2f")

# Input Semester 1
col1, col2, col3 = st.columns(3)
with col1:
    Curricular_units_1st_sem_approved = st.number_input(
        'Curricular Units Approved (S1)', min_value=0)
with col2:
    Curricular_units_1st_sem_evaluations = st.number_input(
        'Curricular Units Evaluations (S1)', min_value=0)
with col3:
    Curricular_units_1st_sem_grade = st.number_input(
        'Curricular Units Grade (S1)', min_value=0.0, format="%.2f")

col4, col5, col6 = st.columns(3)
with col4:
    Curricular_units_2nd_sem_approved = st.number_input(
        'Curricular Units Approved (S2)', min_value=0)
with col5:
    Curricular_units_2nd_sem_evaluations = st.number_input(
        'Curricular Units Evaluations (S2)', min_value=0)
with col6:
    Curricular_units_2nd_sem_grade = st.number_input(
        'Curricular Units Grade (S2)', min_value=0.0, format="%.2f")

# Convert categorical value to numerical (Yes = 1, No = 0)
Tuition_fees_up_to_date_val = 1 if Tuition_fees_up_to_date == "Yes" else 0

# Create a feature array for prediction
features = np.array([[ 
    Curricular_units_2nd_sem_approved,
    Curricular_units_2nd_sem_grade,
    Curricular_units_1st_sem_approved,
    Tuition_fees_up_to_date_val,
    Curricular_units_1st_sem_grade,
    Age_at_enrollment,
    Admission_grade,
    Curricular_units_2nd_sem_evaluations,
    Previous_qualification_grade,
    Curricular_units_1st_sem_evaluations
]])

st.markdown("")

# Prediction button
if st.button("Predict Dropout"):
    prediction = model.predict(features)[0]
    if prediction == 0:
        st.error("Prediction Result: The student is at risk of dropping out.")
    else:
        st.success("Prediction Result: The student is likely to continue their studies.")