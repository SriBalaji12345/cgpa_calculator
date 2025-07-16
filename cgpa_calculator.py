import streamlit as st

st.title(" CGPA Calculator - Created by Sri Balaji")

st.write("Enter your semester details below:")
st.info("Note: Subjects with *0 credit points* will not affect your GPA/CGPA calculation.")

total_semesters = st.number_input("Total number of semesters completed (1-8):", min_value=1, max_value=8, step=1)

overall_points = 0
overall_credits = 0

for sem in range(1, total_semesters + 1):
    st.header(f"Semester {sem}")
    num_subjects = st.number_input(f"Number of subjects in Semester {sem}:", min_value=1, step=1, key=f"subjects_{sem}")

    sem_points = 0
    sem_credits = 0

    for subj in range(1, num_subjects + 1):
        st.write(f"Subject {subj}:")
        credit = st.number_input(f"Credit points for Subject {subj}:", min_value=0.0, step=0.5, key=f"credit_{sem}_{subj}")
        grade = st.number_input(f"Grade point you gained (0–10):", min_value=0, max_value=10, step=1, key=f"grade_{sem}_{subj}")
        sem_points += credit * grade
        sem_credits += credit

    if sem_credits > 0:
        sem_gpa = sem_points / sem_credits
        st.success(f"GPA for Semester {sem}: {sem_gpa:.2f}")
    else:
        st.warning(f"No credits entered for Semester {sem}. GPA not calculated.")

    overall_points += sem_points
    overall_credits += sem_credits

if overall_credits > 0:
    cgpa = overall_points / overall_credits
    st.subheader(f" Your Overall CGPA after {total_semesters} semester(s): {cgpa:.2f}")
else:
    st.info("Enter valid data to calculate CGPA.")