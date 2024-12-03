﻿import numpy as np
import pandas as pd
from pandas.api.types import CategoricalDtype

# Đọc dữ liệu từ file CSV gốc trong thư mục data
df = pd.read_csv('data_source/StudentPerformanceFactors.csv')

print(f"Ma trận DataFrame: {df.shape}")

print("Năm dòng đầu của DF: ")
print(df.head())

print(f"Dữ liệu có bị trùng lặp không? {df.duplicated().any()}")

print(f"Số giá trị trùng lặp: {df.duplicated().sum()}")

percent_null = ( df.isnull().sum().sum() / np.product(df.shape)) * 100
print(f"Phần trăm giá trị bị NULL của toàn bộ DF: {percent_null}")

print("Kiểm tra xem có giá trị ở thuộc tính nào bị NULL không?")
print(df.isnull().any())

print("Số giá trị bị NULL của từng thuộc tính: ")
print(df.isnull().sum())

# Xóa các hàng chứa các giá trị bị thiếu
print("\nXử lí các giá trị NULL:")
print("Xoá các hàng có giá trị NULL:")
df_na = df.dropna()
print(f"Shape sau khi đã xoá: {df_na.shape}")
print(f"Shape ban đầu: {df.shape}")
print("Kiểm tra lại xem còn giá trị NULL nào không?")
print(df_na.isnull().sum())

print("\nTóm tắt thống kê cơ bản dữ liệu số:")
print(df_na.describe())

# Kiểm tra từng cột thuộc tính số xem có giá trị nào ngoại lệ không?
for col in df_na.select_dtypes(include=['number']).columns:
    print(f"Unique values in '{col}': {df_na[col].unique()}")

# Loại bỏ các giá trị ngoại lệ
df_cleaned = df_na[df_na['Exam_Score'] <= 100]
print("\nSau khi xử lí điểm vượt quá 100: ")
print(df_cleaned.describe())

# Kiểm tra từng cột thuộc tính không phải số (categorical hoặc object)
for col in df_cleaned.select_dtypes(exclude=['number']).columns:
    print(f"Unique values in '{col}': {df_cleaned[col].unique()}")

df_cleaned = df.copy()  # Tạo bản sao độc lập của df_cleaned

Parental_Involvement_Type = CategoricalDtype(categories=["Low", "Medium", "High"], ordered=True)
df_cleaned["Parental_Involvement"] =  df_cleaned["Parental_Involvement"].astype(Parental_Involvement_Type)

Teacher_Quality_Type = CategoricalDtype(categories=["Low", "Medium", "High"], ordered=True)
df_cleaned["Teacher_Quality"] =  df_cleaned["Teacher_Quality"].astype(Teacher_Quality_Type)

Access_to_Resources_Type = CategoricalDtype(categories=["Low", "Medium", "High"], ordered=True)
df_cleaned["Access_to_Resources"] =  df_cleaned["Access_to_Resources"].astype(Access_to_Resources_Type)

Motivation_Level_Type = CategoricalDtype(categories=["Low", "Medium", "High"], ordered=True)
df_cleaned["Motivation_Level"] =  df_cleaned["Motivation_Level"].astype(Motivation_Level_Type)

Family_Income_Type = CategoricalDtype(categories=["Low", "Medium", "High"], ordered=True)
df_cleaned["Family_Income"] =  df_cleaned["Family_Income"].astype(Family_Income_Type)

Peer_Influence_Type = CategoricalDtype(categories=['Negative','Neutral','Positive'], ordered=True)
df_cleaned["Peer_Influence"] =  df_cleaned["Peer_Influence"].astype(Peer_Influence_Type)

Distance_from_Home_Type = CategoricalDtype(categories=['Near', 'Moderate', 'Far'], ordered=True)
df_cleaned["Distance_from_Home"] =  df_cleaned["Distance_from_Home"].astype(Distance_from_Home_Type)

# Kiểm tra kiểu dữ liệu của từng cột
print("Kiểu dữ liệu của từng cột: ")
print(df_cleaned.info())
print(df_cleaned.head())

# Phân tách các biến liên tục và biến phân loại
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

# Xuất DataFrame đã làm sạch thành file CSV mới
df_cleaned.to_csv('data_source/cleaned_data.csv', index=False)
print("\nFile cleaned_data.csv đã được lưu vào thư mục data.")
