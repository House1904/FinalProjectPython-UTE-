import numpy as np
import pandas as pd

# Đọc dữ liệu từ file CSV gốc trong thư mục data
df = pd.read_csv('data_source/StudentPerformanceFactors.csv')

print(f"Ma trận DataFrame: {df.shape}")

print("Năm dòng đầu của DF: ")
print(df.head())

print(f"Số giá trị trùng lặp: {df.duplicated().sum()}")

print("Số giá trị bị NULL: ")
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

# Loại bỏ các giá trị ngoại lệ
df_cleaned = df_na[df_na['Exam_Score'] <= 100]
print("\nSau khi xử lí điểm vượt quá 100: ")
print(df_cleaned.describe())

# Kiểm tra kiểu dữ liệu của từng cột
print("Kiểu dữ liệu của từng cột: ")
print(df_cleaned.info())
print(df_cleaned.head())

# Phân tách các biến số và biến phân loại
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
