# Basic
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
import matplotlib  # Thêm để chọn backend

warnings.filterwarnings('ignore')

# Feature Engineering
import re

rs = 999  # Random seed

df_cleaned = pd.read_csv('data_source\cleaned_data.csv')

print("Kiểu dữ liệu của từng cột: ")
print(df_cleaned.info())
print(df_cleaned.head())

num_col = ['Hours_Studied', 'Attendance', 'Previous_Scores']
cat_col = ['Parental_Involvement', 'Access_to_Resources', 'Sleep_Hours', 'Extracurricular_Activities', 
           'Motivation_Level', 'Internet_Access', 'Tutoring_Sessions', 'Family_Income', 'Teacher_Quality', 
           'School_Type', 'Peer_Influence', 'Physical_Activity', 'Learning_Disabilities', 'Parental_Education_Level', 
           'Distance_from_Home', 'Gender']
target = 'Exam_Score'

print("\nKiểm tra kiểu dữ liệu")
print(df_cleaned[num_col].dtypes)
print(df_cleaned[cat_col].dtypes)
print(df_cleaned[target].dtype)

# Visualization - Trực quan hoá dữ liệu

# Vẽ histogram cho Exam_Score với bins đã định nghĩa
plt.figure(figsize=(10, 6))

sns.histplot(df_cleaned[target], bins = 50, kde=True, color='red', edgecolor = 'black', alpha = 0.5 )

plt.title('Distribution of Exam Score')
plt.xlabel('Exam Score')
plt.ylabel('Frequency')

plt.xlim(55, 100)

plt.grid(axis='y', alpha = 0.75)
plt.show()

print("\nNhận định về Distribution of Exam Score.")

below_64 = df_cleaned[df_cleaned['Exam_Score'] <= 64]
above_70 = df_cleaned[df_cleaned['Exam_Score'] >= 70]
between_65_and_69 = df_cleaned[(df_cleaned['Exam_Score'] >= 65) & (df_cleaned['Exam_Score'] <= 69)]

percent_below_64 = (len(below_64) / len(df_cleaned)) * 100
percent_above_70 = (len(above_70) / len(df_cleaned)) * 100
percent_between_65_and_69 = (len(between_65_and_69) / len(df_cleaned)) * 100

print(f"Phần trăm điểm số dưới 64: {percent_below_64:.2f}%")
print(f"Phần trăm điểm số trên 70: {percent_above_70:.2f}%")
print(f"Phần trăm điểm số trong khoảng 65 đến 69: {percent_between_65_and_69:.2f}%")

# Histogram cho Hours_Studied
plt.figure(figsize=(10, 6))
sns.histplot(df_cleaned['Hours_Studied'], bins=30, kde=True, color='blue', edgecolor='black', alpha=0.5)
plt.title('Distribution of Hours Studied')
plt.xlabel('Hours Studied')
plt.ylabel('Frequency')
plt.xlim(0, 50)
plt.grid(axis='y', alpha=0.75)
plt.show()

print("-" * 20)
print("\nNhận định về Distribution of Hours Studied.")

below_10 = df_cleaned[df_cleaned['Hours_Studied'] <= 10]
above_20 = df_cleaned[df_cleaned['Hours_Studied'] >= 20]
between_11_and_19 = df_cleaned[(df_cleaned['Hours_Studied'] >= 11) & (df_cleaned['Hours_Studied'] <= 19)]

percent_below_10 = (len(below_10) / len(df_cleaned)) * 100
percent_above_20 = (len(above_20) / len(df_cleaned)) * 100
percent_between_11_and_19 = (len(between_11_and_19) / len(df_cleaned)) * 100

print(f"Phần trăm số giờ học bài dưới 10 giờ: {percent_below_10:.2f}%")
print(f"Phần trăm số giờ học bài trên 20 giờ: {percent_above_20:.2f}%")
print(f"Phần trăm số giờ học bài trong khoảng 11 giờ đến 19 giờ: {percent_between_11_and_19:.2f}%")

# Histogram cho Attendance
plt.figure(figsize=(10, 6))
sns.histplot(df_cleaned['Attendance'], bins=50, kde=True, color='violet', edgecolor='black', alpha=0.5)
plt.title('Distribution of Attendance')
plt.xlabel('Attendance')
plt.ylabel('Frequency')
plt.xlim(60, 100)
plt.grid(axis='y', alpha=0.75)
plt.show()

print("-" * 20)
print("\nNhận định về Distribution of Attendance.")

below_69 = df_cleaned[df_cleaned['Attendance'] <= 69]
above_80 = df_cleaned[df_cleaned['Attendance'] >= 80]
between_70_and_79 = df_cleaned[(df_cleaned['Attendance'] >= 70) & (df_cleaned['Attendance'] <= 79)]

percent_below_69 = (len(below_69) / len(df_cleaned)) * 100
percent_above_80 = (len(above_80) / len(df_cleaned)) * 100
percent_between_70_and_79 = (len(between_70_and_79) / len(df_cleaned)) * 100

print(f"Phần trăm tham dự dưới 69: {percent_below_69:.2f}%")
print(f"Phần trăm tham dự trên 80: {percent_above_80:.2f}%")
print(f"Phần trăm tham dự trong khoảng 70 đến 79: {percent_between_70_and_79:.2f}%")

# Bar cho Parental_Involvement
counts = df_cleaned['Parental_Involvement'].value_counts()
counts.plot(kind='bar', color=['red', 'orange', 'green'], edgecolor='black', alpha=0.5)
plt.title('Distribution of Parental Involvement')
plt.xlabel('Parental Involvement')
plt.ylabel('Frequency')
plt.xticks(rotation=0)
plt.grid(axis='y', alpha=0.75)
plt.show()

print("-" * 20)
print("\nNhận định về Distribution of Parental Involvement.")

low_involvement = df_cleaned[df_cleaned['Parental_Involvement'] == 'Low']
medium_involvement = df_cleaned[df_cleaned['Parental_Involvement'] == 'Medium']
high_involvement = df_cleaned[df_cleaned['Parental_Involvement'] == 'High']

percent_low = (len(low_involvement) / len(df_cleaned)) * 100
percent_medium = (len(medium_involvement) / len(df_cleaned)) * 100
percent_high = (len(high_involvement) / len(df_cleaned)) * 100

print(f"Phần trăm tham gia của phụ huynh ở mức thấp: {percent_low:.2f}%")
print(f"Phần trăm tham gia của phụ huynh ở mức trung bình: {percent_medium:.2f}%")
print(f"Phần trăm tham gia của phụ huynh ở mức cao: {percent_high:.2f}%")

# Bar cho Access_to_Resources
counts = df_cleaned['Access_to_Resources'].value_counts()
counts.plot(kind='bar', color=['cyan', 'magenta', 'green'], edgecolor='black', alpha=0.5)
plt.title('Distribution of Access to Resources')
plt.xlabel('Access to Resources')
plt.ylabel('Frequency')
plt.xticks(rotation=0)
plt.grid(axis='y', alpha=0.75)
plt.show()

print("-" * 20)
print("\nNhận định về Distribution of Access to Resources.")

low_access = df_cleaned[df_cleaned['Access_to_Resources'] == 'Low']
medium_access = df_cleaned[df_cleaned['Access_to_Resources'] == 'Medium']
high_access = df_cleaned[df_cleaned['Access_to_Resources'] == 'High']

percent_low = (len(low_access) / len(df_cleaned)) * 100
percent_medium = (len(medium_access) / len(df_cleaned)) * 100
percent_high = (len(high_access) / len(df_cleaned)) * 100

print(f"Phần trăm truy cập vào dữ liệu ở mức thấp: {percent_low:.2f}%")
print(f"Phần trăm truy cập vào dữ liệu ở mức trung bình: {percent_medium:.2f}%")
print(f"Phần trăm truy cập vào dữ liệu ở mức cao: {percent_high:.2f}%")

# Bar cho Extracurricular_Activities
counts = df_cleaned['Extracurricular_Activities'].value_counts()
counts.plot(kind='bar', color=['red', 'green'], edgecolor='black', alpha=0.5)
plt.title('Distribution of Extracurricular Activities')
plt.xlabel('Extracurricular Activities')
plt.ylabel('Frequency')
plt.xticks(rotation=0)
plt.grid(axis='y', alpha=0.75)
plt.show()

print("-" * 20)
print("\nNhận định về Distribution of Extracurricular Activitiess.")

yes_activitiess = df_cleaned[df_cleaned['Extracurricular_Activities'] == 'Yes']
no_activitiess = df_cleaned[df_cleaned['Extracurricular_Activities'] == 'No']

percent_yes = (len(yes_activitiess) / len(df_cleaned)) * 100
percent_no = (len(no_activitiess) / len(df_cleaned)) * 100

print(f"Phần trăm có hoạt động ngoại khóa: {percent_yes:.2f}%")
print(f"Phần trăm không hoạt động ngoại khóa: {percent_no:.2f}%")

# Histogram cho Sleep_Hours
plt.figure(figsize=(10, 6))
sns.histplot(df_cleaned['Sleep_Hours'], bins=8, kde=True, color='blue', edgecolor='black', alpha=0.5)
plt.title('Distribution of Sleep Hours')
plt.xlabel('Sleep Hours')
plt.ylabel('Frequency')
plt.xticks(range(3, 13))
plt.grid(axis='y', alpha=0.4)
plt.show()

print("-" * 20)
print("\nNhận định về Distribution of Sleep Hours.")

below_5 = df_cleaned[df_cleaned['Sleep_Hours'] <= 5]
above_8 = df_cleaned[df_cleaned['Sleep_Hours'] >= 8]
between_6_and_7 = df_cleaned[(df_cleaned['Sleep_Hours'] >= 6) & (df_cleaned['Sleep_Hours'] <= 7)]

percent_below_5 = (len(below_5) / len(df_cleaned)) * 100
percent_above_8 = (len(above_8) / len(df_cleaned)) * 100
percent_between_6_and_7 = (len(between_6_and_7) / len(df_cleaned)) * 100

print(f"Phần trăm số giờ ngủ dưới 5 giờ: {percent_below_5:.2f}%")
print(f"Phần trăm số giờ ngủ trên 8 giờ: {percent_above_8:.2f}%")
print(f"Phần trăm số giờ ngủ trong khoảng 6 đến 7 giờ: {percent_between_6_and_7:.2f}%")

# Histogram cho Previous_Scores
plt.hist(df_cleaned['Previous_Scores'], bins=50, color='green', edgecolor='black', alpha=0.5)
plt.title('Distribution of Previous Scores')
plt.xlabel('Previous Scores')
plt.ylabel('Frequency')
plt.xlim(50, 100)
plt.grid(axis='y', alpha=0.75)
plt.show()

print("-" * 20)
print("\nNhận định về Distribution of Previous Scoress.")

below_69 = df_cleaned[df_cleaned['Previous_Scores'] <= 69]
above_90 = df_cleaned[df_cleaned['Previous_Scores'] >= 90]
between_70_and_89 = df_cleaned[(df_cleaned['Previous_Scores'] >= 70) & (df_cleaned['Previous_Scores'] <= 89)]

percent_below_69 = (len(below_69) / len(df_cleaned)) * 100
percent_above_90 = (len(above_90) / len(df_cleaned)) * 100
percent_between_70_and_89 = (len(between_70_and_89) / len(df_cleaned)) * 100

print(f"Phần trăm điểm dưới 69: {percent_below_69:.2f}%")
print(f"Phần trăm điểm trên 90: {percent_above_90:.2f}%")
print(f"Phần trăm điểm trong khoảng 70 đến 89 giờ: {percent_between_70_and_89:.2f}%")

# Bar cho Motivation_Level
counts = df_cleaned['Motivation_Level'].value_counts()
counts.plot(kind='bar', color=['yellow', 'green', 'red'], edgecolor='black', alpha=0.5)
plt.title('Distribution of Motivation Level')
plt.xlabel('Motivation Level')
plt.ylabel('Frequency')
plt.xticks(rotation=0)
plt.grid(axis='y', alpha=0.75)
plt.show()

print("-" * 20)
print("\nNhận định về Distribution of Motivation Level.")

low_level= df_cleaned[df_cleaned['Motivation_Level'] == 'Low']
medium_level = df_cleaned[df_cleaned['Motivation_Level'] == 'Medium']
high_level = df_cleaned[df_cleaned['Motivation_Level'] == 'High']

percent_low = (len(low_level) / len(df_cleaned)) * 100
percent_medium = (len(medium_level) / len(df_cleaned)) * 100
percent_high = (len(high_level) / len(df_cleaned)) * 100

print(f"Phần trăm động lực ở mức thấp: {percent_low:.2f}%")
print(f"Phần trăm động lực ở mức trung bình: {percent_medium:.2f}%")
print(f"Phần trăm động lực ở mức cao: {percent_high:.2f}%")

# Bar cho Internet_Access
counts = df_cleaned['Internet_Access'].value_counts()
counts.plot(kind='bar', color=['purple', 'red'], edgecolor='black', alpha=0.5)
plt.title('Distribution of Internet Access')
plt.xlabel('Internet Access')
plt.ylabel('Frequency')
plt.xticks(rotation=0)
plt.grid(axis='y', alpha=0.75)
plt.show()

print("-" * 20)
print("\nNhận định về Distribution of Internet Access.")

yes_access = df_cleaned[df_cleaned['Internet_Access'] == 'Yes']
no_access = df_cleaned[df_cleaned['Internet_Access'] == 'No']

percent_yes = (len(yes_access) / len(df_cleaned)) * 100
percent_no = (len(no_access) / len(df_cleaned)) * 100

print(f"Phần trăm có truy cập Internet: {percent_yes:.2f}%")
print(f"Phần trăm không truy cập Internet: {percent_no:.2f}%")

# Histogram cho Tutoring_Sessions
plt.figure(figsize=(10, 6))
sns.histplot(df_cleaned['Tutoring_Sessions'], bins=8, kde=True, color='purple', edgecolor='black', alpha=0.5)
plt.title('Distribution of Tutoring Sessions')
plt.xlabel('Tutoring Sessions')
plt.ylabel('Frequency')
plt.xticks(range(0, 9))
plt.grid(axis='y', alpha=0.4)
plt.show()

print("-" * 20)
print("\nNhận định về Distribution of Tutoring Sessions.")

below_2 = df_cleaned[df_cleaned['Tutoring_Sessions'] <= 2]
above_6 = df_cleaned[df_cleaned['Tutoring_Sessions'] >= 6]
between_3_and_5 = df_cleaned[(df_cleaned['Tutoring_Sessions'] >= 3) & (df_cleaned['Tutoring_Sessions'] <= 5)]

percent_below_2 = (len(below_2) / len(df_cleaned)) * 100
percent_above_6 = (len(above_6) / len(df_cleaned)) * 100
percent_between_3_and_5 = (len(between_3_and_5) / len(df_cleaned)) * 100

print(f"Phần trăm số phiên dạy kèm dưới 2 phiên: {percent_below_5:.2f}%")
print(f"Phần trăm số phiên dạy kèm trên 6 phiên: {percent_above_8:.2f}%")
print(f"Phần trăm số phiên dạy kèm trong khoảng 3 đến 5 phiên: {percent_between_6_and_7:.2f}%")

# Bar cho Family_Income
counts = df_cleaned['Family_Income'].value_counts()
counts.plot(kind='bar', color=['purple', 'yellow', 'pink'], edgecolor='black', alpha=0.5)
plt.title('Distribution of Family Income')
plt.xlabel('Family Income')
plt.ylabel('Frequency')
plt.xticks(rotation=0)
plt.grid(axis='y', alpha=0.75)
plt.show()

print("-" * 20)
print("\nNhận định về Distribution of Family Income.")

low_income= df_cleaned[df_cleaned['Family_Income'] == 'Low']
medium_income = df_cleaned[df_cleaned['Family_Income'] == 'Medium']
high_income = df_cleaned[df_cleaned['Family_Income'] == 'High']

percent_low = (len(low_income) / len(df_cleaned)) * 100
percent_medium = (len(medium_income) / len(df_cleaned)) * 100
percent_high = (len(high_income) / len(df_cleaned)) * 100

print(f"Phần trăm thu nhập gia đình ở mức thấp: {percent_low:.2f}%")
print(f"Phần trăm thu nhập gia đình ở mức trung bình: {percent_medium:.2f}%")
print(f"Phần trăm thu nhập gia đình ở mức cao: {percent_high:.2f}%")

# Bar cho Teacher_Quality
counts = df_cleaned['Teacher_Quality'].value_counts()
counts.plot(kind='bar', color=['fuchsia', 'blue', 'orange'], edgecolor='black', alpha=0.5)
plt.title('Distribution of Teacher Quality')
plt.xlabel('Teacher Quality')
plt.ylabel('Frequency')
plt.xticks(rotation=0)
plt.grid(axis='y', alpha=0.75)
plt.show()

print("-" * 20)
print("\nNhận định về Distribution of Teacher Quality.")

low_quality= df_cleaned[df_cleaned['Teacher_Quality'] == 'Low']
medium_quality = df_cleaned[df_cleaned['Teacher_Quality'] == 'Medium']
high_quality = df_cleaned[df_cleaned['Teacher_Quality'] == 'High']

percent_low = (len(low_quality) / len(df_cleaned)) * 100
percent_medium = (len(medium_quality) / len(df_cleaned)) * 100
percent_high = (len(high_quality) / len(df_cleaned)) * 100

print(f"Phần trăm chất lượng giảng viên ở mức thấp: {percent_low:.2f}%")
print(f"Phần trăm chất lượng giảng viên ở mức trung bình: {percent_medium:.2f}%")
print(f"Phần trăm chất lượng giảng viên ở mức cao: {percent_high:.2f}%")

# Bar cho School_Type
counts = df_cleaned['School_Type'].value_counts()
counts.plot(kind='bar', color=['green', 'violet'], edgecolor='black', alpha=0.5)
plt.title('Distribution of School Type')
plt.xlabel('School Type')
plt.ylabel('Frequency')
plt.xticks(rotation=0)
plt.grid(axis='y', alpha=0.75)
plt.show()

print("-" * 20)
print("\nNhận định về Distribution of School Type.")

public_type = df_cleaned[df_cleaned['School_Type'] == 'Public']
private_type = df_cleaned[df_cleaned['School_Type'] == 'Private']

public_sch = (len(public_type) / len(df_cleaned)) * 100
private_sch = (len(private_type) / len(df_cleaned)) * 100

print(f"Phần trăm học ở trường công lập: {public_sch:.2f}%")
print(f"Phần trăm học ở trường tư thục: {private_sch:.2f}%")

# Bar cho Peer_Influence
counts = df_cleaned['Peer_Influence'].value_counts()
counts.plot(kind='bar', color=['violet', 'lime', 'maroon'], edgecolor='black', alpha=0.5)
plt.title('Distribution of Peer Influence')
plt.xlabel('Peer Influence')
plt.ylabel('Frequency')
plt.xticks(rotation=0)
plt.grid(axis='y', alpha=0.75)
plt.show()

print("-" * 20)
print("\nNhận định về Distribution of Peer Influence.")

po_influ= df_cleaned[df_cleaned['Peer_Influence'] == 'Positive']
ne_influ = df_cleaned[df_cleaned['Peer_Influence'] == 'Negative']
neu_influ = df_cleaned[df_cleaned['Peer_Influence'] == 'Neutral']

percent_po = (len(po_influ) / len(df_cleaned)) * 100
percent_ne = (len(ne_influ) / len(df_cleaned)) * 100
percent_neu = (len(neu_influ) / len(df_cleaned)) * 100

print(f"Phần trăm ảnh hưởng tích cực: {percent_po:.2f}%")
print(f"Phần trăm ảnh hưởng tiêu cực: {percent_ne:.2f}%")
print(f"Phần trăm ảnh hưởng trung lập: {percent_neu:.2f}%")

# Histogram cho Physical_Activity
plt.figure(figsize=(10, 6))
sns.histplot(df_cleaned['Physical_Activity'], bins=8, kde=True, color='teal', edgecolor='black', alpha=0.5)
plt.title('Distribution of Physical Activity')
plt.xlabel('Physical Activity')
plt.ylabel('Frequency')
plt.xticks(range(0, 7))
plt.grid(axis='y', alpha=0.4)
plt.show()

print("-" * 20)
print("\nNhận định về Distribution of Physical Activity.")

below_1 = df_cleaned[df_cleaned['Physical_Activity'] <= 1]
above_5 = df_cleaned[df_cleaned['Physical_Activity'] >= 5]
between_2_and_4 = df_cleaned[(df_cleaned['Physical_Activity'] >= 2) & (df_cleaned['Physical_Activity'] <= 4)]

percent_below_1 = (len(below_2) / len(df_cleaned)) * 100
percent_above_5 = (len(above_5) / len(df_cleaned)) * 100
percent_between_2_and_4 = (len(between_2_and_4) / len(df_cleaned)) * 100

print(f"Phần trăm hoạt động thể chất dưới 1 môn: {percent_below_1:.2f}%")
print(f"Phần trăm hoạt động thể chất trên 5 môn: {percent_above_5:.2f}%")
print(f"Phần trăm hoạt động thể chất trong khoảng 2 đến 4 môn: {percent_between_2_and_4:.2f}%")

# Bar cho Learning_Disabilities
counts = df_cleaned['Learning_Disabilities'].value_counts()
counts.plot(kind='bar', color=['coral', 'olive'], edgecolor='black', alpha=0.5)
plt.title('Distribution of Learning Disabilities')
plt.xlabel('Learning Disabilities')
plt.ylabel('Frequency')
plt.xticks(rotation=0)
plt.grid(axis='y', alpha=0.75)
plt.show()

print("-" * 20)
print("\nNhận định về Distribution of Learning Disabilities.")

yes_disa = df_cleaned[df_cleaned['Learning_Disabilities'] == 'Yes']
no_disa = df_cleaned[df_cleaned['Learning_Disabilities'] == 'No']

percent_yes = (len(yes_disa) / len(df_cleaned)) * 100
percent_no = (len(no_disa) / len(df_cleaned)) * 100

print(f"Phần trăm có truy cập Internet: {percent_yes:.2f}%")
print(f"Phần trăm không truy cập Internet: {percent_no:.2f}%")

# Bar cho Parental_Education_Level
counts = df_cleaned['Parental_Education_Level'].value_counts()
counts.plot(kind='bar', color=['green', 'blue', 'orange'], edgecolor='black', alpha=0.5)
plt.title('Distribution of Parental Education Level')
plt.xlabel('Parental Education Level')
plt.ylabel('Frequency')
plt.xticks(rotation=0)
plt.grid(axis='y', alpha=0.75)
plt.show()

print("-" * 20)
print("\nNhận định về Distribution of Parental Education Level.")

hs = df_cleaned[df_cleaned['Parental_Education_Level'] == 'High School']
co = df_cleaned[df_cleaned['Parental_Education_Level'] == 'College']
po = df_cleaned[df_cleaned['Parental_Education_Level'] == 'Postgraduate']

percent_hs = (len(hs) / len(df_cleaned)) * 100
percent_co = (len(co) / len(df_cleaned)) * 100
percent_po = (len(po) / len(df_cleaned)) * 100

print(f"Phần trăm ba mẹ học trung học: {percent_hs:.2f}%")
print(f"Phần trăm ba mẹ học cao đẳng: {percent_co:.2f}%")
print(f"Phần trăm ba mẹ học tiếp sau đại học: {percent_po:.2f}%")

# Bar cho Distance_from_Home
counts = df_cleaned['Distance_from_Home'].value_counts()
counts.plot(kind='bar', color=['coral', 'olive', 'lime'], edgecolor='black', alpha=0.5)
plt.title('Distribution of Distance from Home')
plt.xlabel('Distance from Home')
plt.ylabel('Frequency')
plt.xticks(rotation=0)
plt.grid(axis='y', alpha=0.75)
plt.show()

print("-" * 20)
print("\nNhận định về Distribution of Distance from Home.")

ne = df_cleaned[df_cleaned['Distance_from_Home'] == 'Near']
fa = df_cleaned[df_cleaned['Distance_from_Home'] == 'Far']
mo = df_cleaned[df_cleaned['Distance_from_Home'] == 'Moderate']

percent_ne = (len(ne) / len(df_cleaned)) * 100
percent_fa = (len(fa) / len(df_cleaned)) * 100
percent_mo = (len(mo) / len(df_cleaned)) * 100

print(f"Phần trăm nhà ở gần trường: {percent_ne:.2f}%")
print(f"Phần trăm nhà ở xa trường: {percent_fa:.2f}%")
print(f"Phần trăm nhà cách trường không xa: {percent_mo:.2f}%")

# Bar cho Gender
counts = df_cleaned['Gender'].value_counts()
counts.plot(kind='bar', color=['azure', 'cyan'], edgecolor='black', alpha=0.5)
plt.title('Distribution of Gender')
plt.xlabel('Gender')
plt.ylabel('Frequency')
plt.xticks(rotation=0)
plt.grid(axis='y', alpha=0.75)
plt.show()

print("-" * 20)
print("\nNhận định về Distribution of Gender.")

ma = df_cleaned[df_cleaned['Gender'] == 'Male']
fe= df_cleaned[df_cleaned['Gender'] == 'Female']

percent_ma = (len(ma) / len(df_cleaned)) * 100
percent_fe = (len(fe) / len(df_cleaned)) * 100

print(f"Phần trăm nữ: {percent_fe:.2f}%")
print(f"Phần trăm nam: {percent_ma:.2f}%")

# Vẽ biểu đồ phân tán Hours Studied và Exam Score
# Liệu số giờ học có ảnh hưởng đến điểm số không?
plt.figure(figsize=(10, 6))
sns.scatterplot(x=df_cleaned['Hours_Studied'], y=df_cleaned['Exam_Score'], color='green', alpha=0.7)

plt.title('Scatter Plot: Hours Studied vs Exam Score')
plt.xlabel('Hours Studied')
plt.ylabel('Exam Score')

plt.grid(True)
plt.show()

print("-" * 20)
correlation = df_cleaned['Hours_Studied'].corr(df_cleaned['Exam_Score'])
print(f"Hệ số tương quan giữa số giờ học và điểm số: {correlation:.2f}")

if correlation > 0.7:
    print("Có một mối quan hệ mạnh mẽ giữa số giờ học và điểm số.")
elif correlation > 0.3:
    print("Có một mối quan hệ yếu giữa số giờ học và điểm số.")
else:
    print("Không có mối quan hệ rõ ràng giữa số giờ học và điểm số.")

# Vẽ biểu đồ phân tán Attendance và Exam Score
plt.figure(figsize=(10, 6))
sns.scatterplot(x=df_cleaned['Attendance'], y=df_cleaned['Exam_Score'], color='gray', alpha=0.7)

plt.title('Scatter Plot: Attendance vs Exam Score')
plt.xlabel('Attendance')
plt.ylabel('Exam Score')

plt.grid(True)
plt.show()

print("-" * 20)
correlation = df_cleaned['Attendance'].corr(df_cleaned['Exam_Score'])
print(f"Hệ số tương quan giữa sự tham gia và điểm số: {correlation:.2f}")

if correlation > 0.7:
    print("Có một mối quan hệ mạnh mẽ giữa sự tham gia và điểm số.")
elif correlation > 0.3:
    print("Có một mối quan hệ yếu giữa sự tham gia và điểm số.")
else:
    print("Không có mối quan hệ rõ ràng giữa sự tham gia và điểm số.")

# Vẽ biểu đồ phân tán Previous Scores và Exam Score
plt.figure(figsize=(10, 6))
sns.scatterplot(x=df_cleaned['Previous_Scores'], y=df_cleaned['Exam_Score'], color='salmon', alpha=0.7)

plt.title('Scatter Plot: Previous Scores vs Exam Score')
plt.xlabel('Previous Scores')
plt.ylabel('Exam Score')

plt.grid(True)
plt.show()

print("-" * 20)
correlation = df_cleaned['Previous_Scores'].corr(df_cleaned['Exam_Score'])
print(f"Hệ số tương quan giữa điểm trước đó và điểm số: {correlation:.2f}")

if correlation > 0.7:
    print("Có một mối quan hệ mạnh mẽ giữa điểm trước đó và điểm số.")
elif correlation > 0.3:
    print("Có một mối quan hệ yếu giữa điểm trước đó và điểm số.")
else:
    print("Không có mối quan hệ rõ ràng giữa điểm trước đó và điểm số.")

# Vẽ biểu đồ boxplot Exam_Score và Parental Involvement
# Sự tham gia của phụ huynh có ảnh hưởng đến kết quả học tập của học sinh?
plt.figure(figsize=(10, 6))
sns.boxplot(x=df_cleaned['Parental_Involvement'], y=df_cleaned['Exam_Score'], palette='Set2')

plt.title('Boxplot: Exam Scores by Parental Involvement')
plt.xlabel('Parental Involvement')
plt.ylabel('Exam Score')

# Mã hóa cột thành các giá trị số
df_cleaned['Parental_Involvement_num'] = df_cleaned['Parental_Involvement'].map({'Low': 0, 'Medium': 1, 'High': 2})

correlation = df_cleaned['Parental_Involvement_num'].corr(df_cleaned['Exam_Score'])
print("-" * 20)
print(f'Mối tương quan giữa sự tham gia của phụ huynh và điểm thi: {correlation:.2f}')

if correlation > 0.7:
    print("Có một mối quan hệ mạnh mẽ giữa sự tham gia của phụ huynh và điểm số.")
elif correlation > 0.3:
    print("Có một mối quan hệ yếu giữa sự tham gia của phụ huynh và điểm số.")
else:
    print("Không có mối quan hệ rõ ràng giữa sự tham gia của phụ huynh và điểm số.")

plt.show()

# Vẽ biểu đồ boxplot Exam_Score và Access_to_Resources
# Mức độ truy cập tài nguyên học tập có liên quan đến kết quả học tập không?
plt.figure(figsize=(10, 6))
sns.boxplot(x=df_cleaned['Access_to_Resources'], y=df_cleaned['Exam_Score'], palette='Set2')

plt.title('Boxplot: Exam Scores by Access to Resources')
plt.xlabel('Access to Resources')
plt.ylabel('Exam Score')

# Mã hóa cột thành các giá trị số
df_cleaned['Access_to_Resources_num'] = df_cleaned['Access_to_Resources'].map({'Low': 0, 'Medium': 1, 'High': 2})

correlation = df_cleaned['Access_to_Resources_num'].corr(df_cleaned['Exam_Score'])
print("-" * 20)
print(f'Mối tương quan giữa truy cập tài nguyên và điểm thi: {correlation:.2f}')

if correlation > 0.7:
    print("Có một mối quan hệ mạnh mẽ giữa truy cập tài nguyên học tập và điểm số.")
elif correlation > 0.3:
    print("Có một mối quan hệ yếu giữa truy cập tài nguyên học tập và điểm số.")
else:
    print("Không có mối quan hệ rõ ràng giữa truy cập tài nguyên học tập và điểm số.")

plt.show()

# Vẽ biểu đồ boxplot Exam_Score và Extracurricular_Activities
# Học sinh tham gia hoạt động ngoại khóa có điểm số khác so với học sinh không tham gia không?
plt.figure(figsize=(10, 6))
sns.boxplot(data=df_cleaned, x='Extracurricular_Activities', y='Exam_Score', palette=['pink', 'blue'])

plt.title('Boxplot: Exam Score by Extracurricular Activities')
plt.xlabel('Extracurricular Activities')
plt.ylabel('Exam Score')

df_cleaned['Extracurricular_Activities_Encoded'] = df_cleaned['Extracurricular_Activities'].map({'Yes': 1, 'No': 0})

correlation = df_cleaned[['Extracurricular_Activities_Encoded', 'Exam_Score']].corr().iloc[0, 1]

print("-" * 20)
print(f"Hệ số tương quan giữa việc tham gia hoạt động ngoại khóa và điểm số: {correlation:.2f}")

if correlation > 0.7:
    print("Có một mối quan hệ mạnh mẽ giữa học sinh tham gia hoạt động ngoại khóa và điểm số.")
elif correlation > 0.3:
    print("Có một mối quan hệ yếu giữa học sinh tham gia hoạt động ngoại khóa và điểm số.")
else:
    print("Không có mối quan hệ rõ ràng giữa học sinh tham gia hoạt động ngoại khóa và điểm số.")

plt.grid(axis='y', alpha=0.75)
plt.show()

# Vẽ biểu đồ boxplot Exam_Score và Sleep_Hours
plt.figure(figsize=(10, 6))

sns.boxplot(data=df_cleaned, x='Sleep_Hours', y='Exam_Score', palette='Set2')

plt.title('Boxplot: Exam Score by Sleep Hours')
plt.xlabel('Sleep Hours')
plt.ylabel('Exam Score')

correlation = df_cleaned[['Sleep_Hours', 'Exam_Score']].corr().iloc[0, 1]

print("-" * 20)
print(f"Hệ số tương quan giữa giờ ngủ và điểm số: {correlation:.2f}")

if correlation > 0.7:
    print("Có một mối quan hệ mạnh mẽ giữa giờ ngủ và điểm số.")
elif correlation > 0.3:
    print("Có một mối quan hệ yếu giữa giờ ngủ và điểm số.")
else:
    print("Không có mối quan hệ rõ ràng giữa giờ ngủ và điểm số.")

plt.grid(axis='y', alpha=0.75)
plt.show()

# Vẽ biểu đồ boxplot Exam_Score và Motivation_Level
plt.figure(figsize=(10, 6))
sns.boxplot(x=df_cleaned['Motivation_Level'], y=df_cleaned['Exam_Score'], palette='Set1')

plt.title('Boxplot: Exam Scores by Motivation Level')
plt.xlabel('Motivation Level')
plt.ylabel('Exam Score')

# Mã hóa cột thành các giá trị số
df_cleaned['Motivation_Level_num'] = df_cleaned['Motivation_Level'].map({'Low': 0, 'Medium': 1, 'High': 2})

correlation = df_cleaned['Motivation_Level_num'].corr(df_cleaned['Exam_Score'])
print("-" * 20)
print(f'Mối tương quan giữa động lực và điểm thi: {correlation:.2f}')

if correlation > 0.7:
    print("Có một mối quan hệ mạnh mẽ giữa động lực và điểm số.")
elif correlation > 0.3:
    print("Có một mối quan hệ yếu giữa động lực và điểm số.")
else:
    print("Không có mối quan hệ rõ ràng giữa động lực và điểm số.")

plt.show()

# Vẽ biểu đồ boxplot Exam_Score và Internet_Access
plt.figure(figsize=(10, 6))
sns.boxplot(data=df_cleaned, x='Internet_Access', y='Exam_Score', palette=['red', 'pink'])

plt.title('Boxplot: Exam Score by Internet Access')
plt.xlabel('Internet Access')
plt.ylabel('Exam Score')

df_cleaned['Internet_Access_num'] = df_cleaned['Internet_Access'].map({'Yes': 1, 'No': 0})

correlation = df_cleaned[['Internet_Access_num', 'Exam_Score']].corr().iloc[0, 1]

print("-" * 20)
print(f"Hệ số tương quan giữa việc truy cập Internet và điểm số: {correlation:.2f}")

if correlation > 0.7:
    print("Có một mối quan hệ mạnh mẽ giữa việc truy cập Internet và điểm số.")
elif correlation > 0.3:
    print("Có một mối quan hệ yếu giữa việc truy cập Internet và điểm số.")
else:
    print("Không có mối quan hệ rõ ràng giữa việc truy cập Internet và điểm số.")

plt.grid(axis='y', alpha=0.75)
plt.show()

# Vẽ biểu đồ boxplot Exam_Score và Tutoring_Sessions
plt.figure(figsize=(10, 6))

sns.boxplot(data=df_cleaned, x='Tutoring_Sessions', y='Exam_Score', palette='Set1')

plt.title('Boxplot: Exam Score by Tutoring Sessions')
plt.xlabel('Tutoring Sessions')
plt.ylabel('Exam Score')

correlation = df_cleaned[['Tutoring_Sessions', 'Exam_Score']].corr().iloc[0, 1]

print("-" * 20)
print(f"Hệ số tương quan giữa các phiên dạy kèm và điểm số: {correlation:.2f}")

if correlation > 0.7:
    print("Có một mối quan hệ mạnh mẽ giữa các phiên dạy kèm và điểm số.")
elif correlation > 0.3:
    print("Có một mối quan hệ yếu giữa các phiên dạy kèm và điểm số.")
else:
    print("Không có mối quan hệ rõ ràng giữa các phiên dạy kèm và điểm số.")

plt.grid(axis='y', alpha=0.75)
plt.show()

# Vẽ biểu đồ boxplot Exam_Score và Family_Income
# Có mối liên hệ giữa thu nhập gia đình và điểm số học tập không?
plt.figure(figsize=(10, 6))
sns.boxplot(x=df_cleaned['Family_Income'], y=df_cleaned['Exam_Score'], palette='Set2')

plt.title('Boxplot: Exam Scores by Family Income')
plt.xlabel('Access to Resources')
plt.ylabel('Exam Score')

# Mã hóa cột thành các giá trị số
df_cleaned['Family_Income_num'] = df_cleaned['Family_Income'].map({'Low': 0, 'Medium': 1, 'High': 2})

# Tính toán mối tương quan
correlation = df_cleaned['Family_Income_num'].corr(df_cleaned['Exam_Score'])
print("-" * 20)
print(f'Mối tương quan giữa thu nhập gia đình và điểm thi: {correlation:.2f}')

# Nhận xét về kết quả
if correlation > 0.7:
    print("Có một mối quan hệ mạnh mẽ giữa thu nhập gia đình và điểm số.")
elif correlation > 0.3:
    print("Có một mối quan hệ yếu giữa thu nhập gia đình và điểm số.")
else:
    print("Không có mối quan hệ rõ ràng giữa thu nhập gia đình và điểm số.")

# Hiển thị biểu đồ
plt.show()

# Vẽ biểu đồ boxplot Exam_Score và Teacher_Quality
# Chất lượng giáo viên có ảnh hưởng như thế nào đến kết quả học tập?
plt.figure(figsize=(10, 6))
sns.boxplot(x=df_cleaned['Teacher_Quality'], y=df_cleaned['Exam_Score'], palette='Set1')

plt.title('Boxplot: Exam Scores by Teacher Quality')
plt.xlabel('Teacher Quality')
plt.ylabel('Exam Score')

# Mã hóa cột thành các giá trị số
df_cleaned['Teacher_Quality_num'] = df_cleaned['Teacher_Quality'].map({'Low': 0, 'Medium': 1, 'High': 2})

# Tính toán mối tương quan
correlation = df_cleaned['Teacher_Quality_num'].corr(df_cleaned['Exam_Score'])
print("-" * 20)
print(f'Mối tương quan giữa chất lượng giáo viên và điểm thi: {correlation:.2f}')

# Nhận xét về kết quả
if correlation > 0.7:
    print("Có một mối quan hệ mạnh mẽ giữa chất lượng giáo viên và điểm số.")
elif correlation > 0.3:
    print("Có một mối quan hệ yếu giữa chất lượng giáo viên và điểm số.")
else:
    print("Không có mối quan hệ rõ ràng giữa chất lượng giáo viên và điểm số.")

# Hiển thị biểu đồ
plt.show()

# Vẽ biểu đồ Boxplot cho Exam_Score và School_Type
# Loại trường học (công lập hay tư thục) có ảnh hưởng đến thành tích học tập?
plt.figure(figsize=(10, 6))
sns.boxplot(x=df_cleaned['School_Type'], y=df_cleaned['Exam_Score'], palette='Set2')

plt.title('Boxplot: Exam Scores by School Type')
plt.xlabel('School Type')
plt.ylabel('Exam Score')

# Mã hóa cột thành các giá trị số
df_cleaned['School_Type_num'] = df_cleaned['School_Type'].map({'Public': 0, 'Private': 1})

# Tính toán mối tương quan
correlation = df_cleaned['School_Type_num'].corr(df_cleaned['Exam_Score'])
print("-" * 20)
print(f'Mối tương quan giữa loại trường học và điểm thi: {correlation:.2f}')

# Nhận xét về kết quả

if correlation > 0.7:
    print("Có một mối quan hệ mạnh mẽ giữa loại trường học và điểm số.")
elif correlation > 0.3:
    print("Có một mối quan hệ yếu giữa loại trường học và điểm số.")
else:
    print("Không có mối quan hệ rõ ràng giữa loại trường học và điểm số.")

# Hiển thị biểu đồ
plt.show()

# Vẽ biểu đồ boxplot Exam_Score và Peer_Influence
# Sự ảnh hưởng của bạn bè đến điểm số học tập?
plt.figure(figsize=(10, 6))
sns.boxplot(x=df_cleaned['Peer_Influence'], y=df_cleaned['Exam_Score'], palette='Set3')

plt.title('Boxplot: Exam Scores by Teacher Quality')
plt.xlabel('Teacher Quality')
plt.ylabel('Exam Score')

# Mã hóa cột thành các giá trị số
df_cleaned['Peer_Influence_num'] = df_cleaned['Peer_Influence'].map({'Positive': 0, 'Negative': 1, 'Neutral': 2})

# Tính toán mối tương quan
correlation = df_cleaned['Peer_Influence_num'].corr(df_cleaned['Exam_Score'])
print("-" * 20)
print(f'Mối tương quan giữa sự ảnh hưởng của bạn bè và điểm thi: {correlation:.2f}')

# Nhận xét về kết quả
if correlation > 0.7:
    print("Có một mối quan hệ mạnh mẽ giữa sự ảnh hưởng của bạn bè và điểm số.")
elif correlation > 0.3:
    print("Có một mối quan hệ yếu giữa sự ảnh hưởng của bạn bè và điểm số.")
else:
    print("Không có mối quan hệ rõ ràng giữa sự ảnh hưởng của bạn bè và điểm số.")

# Hiển thị biểu đồ
plt.show()

# Vẽ biểu đồ boxplot Exam_Score và Physical_Activity
plt.figure(figsize=(10, 6))

sns.boxplot(data=df_cleaned, x='Physical_Activity', y='Exam_Score', palette='Set2')

plt.title('Boxplot: Exam Score by Physical Activity')
plt.xlabel('Physical Activity')
plt.ylabel('Exam Score')

correlation = df_cleaned[['Physical_Activity', 'Exam_Score']].corr().iloc[0, 1]

print("-" * 20)
print(f"Hệ số tương quan giữa hoạt động thể chất và điểm số: {correlation:.2f}")

if correlation > 0.7:
    print("Có một mối quan hệ mạnh mẽ giữa hoạt động thể chất và điểm số.")
elif correlation > 0.3:
    print("Có một mối quan hệ yếu giữa hoạt động thể chất và điểm số.")
else:
    print("Không có mối quan hệ rõ ràng giữa hoạt động thể chất và điểm số.")

plt.grid(axis='y', alpha=0.75)
plt.show()

# Vẽ biểu đồ Boxplot cho Exam_Score và Learning_Disabilities
plt.figure(figsize=(10, 6))
sns.boxplot(x=df_cleaned['Learning_Disabilities'], y=df_cleaned['Exam_Score'], palette='Set2')

plt.title('Boxplot: Exam Scores by School Type')
plt.xlabel('School Type')
plt.ylabel('Exam Score')

# Mã hóa cột thành các giá trị số
df_cleaned['Learning_Disabilities_num'] = df_cleaned['Learning_Disabilities'].map({'No': 0, 'Yes': 1})

# Tính toán mối tương quan
correlation = df_cleaned['Learning_Disabilities_num'].corr(df_cleaned['Exam_Score'])
print("-" * 20)
print(f'Mối tương quan giữa khuyết tập học tập và điểm thi: {correlation:.2f}')

if correlation > 0.7:
    print("Có một mối quan hệ mạnh mẽ giữa khuyết tật học tập và điểm số.")
elif correlation > 0.3:
    print("Có một mối quan hệ yếu giữa khuyết tật học tập và điểm số.")
else:
    print("Không có mối quan hệ rõ ràng giữa khuyết tật học tập và điểm số.")

# Hiển thị biểu đồ
plt.show()

# Vẽ biểu đồ boxplot Exam_Score và Parental_Education_Level
plt.figure(figsize=(10, 6))
sns.boxplot(x=df_cleaned['Parental_Education_Level'], y=df_cleaned['Exam_Score'], palette='Set3')

plt.title('Boxplot: Exam Scores by Parental Education Level')
plt.xlabel('Parental Education Level')
plt.ylabel('Exam Score')

# Mã hóa cột thành các giá trị số
df_cleaned['Parental_Education_Level_num'] = df_cleaned['Parental_Education_Level'].map({'High School': 0, 'College': 1, 'Postgraduate': 2})

# Tính toán mối tương quan
correlation = df_cleaned['Parental_Education_Level_num'].corr(df_cleaned['Exam_Score'])
print("-" * 20)
print(f'Mối tương quan giữa mức độ học tập của ba mẹ và điểm thi: {correlation:.2f}')

# Nhận xét về kết quả
if correlation > 0.7:
    print("Có một mối quan hệ mạnh mẽ giữa mức độ học tập của ba mẹ và điểm số.")
elif correlation > 0.3:
    print("Có một mối quan hệ yếu giữa mức độ học tập của ba mẹ và điểm số.")
else:
    print("Không có mối quan hệ rõ ràng giữa mức độ học tập của ba mẹ và điểm số.")

# Hiển thị biểu đồ
plt.show()

# Vẽ biểu đồ boxplot Exam_Score và Distance_from_Home
plt.figure(figsize=(10, 6))
sns.boxplot(x=df_cleaned['Distance_from_Home'], y=df_cleaned['Exam_Score'], palette='Set3')

plt.title('Boxplot: Exam Scores by Distance from Home')
plt.xlabel('Distance from Home')
plt.ylabel('Exam Score')

# Mã hóa cột thành các giá trị số
df_cleaned['Distance_from_Home_num'] = df_cleaned['Distance_from_Home'].map({'Near': 0, 'Moderate': 1, 'Far': 2})

# Tính toán mối tương quan
correlation = df_cleaned['Distance_from_Home_num'].corr(df_cleaned['Exam_Score'])
print("-" * 20)
print(f'Mối tương quan giữa khoảng cách từ nhà đến trường và điểm thi: {correlation:.2f}')

# Nhận xét về kết quả
if correlation > 0.7:
    print("Có một mối quan hệ mạnh mẽ giữa khoảng cách từ nhà đến trường và điểm số.")
elif correlation > 0.3:
    print("Có một mối quan hệ yếu giữa khoảng cách từ nhà đến trường và điểm số.")
else:
    print("Không có mối quan hệ rõ ràng giữa khoảng cách từ nhà đến trường và điểm số.")

# Hiển thị biểu đồ
plt.show()

# Vẽ biểu đồ Boxplot cho Exam_Score và Gender
plt.figure(figsize=(10, 6))
sns.boxplot(x=df_cleaned['Gender'], y=df_cleaned['Exam_Score'], palette='Set2')

plt.title('Boxplot: Exam Scores by Gender')
plt.xlabel('Gender')
plt.ylabel('Exam Score')

# Mã hóa cột thành các giá trị số
df_cleaned['Gender_num'] = df_cleaned['Gender'].map({'Female': 0, 'Male': 1})

# Tính toán mối tương quan
correlation = df_cleaned['Gender_num'].corr(df_cleaned['Exam_Score'])
print("-" * 20)
print(f'Mối tương quan giữa giới tính và điểm thi: {correlation:.2f}')

if correlation > 0.7:
    print("Có một mối quan hệ mạnh mẽ giữa giới tính và điểm số.")
elif correlation > 0.3:
    print("Có một mối quan hệ yếu giữa giới tính và điểm số.")
else:
    print("Không có mối quan hệ rõ ràng giữa giới tính và điểm số.")

# Hiển thị biểu đồ
plt.show()






