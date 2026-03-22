import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
st.set_page_config(page_title="Student Dashboard", layout="wide")
st.title("📊 Student Performance Dashboard")
st.sidebar.header("Student Input")
name = st.sidebar.text_input("Student Name", "Nagaraj")
math = st.sidebar.slider("Math Marks", 0, 100, 75)
science = st.sidebar.slider("Science Marks", 0, 100, 80)
english = st.sidebar.slider("English Marks", 0, 100, 70)
history = st.sidebar.slider("History Marks", 0, 100, 65)
cs = st.sidebar.slider("Computer Science Marks", 0, 100, 85)
marks = [math, science, english, history, cs]
subjects = ["Math", "Science", "English", "History", "CS"]
total = sum(marks)
average = total / len(marks)
if average >= 90:
    grade = "A+"
elif average >= 75:
    grade = "A"
elif average >= 60:
    grade = "B"
elif average >= 50:
    grade = "C"
else:
    grade = "Fail"
col1, col2, col3 = st.columns(3)
col1.metric("Total Marks", total)
col2.metric("Average", round(average, 2))
col3.metric("Grade", grade)
st.divider()
st.subheader("📈 Performance Analysis")
col1, col2 = st.columns(2)
fig1, ax1 = plt.subplots()
ax1.bar(subjects, marks)
ax1.set_title("Marks by Subject")
col1.pyplot(fig1)
fig2, ax2 = plt.subplots()
ax2.plot(subjects, marks, marker='o')
ax2.set_title("Performance Trend")
col2.pyplot(fig2)
col3, col4 = st.columns(2)
fig3, ax3 = plt.subplots()
ax3.pie(marks, labels=subjects, autopct='%1.1f%%')
ax3.set_title("Marks Distribution")
col3.pyplot(fig3)
class_data = np.random.randint(40, 100, 50)
fig4, ax4 = plt.subplots()
ax4.hist(class_data)
ax4.set_title("Class Marks Distribution")
col4.pyplot(fig4)
st.subheader("📋 Student Details")
df = pd.DataFrame({
    "Subject": subjects,
    "Marks": marks
})
st.dataframe(df)
st.success("Dashboard Generated Successfully ✅")