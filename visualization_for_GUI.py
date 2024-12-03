import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
from scipy.stats import ttest_ind

df_cleaned = pd.read_csv('data_source\\cleaned_data.csv') # Lấy dữ liệu chuẩn từ file đã làm sạch

# 1. VẼ BIỂU ĐỒ TẦN SUẤT VÀ CỘT CHO CÁC THUỘC TÍNH ĐƠN LẺ (HISTOGRAM và BAR)
# Histogram cho biến mục tiêu Exam_Score 
def plot_exam_score_distribution():
    global df_cleaned

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(df_cleaned["Exam_Score"], bins = 45, kde=True, color='red', edgecolor = 'black', alpha = 0.5, ax=ax )
    ax.set_title('Distribution of Exam Score')
    ax.set_xlabel('Exam Score')
    ax.set_ylabel('Frequency')
    ax.set_xlim(55, 100)
    plt.grid(axis='y', alpha = 0.75)
    return fig

# Histogram cho Hours_Studied
def plot_hours_studied_distribution():
    global df_cleaned

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(df_cleaned['Hours_Studied'], bins = 45, kde=True, color='blue', edgecolor='black', alpha=0.5, ax=ax)
    ax.set_title('Distribution of Hours Studied')
    ax.set_xlabel('Hours Studied')
    ax.set_ylabel('Frequency')
    ax.set_xlim(0, 50)
    plt.grid(axis='y', alpha=0.75)
    return fig

# Histogram cho Attendance
def plot_attendance_distribution():
    global df_cleaned

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(df_cleaned['Attendance'], bins=45, kde=True, color='violet', edgecolor='black', alpha=0.5, ax=ax)
    ax.set_title('Distribution of Attendance')
    ax.set_xlabel('Attendance')
    ax.set_ylabel('Frequency')
    ax.set_xlim(60, 100)
    plt.grid(axis='y', alpha=0.75)
    return fig

# Histogram cho Previous_Scores
def plot_previous_scores_distribution():
    global df_cleaned

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(df_cleaned['Previous_Scores'], bins=80, kde=True, color='green', edgecolor='black', alpha=0.5, ax=ax)
    ax.set_title('Distribution of Previous Scores')
    ax.set_xlabel('Previous Scores')
    ax.set_ylabel('Frequency')
    ax.set_xlim(50, 100)
    plt.grid(axis='y', alpha=0.75)
    return fig

# Bar cho Parental_Involvement
def plot_parental_involvement_distribution():
    global df_cleaned

    fig, ax = plt.subplots(figsize=(10, 6))
    counts = df_cleaned['Parental_Involvement'].value_counts()
    counts.plot(kind='bar', color=['red', 'orange', 'green'], edgecolor='black', alpha=0.5, ax=ax)
    ax.set_title('Distribution of Parental Involvement')
    ax.set_xlabel('Parental Involvement')
    ax.set_ylabel('Frequency')
    ax.set_xticklabels(counts.index, rotation=0)
    plt.grid(axis='y', alpha=0.75)
    return fig

# Bar cho Access_to_Resources
def plot_access_to_resources_distribution():
    global df_cleaned

    fig, ax = plt.subplots(figsize=(10, 6))
    counts = df_cleaned['Access_to_Resources'].value_counts()
    counts.plot(kind='bar', color=['cyan', 'magenta', 'green'], edgecolor='black', alpha=0.5, ax=ax)
    ax.set_title('Distribution of Access to Resources')
    ax.set_xlabel('Access to Resources')
    ax.set_ylabel('Frequency')
    ax.set_xticklabels(counts.index, rotation=0)
    plt.grid(axis='y', alpha=0.75)
    return fig

# Bar cho Extracurricular_Activities
def plot_extracurricular_activities_distribution():
    global df_cleaned

    fig, ax = plt.subplots(figsize=(10,6))
    counts = df_cleaned['Extracurricular_Activities'].value_counts()
    counts.plot(kind='bar', color=['red', 'green'], edgecolor='black', alpha=0.5, ax=ax)
    ax.set_title('Distribution of Extracurricular Activities')
    ax.set_xlabel('Extracurricular Activities')
    ax.set_ylabel('Frequency')
    ax.set_xticklabels(counts.index, rotation=0)
    plt.grid(axis='y', alpha=0.75)
    return fig

# Bar cho Sleep_Hours
def plot_sleep_hours_distribution():
    global df_cleaned

    fig, ax = plt.subplots(figsize=(10, 6))
    counts = df_cleaned['Sleep_Hours'].value_counts().sort_index()
    colors = ['#FF6347', '#FFD700', '#ADFF2F', '#00BFFF', '#FF69B4', '#8A2BE2', 
              '#FF4500', '#32CD32', '#FF1493', '#C71585']
    counts.plot(kind='bar', color=colors[:len(counts)], edgecolor='black', alpha=0.5, ax=ax)
    ax.set_title('Distribution of Sleep Hours')
    ax.set_xlabel('Sleep Hours')
    ax.set_ylabel('Frequency')
    ax.set_xticklabels(counts.index, rotation=0)
    plt.grid(axis='y', alpha=0.75)
    return fig

# Bar cho Motivation_Level
def plot_motivation_level_distribution():
    global df_cleaned

    fig, ax = plt.subplots(figsize=(10, 6))
    counts = df_cleaned['Motivation_Level'].value_counts()
    counts.plot(kind='bar', color=['yellow', 'green', 'red'], edgecolor='black', alpha=0.5, ax=ax)
    ax.set_title('Distribution of Motivation Level')
    ax.set_xlabel('Motivation Level')
    ax.set_ylabel('Frequency')
    ax.set_xticklabels(counts.index, rotation=0)
    plt.grid(axis='y', alpha=0.75)
    return fig

# Bar cho Internet_Access
def plot_internet_access_distribution():
    global df_cleaned

    fig, ax = plt.subplots(figsize=(10, 6)) 
    counts = df_cleaned['Internet_Access'].value_counts()
    counts.plot(kind='bar', color=['purple', 'red'], edgecolor='black', alpha=0.5, ax=ax)
    ax.set_title('Distribution of Internet Access')
    ax.set_xlabel('Internet Access')
    ax.set_ylabel('Frequency')
    ax.set_xticklabels(counts.index, rotation=0)
    plt.grid(axis='y', alpha=0.75)
    return fig

# Bar cho Tutoring_Sessions 
def plot_tutoring_sessions_distribution():
    global df_cleaned

    fig, ax = plt.subplots(figsize=(10, 6))
    counts = df_cleaned['Tutoring_Sessions'].value_counts().sort_index()
    colors = ['purple', 'blue', 'green', 'orange', 'red', 'yellow', 'brown', 'pink', 'cyan']
    counts.plot(kind='bar', color=colors[:len(counts)], edgecolor='black', alpha=0.7, ax=ax)
    ax.set_title('Distribution of Tutoring Sessions')
    ax.set_xlabel('Tutoring Sessions')
    ax.set_ylabel('Frequency')
    ax.set_xticklabels(range(9), rotation=0)
    plt.grid(axis='y', alpha=0.75)
    return fig

# Bar cho Family_Income
def plot_family_income_distribution():
    global df_cleaned

    fig, ax = plt.subplots(figsize=(10, 6))
    counts = df_cleaned['Family_Income'].value_counts()
    counts.plot(kind='bar', color=['purple', 'yellow', 'pink'], edgecolor='black', alpha=0.5, ax=ax)
    ax.set_title('Distribution of Family Income')
    ax.set_xlabel('Family Income')
    ax.set_ylabel('Frequency')
    ax.set_xticklabels(counts.index, rotation=0)
    plt.grid(axis='y', alpha=0.75)
    return fig

# Bar cho Teacher_Quality
def plot_teacher_quality_distribution():
    global df_cleaned

    fig, ax = plt.subplots(figsize=(10, 6))
    counts = df_cleaned['Teacher_Quality'].value_counts()
    counts.plot(kind='bar', color=['fuchsia', 'blue', 'orange'], edgecolor='black', alpha=0.5, ax=ax)
    ax.set_title('Distribution of Teacher Quality')
    ax.set_xlabel('Teacher Quality')
    ax.set_ylabel('Frequency')
    ax.set_xticklabels(counts.index, rotation=0)
    plt.grid(axis='y', alpha=0.75)
    return fig

# Bar cho School_Type
def plot_school_type_distribution():
    global df_cleaned

    fig, ax = plt.subplots(figsize=(10, 6))
    counts = df_cleaned['School_Type'].value_counts()
    counts.plot(kind='bar', color=['green', 'violet'], edgecolor='black', alpha=0.5, ax=ax)
    ax.set_title('Distribution of School Type')
    ax.set_xlabel('School Type')
    ax.set_ylabel('Frequency')
    ax.set_xticklabels(counts.index, rotation=0)
    plt.grid(axis='y', alpha=0.75)
    return fig

# Bar cho Peer_Influence
def plot_peer_influence_distribution():
    global df_cleaned

    fig, ax = plt.subplots(figsize=(10,6))
    counts = df_cleaned['Peer_Influence'].value_counts()
    counts.plot(kind='bar', color=['violet', 'lime', 'maroon'], edgecolor='black', alpha=0.5, ax=ax)
    ax.set_title('Distribution of Peer Influence')
    ax.set_xlabel('Peer Influence')
    ax.set_ylabel('Frequency')
    ax.set_xticklabels(counts.index, rotation=0)
    return fig

# Bar cho Physical_Activity
def plot_physical_activity_distribution():
    global df_cleaned

    fig, ax = plt.subplots(figsize=(10,6))
    counts = df_cleaned['Physical_Activity'].value_counts().sort_index()
    colors = ['teal', 'orange', 'blue', 'green', 'purple', 'red', 'pink']
    counts.plot(kind='bar', color=colors[:len(counts)], edgecolor='black', alpha=0.7, ax=ax)
    ax.set_title('Distribution of Physical Activity')
    ax.set_xlabel('Physical Activity')
    ax.set_ylabel('Frequency')
    ax.set_xticklabels(range(7), rotation=0)
    plt.grid(axis='y', alpha=0.75)
    return fig

# Bar cho Learning_Disabilities
def plot_learning_disabilities_distribution():
    global df_cleaned

    fig, ax = plt.subplots(figsize=(10,6))
    counts = df_cleaned['Learning_Disabilities'].value_counts()
    counts.plot(kind='bar', color=['coral', 'olive'], edgecolor='black', alpha=0.5, ax=ax)
    ax.set_title('Distribution of Learning Disabilities')
    ax.set_xlabel('Learning Disabilities')
    ax.set_ylabel('Frequency')
    ax.set_xticklabels(counts.index, rotation=0)
    plt.grid(axis='y', alpha=0.75)
    return fig

# Bar cho Parental_Education_Level
def plot_parental_education_level_distribution():
    global df_cleaned

    fig, ax = plt.subplots(figsize=(10,6))
    counts = df_cleaned['Parental_Education_Level'].value_counts()
    counts.plot(kind='bar', color=['green', 'blue', 'orange'], edgecolor='black', alpha=0.5, ax=ax)
    ax.set_title('Distribution of Parental Education Level')
    ax.set_xlabel('Parental Education Level')
    ax.set_ylabel('Frequency')
    ax.set_xticklabels(counts.index, rotation=0)
    plt.grid(axis='y', alpha=0.75)
    return fig

# Bar cho Distance_from_Home
def plot_distance_from_home_distribution():
    global df_cleaned

    fig, ax = plt.subplots(figsize=(10,6))  
    counts = df_cleaned['Distance_from_Home'].value_counts()
    counts.plot(kind='bar', color=['coral', 'olive', 'lime'], edgecolor='black', alpha=0.5, ax=ax)
    ax.set_title('Distribution of Distance from Home')
    ax.set_xlabel('Distance from Home')
    ax.set_ylabel('Frequency')
    ax.set_xticklabels(counts.index, rotation=0)
    plt.grid(axis='y', alpha=0.75)
    return fig

# Bar cho Gender
def plot_gender_distribution():
    global df_cleaned

    fig, ax = plt.subplots(figsize=(10,6))
    counts = df_cleaned['Gender'].value_counts()
    counts.plot(kind='bar', color=['azure', 'cyan'], edgecolor='black', alpha=0.5, ax=ax)
    ax.set_title('Distribution of Gender')
    ax.set_xlabel('Gender')
    ax.set_ylabel('Frequency')
    ax.set_xticklabels(counts.index, rotation=0)
    plt.grid(axis='y', alpha=0.75)
    return fig

# 2. VẼ BIỂU ĐỒ BIỂU DIỄN QUAN HỆ PHÂN TÁN (SỐ) VÀ BIỂU ĐỒ HỘP (PHÂN LOẠI) VỚI BIẾN MỤC TIÊU EXAM_SCORE
# Vẽ biểu đồ phân tán Hours Studied và Exam Score
def scatterplot_Hours_Studied_and_Exam_Score():
    global df_cleaned

    fig, ax = plt.subplots(figsize=(10,6))
    sns.scatterplot(x=df_cleaned['Hours_Studied'], y=df_cleaned['Exam_Score'], color='green', alpha=0.7, ax=ax)
    ax.set_title('Scatter Plot: Hours Studied vs Exam Score')
    ax.set_xlabel('Hours Studied')
    ax.set_ylabel('Exam Score')
    plt.grid(True)
    return fig

# Vẽ biểu đồ phân tán Attendance và Exam Score
def scatterplot_Attendance_and_Exam_Score():
    global df_cleaned

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(x=df_cleaned['Attendance'], y=df_cleaned['Exam_Score'], color='gray', alpha=0.7, ax=ax)
    ax.set_title('Scatter Plot: Attendance vs Exam Score')
    ax.set_xlabel('Attendance')
    ax.set_ylabel('Exam Score')
    plt.grid(True)
    return fig

# Vẽ biểu đồ phân tán Previous Scores và Exam Score
def scatterplot_Previous_Scores_and_Exam_Score():
    global df_cleaned

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(x=df_cleaned['Previous_Scores'], y=df_cleaned['Exam_Score'], color='salmon', alpha=0.7, ax=ax)
    ax.set_title('Scatter Plot: Previous Scores vs Exam Score')
    ax.set_xlabel('Previous Scores')
    ax.set_ylabel('Exam Score')
    plt.grid(True)
    return fig

# Xây dựng sơ đồ phân tán dựa trên các đặc điểm số (tính đến các hoạt động ngoại khóa):
def scatterplot_Numcol_and_Exam_Score_with_Extracurricular_Activities():
    global df_cleaned

    fig, axes = plt.subplots(1, 3, figsize=(12, 5))  
    for idx, col in enumerate(['Hours_Studied', 'Attendance', 'Previous_Scores']):
        sns.scatterplot(x=df_cleaned[col], y=df_cleaned['Exam_Score'], 
                        ax=axes[idx], palette='husl', hue=df_cleaned['Extracurricular_Activities'])  
        axes[idx].set_title(f'Relationship b/t {col} & Exam_Score')  
        axes[idx].legend(loc='upper center', bbox_to_anchor=(0.5, 1.25), ncol=2, 
                         title='Extracurricular_Activities')
        axes[idx].set_xlabel(col)  
        axes[idx].set_ylabel('Exam_Score')  
    plt.tight_layout()  

    # Chia thành 2 nhóm: tham gia và không tham gia
    group_yes = df_cleaned[df_cleaned['Extracurricular_Activities'] == 'Yes']['Exam_Score']
    group_no = df_cleaned[df_cleaned['Extracurricular_Activities'] == 'No']['Exam_Score']

    # Kiểm định t-test
    t_stat, p_value = ttest_ind(group_yes, group_no)
   # Kiểm tra p-value và in kết quả
    if p_value < 0.05:
        print(f"T-statistic: {t_stat}, P-value: {p_value}")
        print("Kết luận: Có sự khác biệt có ý nghĩa thống kê giữa hai nhóm.")
    
    # Kiểm tra dấu của T-statistic để xác định nhóm nào có điểm cao hơn
        if t_stat > 0:
            print("Nhóm có hoạt động ngoại khóa có điểm thi cao hơn nhóm không có hoạt động ngoại khóa.")
        else:
            print("Nhóm không có hoạt động ngoại khóa có điểm thi cao hơn nhóm có hoạt động ngoại khóa.")
    else:
        print(f"T-statistic: {t_stat}, P-value: {p_value}")
        print("Kết luận: Không có sự khác biệt có ý nghĩa thống kê giữa hai nhóm.")
    
    return fig

# Xây dựng sơ đồ phân tán dựa trên các đặc điểm số (tính đến giới tính):
def scatterplot_Numcol_and_Exam_Score_with_Gender():
    global df_cleaned

    fig, axes = plt.subplots(1, 3, figsize=(12, 5))  
    for idx, col in enumerate(['Hours_Studied', 'Attendance', 'Previous_Scores']):
        sns.scatterplot(x=df_cleaned[col], y=df_cleaned['Exam_Score'], 
                        ax=axes[idx], palette='Accent', hue=df_cleaned['Gender'])  
        axes[idx].set_title(f'Relationship b/t {col} & Exam_Score')  
        axes[idx].legend(loc='upper center', bbox_to_anchor=(0.5, 1.25), ncol=2, 
                         title='Gender')
        axes[idx].set_xlabel(col)  
        axes[idx].set_ylabel('Exam_Score')  
    plt.tight_layout()  

     # Chia thành 2 nhóm: nam và nữ
    group_yes = df_cleaned[df_cleaned['Gender'] == 'Male']['Exam_Score']
    group_no = df_cleaned[df_cleaned['Gender'] == 'Female']['Exam_Score']

    # Kiểm định t-test
    t_stat, p_value = ttest_ind(group_yes, group_no)
    # Kiểm tra p-value và in kết quả
    if p_value < 0.05:
        print(f"T-statistic: {t_stat}, P-value: {p_value}")
        print("Kết luận: Có sự khác biệt có ý nghĩa thống kê giữa hai nhóm.")
    
    # Kiểm tra dấu của T-statistic để xác định nhóm nào có điểm cao hơn
        if t_stat > 0:
            print("Nhóm sinh viên nam có điểm thi cao hơn nhóm sinh viên nữ.")
        else:
            print("Nhóm sinh viên nữ có điểm thi cao hơn nhóm sinh viên nam.")
    else:
        print(f"T-statistic: {t_stat}, P-value: {p_value}")
        print("Kết luận: Không có sự khác biệt có ý nghĩa thống kê giữa hai nhóm.")

    return fig

# Xây dựng sơ đồ phân tán dựa trên các đặc điểm số (tính đến việc truy cập Internet):
def scatterplot_Numcol_and_Exam_Score_with_Internet_Access():
    global df_cleaned

    fig, axes = plt.subplots(1, 3, figsize=(12, 5))  
    for idx, col in enumerate(['Hours_Studied', 'Attendance', 'Previous_Scores']):
        sns.scatterplot(x=df_cleaned[col], y=df_cleaned['Exam_Score'], 
                        ax=axes[idx], palette='muted', hue=df_cleaned['Internet_Access'])  
        axes[idx].set_title(f'Relationship b/t {col} & Exam_Score')  
        axes[idx].legend(loc='upper center', bbox_to_anchor=(0.5, 1.25), ncol=2, 
                         title='Internet_Access')
        axes[idx].set_xlabel(col)  
        axes[idx].set_ylabel('Exam_Score')  
    plt.tight_layout()  

     # Chia thành 2 nhóm: có truy cập và không truy cập Internet
    group_yes = df_cleaned[df_cleaned['Internet_Access'] == 'Yes']['Exam_Score']
    group_no = df_cleaned[df_cleaned['Internet_Access'] == 'No']['Exam_Score']

    # Kiểm định t-test
    t_stat, p_value = ttest_ind(group_yes, group_no)
    # Kiểm tra p-value và in kết quả
    if p_value < 0.05:
        print(f"T-statistic: {t_stat}, P-value: {p_value}")
        print("Kết luận: Có sự khác biệt có ý nghĩa thống kê giữa hai nhóm.")
    
    # Kiểm tra dấu của T-statistic để xác định nhóm nào có điểm cao hơn
        if t_stat > 0:
            print("Nhóm sinh viên được truy cập Internet có điểm thi cao hơn Nhóm sinh viên không được truy cập Internet.")
        else:
            print("Nhóm sinh viên không được truy cập Internet có điểm thi cao hơn Nhóm sinh viên được truy cập Internet.")
    else:
        print(f"T-statistic: {t_stat}, P-value: {p_value}")
        print("Kết luận: Không có sự khác biệt có ý nghĩa thống kê giữa hai nhóm.")

    return fig

# Xây dựng sơ đồ phân tán dựa trên các đặc điểm số (tính đến Khuyết tật học tập):
def scatterplot_Numcol_and_Exam_Score_with_Learning_Disabilities():
    global df_cleaned

    fig, axes = plt.subplots(1, 3, figsize=(12, 5))  
    for idx, col in enumerate(['Hours_Studied', 'Attendance', 'Previous_Scores']):
        sns.scatterplot(x=df_cleaned[col], y=df_cleaned['Exam_Score'], 
                        ax=axes[idx], palette='colorblind', hue=df_cleaned['Learning_Disabilities'])  
        axes[idx].set_title(f'Relationship b/t {col} & Exam_Score')  
        axes[idx].legend(loc='upper center', bbox_to_anchor=(0.5, 1.25), ncol=2, 
                         title='Learning_Disabilities')
        axes[idx].set_xlabel(col)  
        axes[idx].set_ylabel('Exam_Score')  
    plt.tight_layout()  

     # Chia thành 2 nhóm: tham gia và không tham gia
    group_yes = df_cleaned[df_cleaned['Learning_Disabilities'] == 'Yes']['Exam_Score']
    group_no = df_cleaned[df_cleaned['Learning_Disabilities'] == 'No']['Exam_Score']

    # Kiểm định t-test
    t_stat, p_value = ttest_ind(group_yes, group_no)
    # Kiểm tra p-value và in kết quả
    if p_value < 0.05:
        print(f"T-statistic: {t_stat}, P-value: {p_value}")
        print("Kết luận: Có sự khác biệt có ý nghĩa thống kê giữa hai nhóm.")
    
    # Kiểm tra dấu của T-statistic để xác định nhóm nào có điểm cao hơn
        if t_stat > 0:
            print("Nhóm sinh viên khuyết tật có điểm thi cao hơn Nhóm sinh viên không khuyết tật.")
        else:
            print("Nhóm sinh viên không khuyết tật có điểm thi cao hơn Nhóm sinh viên khuyết tật.")
    else:
        print(f"T-statistic: {t_stat}, P-value: {p_value}")
        print("Kết luận: Không có sự khác biệt có ý nghĩa thống kê giữa hai nhóm.")

    return fig

# Vẽ biểu đồ boxplot Exam_Score và Parental Involvement
def boxplot_Parental_Involvement_and_Exam_Score():
    global df_cleaned

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(x=df_cleaned['Parental_Involvement'], y=df_cleaned['Exam_Score'], palette='Set2', ax=ax)
    ax.set_title('Boxplot: Exam Scores by Parental Involvement')
    ax.set_xlabel('Parental Involvement')
    ax.set_ylabel('Exam Score')
    return fig

# Mã hóa cột thành các giá trị số
df_cleaned['Parental_Involvement_num'] = df_cleaned['Parental_Involvement'].map({'Low': 0, 'Medium': 1, 'High': 2})

# Vẽ biểu đồ boxplot Exam_Score và Access_to_Resources
def boxplot_Access_to_Resources_and_Exam_Score():
    global df_cleaned

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(x=df_cleaned['Access_to_Resources'], y=df_cleaned['Exam_Score'], palette='Set2', ax=ax)
    ax.set_title('Boxplot: Exam Scores by Access to Resources')
    ax.set_xlabel('Access to Resources')
    ax.set_ylabel('Exam Score')
    return fig

# Mã hóa cột thành các giá trị số
df_cleaned['Access_to_Resources_num'] = df_cleaned['Access_to_Resources'].map({'Low': 0, 'Medium': 1, 'High': 2})

# Vẽ biểu đồ boxplot Exam_Score và Extracurricular_Activities
def boxplot_Extracurricular_Activities_and_Exam_Score():
    global df_cleaned

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(data=df_cleaned, x='Extracurricular_Activities', y='Exam_Score', palette=['pink', 'blue'], ax=ax)
    ax.set_title('Boxplot: Exam Score by Extracurricular Activities')
    ax.set_xlabel('Extracurricular Activities')
    ax.set_ylabel('Exam Score')
    return fig

# Mã hóa cột thành các giá trị số
df_cleaned['Extracurricular_Activities_num'] = df_cleaned['Extracurricular_Activities'].map({'Yes': 1, 'No': 0})

# Vẽ biểu đồ boxplot Exam_Score và Sleep_Hours
def boxplot_Sleep_Hours_and_Exam_Score():
    global df_cleaned

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(data=df_cleaned, x='Sleep_Hours', y='Exam_Score', palette='Paired', ax=ax)
    ax.set_title('Boxplot: Exam Score by Sleep Hours')
    ax.set_xlabel('Sleep Hours')
    ax.set_ylabel('Exam Score')
    return fig

# Vẽ biểu đồ boxplot Exam_Score và Motivation_Level
def boxplot_Motivation_Level_and_Exam_Score():
    global df_cleaned

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(x=df_cleaned['Motivation_Level'], y=df_cleaned['Exam_Score'], palette='Set1', ax=ax)
    ax.set_title('Boxplot: Exam Scores by Motivation Level')
    ax.set_xlabel('Motivation Level')
    ax.set_ylabel('Exam Score')
    return fig

# Mã hóa cột thành các giá trị số
df_cleaned['Motivation_Level_num'] = df_cleaned['Motivation_Level'].map({'Low': 0, 'Medium': 1, 'High': 2})

# Vẽ biểu đồ boxplot Exam_Score và Internet_Access
def boxplot_Internet_Access_and_Exam_Score():
    global df_cleaned

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(data=df_cleaned, x='Internet_Access', y='Exam_Score', palette=['red', 'pink'], ax=ax)
    ax.set_title('Boxplot: Exam Score by Internet Access')
    ax.set_xlabel('Internet Access')
    ax.set_ylabel('Exam Score')
    return fig

df_cleaned['Internet_Access_num'] = df_cleaned['Internet_Access'].map({'Yes': 1, 'No': 0})

# Vẽ biểu đồ boxplot Exam_Score và Tutoring_Sessions
def boxplot_Tutoring_Sessions_and_Exam_Score():
    global df_cleaned
    fig, ax = plt.subplots(figsize=(10, 6))

    sns.boxplot(data=df_cleaned, x='Tutoring_Sessions', y='Exam_Score', palette='Set3', ax=ax)

    ax.set_title('Boxplot: Exam Score by Tutoring Sessions')
    ax.set_xlabel('Tutoring Sessions')
    ax.set_ylabel('Exam Score')
    return fig

# Vẽ biểu đồ boxplot Exam_Score và Family_Income
def boxplot_Family_Income_and_Exam_Score():
    global df_cleaned

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(x=df_cleaned['Family_Income'], y=df_cleaned['Exam_Score'], palette='Set2', ax=ax)
    ax.set_title('Boxplot: Exam Scores by Family Income')
    ax.set_xlabel('Family Income')
    ax.set_ylabel('Exam Score')
    return fig

# Mã hóa cột thành các giá trị số
df_cleaned['Family_Income_num'] = df_cleaned['Family_Income'].map({'Low': 0, 'Medium': 1, 'High': 2})

# Vẽ biểu đồ boxplot Exam_Score và Teacher_Quality
def boxplot_Teacher_Quality_and_Exam_Score():
    global df_cleaned

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(x=df_cleaned['Teacher_Quality'], y=df_cleaned['Exam_Score'], palette='Set1', ax=ax)
    ax.set_title('Boxplot: Exam Scores by Teacher Quality')
    ax.set_xlabel('Teacher Quality')
    ax.set_ylabel('Exam Score')
    return fig

# Mã hóa cột thành các giá trị số
df_cleaned['Teacher_Quality_num'] = df_cleaned['Teacher_Quality'].map({'Low': 0, 'Medium': 1, 'High': 2})

# Vẽ biểu đồ Boxplot cho Exam_Score và School_Type
def boxplot_School_Type_and_Exam_Score():
    global df_cleaned

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(x=df_cleaned['School_Type'], y=df_cleaned['Exam_Score'], palette='Set2', ax=ax)
    ax.set_title('Boxplot: Exam Scores by School Type')
    ax.set_xlabel('School Type')
    ax.set_ylabel('Exam Score')
    return fig

# Mã hóa cột thành các giá trị số
df_cleaned['School_Type_num'] = df_cleaned['School_Type'].map({'Public': 0, 'Private': 1})

# Vẽ biểu đồ boxplot Exam_Score và Peer_Influence
def boxplot_Peer_Influence_and_Exam_Score():
    global df_cleaned

    fig, ax = plt.figure(figsize=(10, 6))
    sns.boxplot(x=df_cleaned['Peer_Influence'], y=df_cleaned['Exam_Score'], palette='Set3', ax=ax)
    ax.set_title('Boxplot: Exam Scores by Peer Influence')
    ax.set_xlabel('Peer Influence')
    ax.set_ylabel('Exam Score')
    return fig

# Mã hóa cột thành các giá trị số
df_cleaned['Peer_Influence_num'] = df_cleaned['Peer_Influence'].map({'Positive': 0, 'Negative': 1, 'Neutral': 2})

# Vẽ biểu đồ boxplot Exam_Score và Physical_Activity
def boxplot_Physical_Activity_and_Exam_Score():
    global df_cleaned

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(data=df_cleaned, x='Physical_Activity', y='Exam_Score', palette='tab20', ax=ax)
    ax.set_title('Boxplot: Exam Score by Physical Activity')
    ax.set_xlabel('Physical Activity')
    ax.set_ylabel('Exam Score')
    return fig

# Vẽ biểu đồ Boxplot cho Exam_Score và Learning_Disabilities
def boxplot_Learning_Disabilities_and_Exam_Score():
    global df_cleaned

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(x=df_cleaned['Learning_Disabilities'], y=df_cleaned['Exam_Score'], palette='Set2', ax=ax)
    ax.set_title('Boxplot: Exam Scores by Learning Disabilities')
    ax.set_xlabel('Learning Disabilities')
    ax.set_ylabel('Exam Score')
    return fig

# Mã hóa cột thành các giá trị số
df_cleaned['Learning_Disabilities_num'] = df_cleaned['Learning_Disabilities'].map({'No': 0, 'Yes': 1})

# Vẽ biểu đồ boxplot Exam_Score và Parental_Education_Level
def boxplot_Parental_Education_Level_and_Exam_Score():
    global df_cleaned

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(x=df_cleaned['Parental_Education_Level'], y=df_cleaned['Exam_Score'], palette='Set3', ax=ax)
    ax.set_title('Boxplot: Exam Scores by Parental Education Level')
    ax.set_xlabel('Parental Education Level')
    ax.set_ylabel('Exam Score')
    return fig

# Mã hóa cột thành các giá trị số
df_cleaned['Parental_Education_Level_num'] = df_cleaned['Parental_Education_Level'].map({'High School': 0, 'College': 1, 'Postgraduate': 2})

# Vẽ biểu đồ boxplot Exam_Score và Distance_from_Home
def boxplot_Distance_from_Home_and_Exam_Score():
    global df_cleaned

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(x=df_cleaned['Distance_from_Home'], y=df_cleaned['Exam_Score'], palette='Set3', ax=ax)
    ax.set_title('Boxplot: Exam Scores by Distance from Home')
    ax.set_xlabel('Distance from Home')
    ax.set_ylabel('Exam Score')
    return fig

# Mã hóa cột thành các giá trị số
df_cleaned['Distance_from_Home_num'] = df_cleaned['Distance_from_Home'].map({'Near': 0, 'Moderate': 1, 'Far': 2})

# Vẽ biểu đồ Boxplot cho Exam_Score và Gender
def boxplot_Gender_and_Exam_Score():
    global df_cleaned

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(x=df_cleaned['Gender'], y=df_cleaned['Exam_Score'], palette='Set2', ax=ax)
    ax.set_title('Boxplot: Exam Scores by Gender')
    ax.set_xlabel('Gender')
    ax.set_ylabel('Exam Score')
    return fig

# Mã hóa cột thành các giá trị số
df_cleaned['Gender_num'] = df_cleaned['Gender'].map({'Female': 0, 'Male': 1})

def heatmap():
    global df_cleaned

    numerical_df = df_cleaned.select_dtypes(include='number')
    corr_df = numerical_df.corr()
    fig, ax = plt.subplots(figsize=(10, 8)) 
    sns.heatmap(corr_df, annot=True, cmap='coolwarm', fmt=".2f",ax = ax)  
    plt.xticks(rotation=45, ha='right')  
    plt.title('Biểu đồ HEATMAP') 
    plt.tight_layout()
    return fig
