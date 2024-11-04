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
# from sklearn.impute import SimpleImputer
# from sklearn.model_selection import KFold

# # Modeling
# import lightgbm as lgb
# from lightgbm import LGBMRegressor
# from catboost import CatBoostRegressor

# # Model Evaluation
# from sklearn.metrics import mean_squared_error

rs = 999  # Random seed

df_cleaned = pd.read_csv('data_source\cleaned_data.csv')

# Tiếp theo, chúng ta sẽ kiểm tra kiểu dữ liệu của từng cột và phân tách chúng thành 
# các biến số và biến phân loại dựa trên kiểu dữ liệu của chúng.
#Chúng tôi sẽ chuyển đổi các biến thực sự mang tính phân loại nhưng được phân loại là biến số 
#do kiểu dữ liệu số nguyên của chúng thành các biến phân loại.
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

# Thêm tiêu đề và nhãn trục
plt.title('Distribution of Exam Score')
plt.xlabel('Exam Score')
plt.ylabel('Frequency')

# Thiết lập trục hoành để hiện thị từ 55 đến 100
plt.xlim(55, 100)

# Hiển thị biểu đồ
plt.grid(axis='y', alpha = 0.75)
plt.show()

print("\nNhận định về Distribution of Exam Score.")
# Tính toán các ngưỡng điểm số
below_64 = df_cleaned[df_cleaned['Exam_Score'] <= 64]
above_70 = df_cleaned[df_cleaned['Exam_Score'] >= 70]
between_65_and_69 = df_cleaned[(df_cleaned['Exam_Score'] >= 65) & (df_cleaned['Exam_Score'] <= 69)]

# Tính toán tỷ lệ phần trăm
percent_below_64 = (len(below_64) / len(df_cleaned)) * 100
percent_above_70 = (len(above_70) / len(df_cleaned)) * 100
percent_between_65_and_69 = (len(between_65_and_69) / len(df_cleaned)) * 100

# Kết quả
print(f"Phần trăm điểm số dưới 64: {percent_below_64:.2f}%")
print(f"Phần trăm điểm số trên 70: {percent_above_70:.2f}%")
print(f"Phần trăm điểm số trong khoảng 65 đến 69: {percent_between_65_and_69:.2f}%")
# 21,89% số điểm thấp nhất dưới 64, trong khi 24,78% số điểm cao nhất trên 70, 50% số điểm tập trung ở mức từ 65 đến 69.

# Histogram cho Hours_Studied
plt.figure(figsize=(10, 6))
sns.histplot(df_cleaned['Hours_Studied'], bins=50, kde=True, color='blue', edgecolor='black', alpha=0.5)
plt.title('Distribution of Hours Studied')
plt.xlabel('Hours Studied')
plt.ylabel('Frequency')
plt.xlim(0, 50)
plt.grid(axis='y', alpha=0.75)
plt.show()

# Histogram cho Attendance
plt.figure(figsize=(10, 6))
sns.histplot(df_cleaned['Attendance'], bins=50, kde=True, color='orange', edgecolor='black', alpha=0.5)
plt.title('Distribution of Attendance')
plt.xlabel('Attendance')
plt.ylabel('Frequency')
plt.xlim(60, 100)
plt.grid(axis='y', alpha=0.75)
plt.show()

# Histogram cho Previous_Scores
plt.hist(df_cleaned['Previous_Scores'], bins=50, color='green', edgecolor='black', alpha=0.5)
plt.title('Distribution of Previous Scores')
plt.xlabel('Previous Scores')
plt.ylabel('Frequency')
plt.xlim(0, 100)
plt.grid(axis='y', alpha=0.75)
plt.show()