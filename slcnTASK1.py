#pandas,NumPy,matplotlib
import pandas as pd

#loading the dataset
df = pd.read_csv('student_performance.csv')
#print(df.head())

#total number of students = total rows
total_stu = len(df)
print("Total number of students:", total_stu)

#studied more than 2 hrs

morethan2 = df[df['study_hours_per_day'] > 2]
print("Students who studied > 2 hours:", len(morethan2))

#students who passed
passed = df[df['exam_score']>=35]
print("number of students who passed: ", len(passed))

#students who studied more than 2hrs and passed
studyAndpassed = df[(df['study_hours_per_day']>2)  & (df['exam_score'] >= 35)]
print("no. of students who studied > 2 hrs and passed: ", len(studyAndpassed))

#Percentage of students who passed among those who studied > 2 hours
percent_passed = (len(studyAndpassed)/len(morethan2))*100
print("Percentage of students who passed among those who studied > 2 hours = ", percent_passed)



