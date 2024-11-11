# Basic
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings('ignore')

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

# 1. VẼ BIỂU ĐỒ ĐƠN CHO TỪNG THUỘC TÍNH RỒI PHÂN TÍCH -> ĐƯA RA NHẬN ĐỊNH

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

print("-" * 20)
print("\nNhận định về Distribution of Hours Studied.")
#Tính toán các ngưỡng 
below_10 = df_cleaned[df_cleaned['Hours_Studied'] <= 10]
above_20 = df_cleaned[df_cleaned['Hours_Studied'] >= 20]
between_11_and_19 = df_cleaned[(df_cleaned['Hours_Studied'] >= 11) & (df_cleaned['Hours_Studied'] <= 19)]

#Tính toán tỉ lệ phần trăm
percent_below_10 = (len(below_10) / len(df_cleaned)) * 100
percent_above_20 = (len(above_20) / len(df_cleaned)) * 100
percent_between_11_and_19 = (len(between_11_and_19) / len(df_cleaned)) * 100

# Kết quả
print(f"Phần trăm số giờ học bài dưới 10: {percent_below_10:.2f}%")
print(f"Phần trăm số giờ học bài trên 20: {percent_above_20:.2f}%")
print(f"Phần trăm số giờ học bài trong khoảng 11 đến 19: {percent_between_11_and_19:.2f}%")


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
#Tính toán các ngưỡng 
below_69 = df_cleaned[df_cleaned['Attendance'] <= 69]
above_80 = df_cleaned[df_cleaned['Attendance'] >= 80]
between_70_and_79 = df_cleaned[(df_cleaned['Attendance'] >= 70) & (df_cleaned['Attendance'] <= 79)]

#Tính toán tỉ lệ phần trăm
percent_below_69 = (len(below_69) / len(df_cleaned)) * 100
percent_above_80 = (len(above_80) / len(df_cleaned)) * 100
percent_between_70_and_79 = (len(between_70_and_79) / len(df_cleaned)) * 100

# Kết quả
print(f"Phần trăm tham dự dưới 69: {percent_below_69:.2f}%")
print(f"Phần trăm tham dự trên 80: {percent_above_80:.2f}%")
print(f"Phần trăm tham dự trong khoảng 70 đến 79: {percent_between_70_and_79:.2f}%")

# # Histogram cho Parental_Involvement
# counts = df_cleaned['Parental_Involvement'].value_counts()
# counts.plot(kind='bar', color=['red', 'orange', 'green'], edgecolor='black', alpha=0.5)
# plt.title('Distribution of Parental Involvement')
# plt.xlabel('Parental Involvement')
# plt.ylabel('Frequency')
# plt.xticks(rotation=0)
# plt.grid(axis='y', alpha=0.75)
# plt.show()

# print("-" * 20)
# print("\nNhận định về Distribution of Parental Involvement.")
# # Tính toán số lượng
# low_involvement = df_cleaned[df_cleaned['Parental_Involvement'] == 'Low']
# medium_involvement = df_cleaned[df_cleaned['Parental_Involvement'] == 'Medium']
# high_involvement = df_cleaned[df_cleaned['Parental_Involvement'] == 'High']

# # Tính toán tỷ lệ phần trăm
# percent_low = (len(low_involvement) / len(df_cleaned)) * 100
# percent_medium = (len(medium_involvement) / len(df_cleaned)) * 100
# percent_high = (len(high_involvement) / len(df_cleaned)) * 100

# # Kết quả
# print(f"Phần trăm tham gia của phụ huynh ở mức thấp: {percent_low:.2f}%")
# print(f"Phần trăm tham gia của phụ huynh ở mức trung bình: {percent_medium:.2f}%")
# print(f"Phần trăm tham gia của phụ huynh ở mức cao: {percent_high:.2f}%")


# # Histogram cho Access_to_Resources
# counts = df_cleaned['Access_to_Resources'].value_counts()
# counts.plot(kind='bar', color=['cyan', 'magenta', 'green'], edgecolor='black', alpha=0.5)
# plt.title('Distribution of Access to Resources')
# plt.xlabel('Access to Resources')
# plt.ylabel('Frequency')
# plt.xticks(rotation=0)
# plt.grid(axis='y', alpha=0.75)
# plt.show()

# print("-" * 20)
# print("\nNhận định về Distribution of Access to Resources.")
# # Tính toán số lượng
# low_access = df_cleaned[df_cleaned['Access_to_Resources'] == 'Low']
# medium_access = df_cleaned[df_cleaned['Access_to_Resources'] == 'Medium']
# high_access = df_cleaned[df_cleaned['Access_to_Resources'] == 'High']

# # Tính toán tỷ lệ phần trăm
# percent_low = (len(low_access) / len(df_cleaned)) * 100
# percent_medium = (len(medium_access) / len(df_cleaned)) * 100
# percent_high = (len(high_access) / len(df_cleaned)) * 100

# # Kết quả
# print(f"Phần trăm truy cập vào dữ liệu ở mức thấp: {percent_low:.2f}%")
# print(f"Phần trăm truy cập vào dữ liệu ở mức trung bình: {percent_medium:.2f}%")
# print(f"Phần trăm truy cập vào dữ liệu ở mức cao: {percent_high:.2f}%")


# # Histogram cho Extracurricular_Activities
# counts = df_cleaned['Extracurricular_Activities'].value_counts()
# counts.plot(kind='bar', color=['red', 'green'], edgecolor='black', alpha=0.5)
# plt.title('Distribution of Extracurricular Activities')
# plt.xlabel('Extracurricular Activities')
# plt.ylabel('Frequency')
# plt.xticks(rotation=0)
# plt.grid(axis='y', alpha=0.75)
# plt.show()

# print("-" * 20)
# print("\nNhận định về Distribution of Extracurricular Activitiess.")
# # Tính toán số lượng
# yes_activitiess = df_cleaned[df_cleaned['Extracurricular_Activities'] == 'Yes']
# no_activitiess = df_cleaned[df_cleaned['Extracurricular_Activities'] == 'No']

# # Tính toán tỷ lệ phần trăm
# percent_yes = (len(yes_activitiess) / len(df_cleaned)) * 100
# percent_no = (len(no_activitiess) / len(df_cleaned)) * 100

# # Kết quả
# print(f"Phần trăm có hoạt động ngoại khóa: {percent_yes:.2f}%")
# print(f"Phần trăm không hoạt động ngoại khóa: {percent_no:.2f}%")


# # Histogram cho Sleep_Hours
# plt.figure(figsize=(10, 6))
# sns.histplot(df_cleaned['Sleep_Hours'], bins=8, kde=True, color='blue', edgecolor='black', alpha=0.5)
# plt.title('Distribution of Sleep Hours')
# plt.xlabel('Sleep Hours')
# plt.ylabel('Frequency')
# plt.xticks(range(3, 13))
# plt.grid(axis='y', alpha=0.4)
# plt.show()

# print("-" * 20)
# print("\nNhận định về Distribution of Sleep Hours.")
# #Tính toán các ngưỡng 
# below_5 = df_cleaned[df_cleaned['Sleep_Hours'] <= 5]
# above_8 = df_cleaned[df_cleaned['Sleep_Hours'] >= 8]
# between_6_and_7 = df_cleaned[(df_cleaned['Sleep_Hours'] >= 6) & (df_cleaned['Sleep_Hours'] <= 7)]

# #Tính toán tỉ lệ phần trăm
# percent_below_5 = (len(below_5) / len(df_cleaned)) * 100
# percent_above_8 = (len(above_8) / len(df_cleaned)) * 100
# percent_between_6_and_7 = (len(between_6_and_7) / len(df_cleaned)) * 100

# # Kết quả
# print(f"Phần trăm số giờ ngủ dưới 5 giờ: {percent_below_5:.2f}%")
# print(f"Phần trăm số giờ ngủ trên 8 giờ: {percent_above_8:.2f}%")
# print(f"Phần trăm số giờ ngủ trong khoảng 6 đến 7 giờ: {percent_between_6_and_7:.2f}%")

# # Histogram cho Previous_Scores
# plt.hist(df_cleaned['Previous_Scores'], bins=50, color='green', edgecolor='black', alpha=0.5)
# plt.title('Distribution of Previous Scores')
# plt.xlabel('Previous Scores')
# plt.ylabel('Frequency')
# plt.xlim(50, 100)
# plt.grid(axis='y', alpha=0.75)
# plt.show()

# print("-" * 20)
# print("\nNhận định về Distribution of Previous Scoress.")
# #Tính toán các ngưỡng 
# below_69 = df_cleaned[df_cleaned['Previous_Scores'] <= 69]
# above_90 = df_cleaned[df_cleaned['Previous_Scores'] >= 90]
# between_70_and_89 = df_cleaned[(df_cleaned['Previous_Scores'] >= 70) & (df_cleaned['Previous_Scores'] <= 89)]

# #Tính toán tỉ lệ phần trăm
# percent_below_69 = (len(below_69) / len(df_cleaned)) * 100
# percent_above_90 = (len(above_90) / len(df_cleaned)) * 100
# percent_between_70_and_89 = (len(between_70_and_89) / len(df_cleaned)) * 100

# # Kết quả
# print(f"Phần trăm điểm dưới 69: {percent_below_69:.2f}%")
# print(f"Phần trăm điểm trên 90: {percent_above_90:.2f}%")
# print(f"Phần trăm điểm trong khoảng 70 đến 89 giờ: {percent_between_70_and_89:.2f}%")

# # Histogram cho Motivation_Level
# counts = df_cleaned['Motivation_Level'].value_counts()
# counts.plot(kind='bar', color=['yellow', 'green', 'red'], edgecolor='black', alpha=0.5)
# plt.title('Distribution of Motivation Level')
# plt.xlabel('Motivation Level')
# plt.ylabel('Frequency')
# plt.xticks(rotation=0)
# plt.grid(axis='y', alpha=0.75)
# plt.show()

# # Histogram cho Internet_Access
# counts = df_cleaned['Internet_Access'].value_counts()
# counts.plot(kind='bar', color=['purple', 'red'], edgecolor='black', alpha=0.5)
# plt.title('Distribution of Internet Access')
# plt.xlabel('Internet Access')
# plt.ylabel('Frequency')
# plt.xticks(rotation=0)
# plt.grid(axis='y', alpha=0.75)
# plt.show()

# # Histogram cho Tutoring_Sessions
# plt.figure(figsize=(10, 6))
# sns.histplot(df_cleaned['Tutoring_Sessions'], bins=8, kde=True, color='purple', edgecolor='black', alpha=0.5)
# plt.title('Distribution of Tutoring Sessions')
# plt.xlabel('Tutoring Sessions')
# plt.ylabel('Frequency')
# plt.xticks(range(0, 9))
# plt.grid(axis='y', alpha=0.4)
# plt.show()

# # Histogram cho Family_Income
# counts = df_cleaned['Family_Income'].value_counts()
# counts.plot(kind='bar', color=['purple', 'yellow', 'pink'], edgecolor='black', alpha=0.5)
# plt.title('Distribution of Family Income')
# plt.xlabel('Family Income')
# plt.ylabel('Frequency')
# plt.xticks(rotation=0)
# plt.grid(axis='y', alpha=0.75)
# plt.show()

# # Histogram cho Teacher_Quality
# counts = df_cleaned['Teacher_Quality'].value_counts()
# counts.plot(kind='bar', color=['fuchsia', 'blue', 'orange'], edgecolor='black', alpha=0.5)
# plt.title('Distribution of Teacher Quality')
# plt.xlabel('Teacher Quality')
# plt.ylabel('Frequency')
# plt.xticks(rotation=0)
# plt.grid(axis='y', alpha=0.75)
# plt.show()

# # Histogram cho School_Type
# counts = df_cleaned['School_Type'].value_counts()
# counts.plot(kind='bar', color=['green', 'violet'], edgecolor='black', alpha=0.5)
# plt.title('Distribution of School Type')
# plt.xlabel('School Type')
# plt.ylabel('Frequency')
# plt.xticks(rotation=0)
# plt.grid(axis='y', alpha=0.75)
# plt.show()

# # Histogram cho Peer_Influence
# counts = df_cleaned['Peer_Influence'].value_counts()
# counts.plot(kind='bar', color=['violet', 'lime', 'maroon'], edgecolor='black', alpha=0.5)
# plt.title('Distribution of Peer Influence')
# plt.xlabel('Peer Influence')
# plt.ylabel('Frequency')
# plt.xticks(rotation=0)
# plt.grid(axis='y', alpha=0.75)
# plt.show()

# # Histogram cho Physical_Activity
# plt.figure(figsize=(10, 6))
# sns.histplot(df_cleaned['Physical_Activity'], bins=8, kde=True, color='teal', edgecolor='black', alpha=0.5)
# plt.title('Distribution of Physical Activity')
# plt.xlabel('Physical Activity')
# plt.ylabel('Frequency')
# plt.xticks(range(0, 7))
# plt.grid(axis='y', alpha=0.4)
# plt.show()

# # Histogram cho Learning_Disabilities
# counts = df_cleaned['Learning_Disabilities'].value_counts()
# counts.plot(kind='bar', color=['coral', 'olive'], edgecolor='black', alpha=0.5)
# plt.title('Distribution of Learning Disabilities')
# plt.xlabel('Learning Disabilities')
# plt.ylabel('Frequency')
# plt.xticks(rotation=0)
# plt.grid(axis='y', alpha=0.75)
# plt.show()

# # Histogram cho Parental_Education_Level
# counts = df_cleaned['Parental_Education_Level'].value_counts()
# counts.plot(kind='bar', color=['green', 'blue', 'orange'], edgecolor='black', alpha=0.5)
# plt.title('Distribution of Parental Education Level')
# plt.xlabel('Parental Education Level')
# plt.ylabel('Frequency')
# plt.xticks(rotation=0)
# plt.grid(axis='y', alpha=0.75)
# plt.show()

# # Histogram cho Distance_from_Home
# counts = df_cleaned['Distance_from_Home'].value_counts()
# counts.plot(kind='bar', color=['coral', 'olive', 'lime'], edgecolor='black', alpha=0.5)
# plt.title('Distribution of Distance from Home')
# plt.xlabel('Distance from Home')
# plt.ylabel('Frequency')
# plt.xticks(rotation=0)
# plt.grid(axis='y', alpha=0.75)
# plt.show()

# Histogram cho Gender
counts = df_cleaned['Gender'].value_counts()
counts.plot(kind='bar', color=['azure', 'cyan'], edgecolor='black', alpha=0.5)
plt.title('Distribution of Gender')
plt.xlabel('Gender')
plt.ylabel('Frequency')
plt.xticks(rotation=0)
plt.grid(axis='y', alpha=0.75)
plt.show()

# 2.  Biểu đồ phân tán (scatter plots) 
# để thể hiện mối quan hệ giữa các đặc trưng số và biến mục tiêu (target variable)

# Sơ đồ phân tán giữa Hours_Studied và Exam_Score
plt.subplot(1, 3, 1)
sns.scatterplot(x=df_cleaned['Hours_Studied'], y=df_cleaned['Exam_Score'], alpha=0.6)
plt.title('Scatter Plot: Hours Studied vs Exam Score')
plt.xlabel('Hours Studied')
plt.ylabel('Exam Score')

# Sơ đồ phân tán giữa Attendance và Exam_Score
plt.subplot(1, 3, 2)
sns.scatterplot(x=df_cleaned['Attendance'], y=df_cleaned['Exam_Score'], alpha=0.6)
plt.title('Scatter Plot: Attendance vs Exam Score')
plt.xlabel('Attendance')
plt.ylabel('Exam Score')

# Sơ đồ phân tán giữa Previous_Scores và Exam_Score
plt.subplot(1, 3, 3)
sns.scatterplot(x=df_cleaned['Previous_Scores'], y=df_cleaned['Exam_Score'], alpha=0.6)
plt.title('Scatter Plot: Previous Scores vs Exam Score')
plt.xlabel('Previous Scores')
plt.ylabel('Exam Score')

# Điều chỉnh bố cục
plt.tight_layout()
plt.show()

# Tạo biểu đồ phân tán
fig, axes = plt.subplots(1, 3, figsize=(15, 5))  # Tạo 1 hàng, 3 cột

for idx, col in enumerate(num_col):
    # Vẽ biểu đồ phân tán với Seaborn
    sns.scatterplot(x=df_cleaned[col], y=df_cleaned[target], ax=axes[idx], palette='husl', hue=df_cleaned['Extracurricular_Activities'], style=df_cleaned['Extracurricular_Activities'], markers=["o", "s"])
    
    # Cài đặt tiêu đề và nhãn cho trục
    axes[idx].set_title(f'Relationship between {col} & {target}')
    axes[idx].set_xlabel(col)
    axes[idx].set_ylabel(target)
    
    # Đặt legend cho biểu đồ
    axes[idx].legend(loc='upper center', bbox_to_anchor=(0.5, 1.25), ncol=2, title='Extracurricular Activities')

# Điều chỉnh bố cục cho đẹp
plt.tight_layout()
plt.show()

# fig, axes = plt.subplots(nrows=len(cat_col) // 2 + len(cat_col) % 2, ncols=2, figsize=(10, 20))
# axes = axes.flatten()

# for i, column in enumerate(cat_col):
#     value_count = df_cleaned[column].value_counts()
#     value_count.plot(kind='pie', autopct='%0.2f%%', ax=axes[i])
#     axes[i].set_title(column)
#     axes[i].set_ylabel('')   


# for j in range(i + 1, len(axes)):
#     fig.delaxes(axes[j])

# plt.tight_layout()
# plt.show()

# Selecting only numerical columns
numerical_df = df_cleaned.select_dtypes(include='number')

# Calculate correlation matrix for numerical_df
corr_df = numerical_df.corr()

# Plot heatmap for numerical_df
plt.figure(figsize=(8, 6))
sns.heatmap(corr_df, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap for numeric columns')
plt.show()

# Vẽ boxplot cho từng biến phân loại riêng biệt
for col in cat_col:
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=df_cleaned[col], y=df_cleaned[target], palette='Reds')
    plt.title(f'Relationship between {col} and {target}')
    plt.xlabel(col)
    plt.ylabel(target)
    plt.xticks(rotation=45)  # Xoay nhãn trục X nếu cần
    plt.tight_layout()  # Đảm bảo khoảng cách hợp lý
    plt.show()  # Hiển thị biểu đồ trước khi tiếp tục vẽ biểu đồ tiếp theo