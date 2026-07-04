# Imports

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('students.csv')


# Functions to calculate letter grades and pass/fail status


def get_letter_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'
    
def pass_fail(average):
    if average >= 60:
        return 'Pass'
    else:
        return 'Fail'


# Calculate average scores, letter grades, and pass/fail status for each student


df["Average"] = df[["Math", "Science", "English", "History", "Art"]].mean(axis=1)
df["Letter Grade"] = df["Average"].apply(get_letter_grade)
df["Pass//Fail"] = df["Average"].apply(pass_fail)

average_above_90 = df[df["Average"] >= 90]

math_above_95 = df[df["Math"] >= 95]

english_failing = df[df["English"] < 60]

student_with_a_average_but_science_below_85 = df[(df["Average"] >= 90) & (df["Science"] < 85)]

class_average = df["Average"].mean()

class_median = df["Average"].median()

class_std_dev = df["Average"].std()

class_highest = df["Average"].idxmax()

class_lowest = df["Average"].idxmin()


# Sort the DataFrame by average score to find the top and bottom students


sorted_list = df.sort_values(by="Average", ascending=False)
top_10_students = sorted_list.head(10)
bottom_10_students = sorted_list.tail(10)
top_math_students = df.sort_values(by="Math", ascending=False).head(10)
top_science_students = df.sort_values(by="Science", ascending=False).head(10)


# Output the results


print(f"Student with Highest Average:\n{df.loc[class_highest]}")
print(f"Student with Lowest Average:\n{df.loc[class_lowest]}")
print(f"Class Average: {class_average}")
print(f"Class Median: {class_median}")
print(f"Class Standard Deviation: {class_std_dev}")
print(f"Students with Average Above 90:\n{average_above_90}")
print(f"Students with Math Score Above 95:\n{math_above_95}")
print(f"Students Failing English:\n{english_failing}")
print(f"Students with Average Above 90 but Science Below 85:\n{student_with_a_average_but_science_below_85}")
print(f"Top 10 Students by Average:\n{top_10_students}")
print(f"Bottom 10 Students by Average:\n{bottom_10_students}")
print(f"Top 10 Students by Math Score:\n{top_math_students}")
print(f"Top 10 Students by Science Score:\n{top_science_students}")


# Visualizations


plt.figure()
plt.hist(df["Average"])
plt.xlabel("Average Score")
plt.ylabel("Number of Students")
plt.title("Distribution of Student Averages")

plt.figure()
plt.bar(top_10_students["Name"], top_10_students["Average"])
plt.xlabel("Student Name")
plt.ylabel("Average Score")
plt.title("Top 10 Students by Average")
plt.xticks(rotation=45)

plt.figure()
plt.pie(df["Letter Grade"].value_counts(), labels=df["Letter Grade"].value_counts().index, autopct='%1.1f%%')
plt.title("Distribution of Letter Grades")

plt.figure()
plt.scatter(df["Math"], df["Science"])
plt.xlabel("Math Score")
plt.ylabel("Science Score")
plt.title("Relationship between Math and Science Scores")

plt.show()
