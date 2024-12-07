import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
from scipy.stats import ttest_ind

warnings.filterwarnings('ignore') # Tắt thông báo cảnh báo (warnings)

df_cleaned = pd.read_csv("data_source\\cleaned_data.csv") # Lấy dữ liệu chuẩn từ file đã làm sạch

# 1. VẼ BIỂU ĐỒ TẦN SUẤT VÀ CỘT CHO CÁC THUỘC TÍNH ĐƠN LẺ (HISTOGRAM và BAR)
# Histogram cho biến mục tiêu Exam_Score 
def plot_exam_score_distribution():
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(df_cleaned["Exam_Score"], bins = 45, kde=True, color='red', edgecolor = 'black', alpha = 0.5, ax=ax )
    ax.set_title('Distribution of Exam Score')
    ax.set_xlabel('Exam Score')
    ax.set_ylabel('Frequency')
    ax.set_xlim(55, 100)
    plt.grid(axis='y', alpha = 0.75)
    return fig

def exam_score_insight():
    below_64 = df_cleaned[df_cleaned['Exam_Score'] <= 64]
    above_70 = df_cleaned[df_cleaned['Exam_Score'] >= 70]
    between_65_and_69 = df_cleaned[(df_cleaned['Exam_Score'] >= 65) & (df_cleaned['Exam_Score'] <= 69)]

    percent_below_64 = (len(below_64) / len(df_cleaned)) * 100
    percent_above_70 = (len(above_70) / len(df_cleaned)) * 100
    percent_between_65_and_69 = (len(between_65_and_69) / len(df_cleaned)) * 100

    mean_score = df_cleaned['Exam_Score'].mean()
    median_score = df_cleaned['Exam_Score'].median()
    mode_score = df_cleaned['Exam_Score'].mode()[0] 
  
    insight = (
        "Thống kê mô tả về Điểm thi:\n"
        f"Phần trăm điểm số dưới 64: {percent_below_64:.2f}%\n"
        f"Phần trăm điểm số trên 70: {percent_above_70:.2f}%\n"
        f"Phần trăm điểm số trong khoảng 65 đến 69: {percent_between_65_and_69:.2f}%\n"
        f"Trung bình của Exam Score: {mean_score:.2f}\n"
        f"Trung vị của Exam Score: {median_score:.2f}\n"
        f"Đỉnh cao nhất của Exam Score: {mode_score}\n"
        f"Khoảng giá trị của Exam Score: [{df_cleaned['Exam_Score'].min():.2f},{df_cleaned['Exam_Score'].max():.2f}]\n"
    )

    return insight

# Histogram cho Hours_Studied
def plot_hours_studied_distribution():
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(df_cleaned['Hours_Studied'], bins = 45, kde=True, color='blue', edgecolor='black', alpha=0.5, ax=ax)
    ax.set_title('Distribution of Hours Studied')
    ax.set_xlabel('Hours Studied')
    ax.set_ylabel('Frequency')
    ax.set_xlim(0, 50)
    plt.grid(axis='y', alpha=0.75)
    return fig

def hours_studied_insight():
    below_10 = df_cleaned[df_cleaned['Hours_Studied'] <= 10]
    above_20 = df_cleaned[df_cleaned['Hours_Studied'] >= 20]
    between_11_and_19 = df_cleaned[(df_cleaned['Hours_Studied'] >= 11) & (df_cleaned['Hours_Studied'] <= 19)]

    percent_below_10 = (len(below_10) / len(df_cleaned)) * 100
    percent_above_20 = (len(above_20) / len(df_cleaned)) * 100
    percent_between_11_and_19 = (len(between_11_and_19) / len(df_cleaned)) * 100

    mean_score = df_cleaned['Hours_Studied'].mean()
    median_score = df_cleaned['Hours_Studied'].median()
    mode_score = df_cleaned['Hours_Studied'].mode()[0]  

    insight = (
        "Thống kê mô tả về Số giờ học mỗi tuần:\n"
        f"Phần trăm số giờ học bài dưới 10 giờ: {percent_below_10:.2f}%\n"
        f"Phần trăm số giờ học bài trên 20 giờ: {percent_above_20:.2f}%\n"
        f"Phần trăm số giờ học bài trong khoảng 11 giờ đến 19 giờ: {percent_between_11_and_19:.2f}%\n"
        f"Trung bình của Hours Studied: {mean_score:.2f}\n"
        f"Trung vị của Hours Studied: {median_score:.2f}\n"
        f"Đỉnh cao nhất của Hours Studied: {mode_score}\n"
        f"Khoảng giá trị của Hours Studied: [{df_cleaned['Hours_Studied'].min():.2f},{df_cleaned['Hours_Studied'].max():.2f}]\n"
    )
    
    return insight

# Histogram cho Attendance
def plot_attendance_distribution():
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(df_cleaned['Attendance'], bins=45, kde=True, color='violet', edgecolor='black', alpha=0.5, ax=ax)
    ax.set_title('Distribution of Attendance')
    ax.set_xlabel('Attendance')
    ax.set_ylabel('Frequency')
    ax.set_xlim(60, 100)
    plt.grid(axis='y', alpha=0.75)
    return fig

def attendance_insight():
    below_69 = df_cleaned[df_cleaned['Attendance'] <= 69]
    above_80 = df_cleaned[df_cleaned['Attendance'] >= 80]
    between_70_and_79 = df_cleaned[(df_cleaned['Attendance'] >= 70) & (df_cleaned['Attendance'] <= 79)]

    percent_below_69 = (len(below_69) / len(df_cleaned)) * 100
    percent_above_80 = (len(above_80) / len(df_cleaned)) * 100
    percent_between_70_and_79 = (len(between_70_and_79) / len(df_cleaned)) * 100

    mean_score = df_cleaned['Attendance'].mean()
    median_score = df_cleaned['Attendance'].median()
    mode_score = df_cleaned['Attendance'].mode()[0]  

    insight = (
        "Thống kê mô tả về Tỷ lệ tham gia buổi học:\n"
        f"Phần trăm tham dự dưới 69: {percent_below_69:.2f}%\n"
        f"Phần trăm tham dự trên 80: {percent_above_80:.2f}%\n"
        f"Phần trăm tham dự trong khoảng 70 đến 79: {percent_between_70_and_79:.2f}%\n"
        f"Trung bình của Attendance: {mean_score:.2f}\n"
        f"Trung vị của Attendance: {median_score:.2f}\n"
        f"Đỉnh cao nhất của Attendance: {mode_score}\n"
        f"Khoảng giá trị của Attendance: [{df_cleaned['Attendance'].min():.2f},{df_cleaned['Attendance'].max():.2f}]\n"
    )
    
    return insight

# Histogram cho Previous_Scores
def plot_previous_scores_distribution():
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(df_cleaned['Previous_Scores'], bins=80, kde=True, color='green', edgecolor='black', alpha=0.5, ax=ax)
    ax.set_title('Distribution of Previous Scores')
    ax.set_xlabel('Previous Scores')
    ax.set_ylabel('Frequency')
    ax.set_xlim(50, 100)
    plt.grid(axis='y', alpha=0.75)
    return fig

def previous_scores_insight():
    below_69 = df_cleaned[df_cleaned['Previous_Scores'] <= 69]
    above_90 = df_cleaned[df_cleaned['Previous_Scores'] >= 90]
    between_70_and_89 = df_cleaned[(df_cleaned['Previous_Scores'] >= 70) & (df_cleaned['Previous_Scores'] <= 89)]

    percent_below_69 = (len(below_69) / len(df_cleaned)) * 100
    percent_above_90 = (len(above_90) / len(df_cleaned)) * 100
    percent_between_70_and_89 = (len(between_70_and_89) / len(df_cleaned)) * 100

    mean_score = df_cleaned['Previous_Scores'].mean()
    median_score = df_cleaned['Previous_Scores'].median()
    mode_score = df_cleaned['Previous_Scores'].mode()[0]  
    insight = (
        "Thống kê mô tả về Điểm thi trước đó:\n"
        f"Phần trăm điểm dưới 69: {percent_below_69:.2f}%\n"
        f"Phần trăm điểm trên 90: {percent_above_90:.2f}%\n"
        f"Phần trăm điểm trong khoảng 70 đến 89: {percent_between_70_and_89:.2f}%\n"
        f"Trung bình của Previous Scores: {mean_score:.2f}\n"
        f"Trung vị của Previous Scores: {median_score:.2f}\n"
        f"Đỉnh cao nhất của Previous Scores: {mode_score}\n"
        f"Khoảng giá trị của Previous Scores: [{df_cleaned['Previous_Scores'].min():.2f},{df_cleaned['Previous_Scores'].max():.2f}]\n"
    )
    
    return insight

# Bar cho Parental_Involvement
def plot_parental_involvement_distribution():
    fig, ax = plt.subplots(figsize=(10, 6))
    counts = df_cleaned['Parental_Involvement'].value_counts()
    counts.plot(kind='bar', color=['red', 'orange', 'green'], edgecolor='black', alpha=0.5, ax=ax)
    ax.set_title('Distribution of Parental Involvement')
    ax.set_xlabel('Parental Involvement')
    ax.set_ylabel('Frequency')
    ax.set_xticklabels(counts.index, rotation=0)
    plt.grid(axis='y', alpha=0.75)
    return fig

def parental_involvement_insight():
    low_involvement = df_cleaned[df_cleaned['Parental_Involvement'] == 'Low']
    medium_involvement = df_cleaned[df_cleaned['Parental_Involvement'] == 'Medium']
    high_involvement = df_cleaned[df_cleaned['Parental_Involvement'] == 'High']

    percent_low = (len(low_involvement) / len(df_cleaned)) * 100
    percent_medium = (len(medium_involvement) / len(df_cleaned)) * 100
    percent_high = (len(high_involvement) / len(df_cleaned)) * 100

    insight = (
        "Thống kê mô tả về Mức độ tham gia của phụ huynh:\n"
        f"Phần trăm tham gia của phụ huynh ở mức thấp: {percent_low:.2f}%\n"
        f"Phần trăm tham gia của phụ huynh ở mức trung bình: {percent_medium:.2f}%\n"
        f"Phần trăm tham gia của phụ huynh ở mức cao: {percent_high:.2f}%\n"
    )
    
    return insight

# Bar cho Access_to_Resources
def plot_access_to_resources_distribution():
    fig, ax = plt.subplots(figsize=(10, 6))
    counts = df_cleaned['Access_to_Resources'].value_counts()
    counts.plot(kind='bar', color=['cyan', 'magenta', 'green'], edgecolor='black', alpha=0.5, ax=ax)
    ax.set_title('Distribution of Access to Resources')
    ax.set_xlabel('Access to Resources')
    ax.set_ylabel('Frequency')
    ax.set_xticklabels(counts.index, rotation=0)
    plt.grid(axis='y', alpha=0.75)
    return fig

def access_to_resources_insight():
    low_access = df_cleaned[df_cleaned['Access_to_Resources'] == 'Low']
    medium_access = df_cleaned[df_cleaned['Access_to_Resources'] == 'Medium']
    high_access = df_cleaned[df_cleaned['Access_to_Resources'] == 'High']

    percent_low = (len(low_access) / len(df_cleaned)) * 100
    percent_medium = (len(medium_access) / len(df_cleaned)) * 100
    percent_high = (len(high_access) / len(df_cleaned)) * 100

    insight = (
        "Thống kê mô tả về Mức độ truy cập tài nguyên học tập:\n"
        f"Phần trăm truy cập vào dữ liệu ở mức thấp: {percent_low:.2f}%\n"
        f"Phần trăm truy cập vào dữ liệu ở mức trung bình: {percent_medium:.2f}%\n"
        f"Phần trăm truy cập vào dữ liệu ở mức cao: {percent_high:.2f}%\n"
    )
    
    return insight

# Bar cho Extracurricular_Activities
def plot_extracurricular_activities_distribution():
    fig, ax = plt.subplots(figsize=(10,6))
    counts = df_cleaned['Extracurricular_Activities'].value_counts()
    counts.plot(kind='bar', color=['red', 'green'], edgecolor='black', alpha=0.5, ax=ax)
    ax.set_title('Distribution of Extracurricular Activities')
    ax.set_xlabel('Extracurricular Activities')
    ax.set_ylabel('Frequency')
    ax.set_xticklabels(counts.index, rotation=0)
    plt.grid(axis='y', alpha=0.75)
    return fig

def extracurricular_activities_insight():
    yes_activitiess = df_cleaned[df_cleaned['Extracurricular_Activities'] == 'Yes']
    no_activitiess = df_cleaned[df_cleaned['Extracurricular_Activities'] == 'No']

    percent_yes = (len(yes_activitiess) / len(df_cleaned)) * 100
    percent_no = (len(no_activitiess) / len(df_cleaned)) * 100

    insight = (
        "Thống kê mô tả về Hoạt động ngoại khoá:\n"
        f"Phần trăm có hoạt động ngoại khóa: {percent_yes:.2f}%\n"
        f"Phần trăm không hoạt động ngoại khóa: {percent_no:.2f}%\n"
    )
    
    return insight

# Bar cho Sleep_Hours
def plot_sleep_hours_distribution():
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

def sleep_hours_insight():
    # Đếm số lần xuất hiện của từng giá trị trong Sleep_Hour
    sleep_hour_counts = df_cleaned['Sleep_Hours'].value_counts()
        
    # Tính phần trăm
    sleep_hour_percentage = (sleep_hour_counts / len(df_cleaned)) * 100

    insight = (
        "Thống kê mô tả về Số giờ ngủ mỗi đêm:\n"
        f"Phần trăm số giờ ngủ của từng giờ:\n"
    )
    for hour, percent in sleep_hour_percentage.items():
        insight += (f"{hour} giờ: {percent:.2f}%\n")
    
    return insight

# Bar cho Motivation_Level
def plot_motivation_level_distribution():
    fig, ax = plt.subplots(figsize=(10, 6))
    counts = df_cleaned['Motivation_Level'].value_counts()
    counts.plot(kind='bar', color=['yellow', 'green', 'red'], edgecolor='black', alpha=0.5, ax=ax)
    ax.set_title('Distribution of Motivation Level')
    ax.set_xlabel('Motivation Level')
    ax.set_ylabel('Frequency')
    ax.set_xticklabels(counts.index, rotation=0)
    plt.grid(axis='y', alpha=0.75)
    return fig

def motivation_level_insight():
    low_level= df_cleaned[df_cleaned['Motivation_Level'] == 'Low']
    medium_level = df_cleaned[df_cleaned['Motivation_Level'] == 'Medium']
    high_level = df_cleaned[df_cleaned['Motivation_Level'] == 'High']

    percent_low = (len(low_level) / len(df_cleaned)) * 100
    percent_medium = (len(medium_level) / len(df_cleaned)) * 100
    percent_high = (len(high_level) / len(df_cleaned)) * 100

    insight = (
        "Thống kê mô tả về Mức độ động lực học tập:\n"
        f"Phần trăm động lực ở mức thấp: {percent_low:.2f}%\n"
        f"Phần trăm động lực ở mức trung bình: {percent_medium:.2f}%\n"
        f"Phần trăm động lực ở mức cao: {percent_high:.2f}%\n"
    )
    
    return insight

# Bar cho Internet_Access
def plot_internet_access_distribution():
    fig, ax = plt.subplots(figsize=(10, 6)) 
    counts = df_cleaned['Internet_Access'].value_counts()
    counts.plot(kind='bar', color=['purple', 'red'], edgecolor='black', alpha=0.5, ax=ax)
    ax.set_title('Distribution of Internet Access')
    ax.set_xlabel('Internet Access')
    ax.set_ylabel('Frequency')
    ax.set_xticklabels(counts.index, rotation=0)
    plt.grid(axis='y', alpha=0.75)
    return fig

def internet_access_insight():
    yes_access = df_cleaned[df_cleaned['Internet_Access'] == 'Yes']
    no_access = df_cleaned[df_cleaned['Internet_Access'] == 'No']

    percent_yes = (len(yes_access) / len(df_cleaned)) * 100
    percent_no = (len(no_access) / len(df_cleaned)) * 100

    insight = (
        "Thống kê mô tả về Khả năng truy cập Internet:\n"
        f"Phần trăm có truy cập Internet: {percent_yes:.2f}%\n"
        f"Phần trăm không truy cập Internet: {percent_no:.2f}%\n"
    )

    return insight

# Bar cho Tutoring_Sessions 
def plot_tutoring_sessions_distribution():
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

def tutoring_sessions_insight():
    tutoring_sessions_counts = df_cleaned['Tutoring_Sessions'].value_counts()
    tutoring_sessions_percentage = (tutoring_sessions_counts / len(df_cleaned)) * 100
    insight = (
        "Thống kê mô tả về Số buổi dạy kèm trong tháng:\n"
        "Phần trăm của từng số buổi dạy kèm:\n"
    )
    for session, percent in tutoring_sessions_percentage.items():
        insight += f"{session} buổi: {percent:.2f}%\n"

    return insight

# Bar cho Family_Income
def plot_family_income_distribution():
    fig, ax = plt.subplots(figsize=(10, 6))
    counts = df_cleaned['Family_Income'].value_counts()
    counts.plot(kind='bar', color=['purple', 'yellow', 'pink'], edgecolor='black', alpha=0.5, ax=ax)
    ax.set_title('Distribution of Family Income')
    ax.set_xlabel('Family Income')
    ax.set_ylabel('Frequency')
    ax.set_xticklabels(counts.index, rotation=0)
    plt.grid(axis='y', alpha=0.75)
    return fig

def family_income_insight():
    low_income= df_cleaned[df_cleaned['Family_Income'] == 'Low']
    medium_income = df_cleaned[df_cleaned['Family_Income'] == 'Medium']
    high_income = df_cleaned[df_cleaned['Family_Income'] == 'High']

    percent_low = (len(low_income) / len(df_cleaned)) * 100
    percent_medium = (len(medium_income) / len(df_cleaned)) * 100
    percent_high = (len(high_income) / len(df_cleaned)) * 100

    insight = (
        "Thống kê mô tả về Mức thu nhập gia đình:\n"
        f"Phần trăm thu nhập gia đình ở mức thấp: {percent_low:.2f}%\n"
        f"Phần trăm thu nhập gia đình ở mức trung bình: {percent_medium:.2f}%\n"
        f"Phần trăm thu nhập gia đình ở mức cao: {percent_high:.2f}%\n"    
    )

    return insight

# Bar cho Teacher_Quality
def plot_teacher_quality_distribution():
    fig, ax = plt.subplots(figsize=(10, 6))
    counts = df_cleaned['Teacher_Quality'].value_counts()
    counts.plot(kind='bar', color=['fuchsia', 'blue', 'orange'], edgecolor='black', alpha=0.5, ax=ax)
    ax.set_title('Distribution of Teacher Quality')
    ax.set_xlabel('Teacher Quality')
    ax.set_ylabel('Frequency')
    ax.set_xticklabels(counts.index, rotation=0)
    plt.grid(axis='y', alpha=0.75)
    return fig

def teacher_quality_insight():
    low_quality= df_cleaned[df_cleaned['Teacher_Quality'] == 'Low']
    medium_quality = df_cleaned[df_cleaned['Teacher_Quality'] == 'Medium']
    high_quality = df_cleaned[df_cleaned['Teacher_Quality'] == 'High']

    percent_low = (len(low_quality) / len(df_cleaned)) * 100
    percent_medium = (len(medium_quality) / len(df_cleaned)) * 100
    percent_high = (len(high_quality) / len(df_cleaned)) * 100

    insight = (
        "Thống kê mô tả về Chất lượng giảng viên:\n"
        f"Phần trăm chất lượng giảng viên ở mức thấp: {percent_low:.2f}%\n"
        f"Phần trăm chất lượng giảng viên ở mức trung bình: {percent_medium:.2f}%\n"
        f"Phần trăm chất lượng giảng viên ở mức cao: {percent_high:.2f}%\n"    
    )

    return insight

# Bar cho School_Type
def plot_school_type_distribution():
    fig, ax = plt.subplots(figsize=(10, 6))
    counts = df_cleaned['School_Type'].value_counts()
    counts.plot(kind='bar', color=['green', 'violet'], edgecolor='black', alpha=0.5, ax=ax)
    ax.set_title('Distribution of School Type')
    ax.set_xlabel('School Type')
    ax.set_ylabel('Frequency')
    ax.set_xticklabels(counts.index, rotation=0)
    plt.grid(axis='y', alpha=0.75)
    return fig

def school_type_insight():
    public_type = df_cleaned[df_cleaned['School_Type'] == 'Public']
    private_type = df_cleaned[df_cleaned['School_Type'] == 'Private']

    public_sch = (len(public_type) / len(df_cleaned)) * 100
    private_sch = (len(private_type) / len(df_cleaned)) * 100

    insight = (
        "Thống kê mô tả về Loại trường theo học:\n"
        f"Phần trăm học ở trường công lập: {public_sch:.2f}%\n"
        f"Phần trăm học ở trường tư thục: {private_sch:.2f}%\n"
    )

    return insight

# Bar cho Peer_Influence
def plot_peer_influence_distribution():
    fig, ax = plt.subplots(figsize=(10,6))
    counts = df_cleaned['Peer_Influence'].value_counts()
    counts.plot(kind='bar', color=['violet', 'lime', 'maroon'], edgecolor='black', alpha=0.5, ax=ax)
    ax.set_title('Distribution of Peer Influence')
    ax.set_xlabel('Peer Influence')
    ax.set_ylabel('Frequency')
    ax.set_xticklabels(counts.index, rotation=0)
    return fig

def peer_influence_insight():
    po_influ= df_cleaned[df_cleaned['Peer_Influence'] == 'Positive']
    ne_influ = df_cleaned[df_cleaned['Peer_Influence'] == 'Negative']
    neu_influ = df_cleaned[df_cleaned['Peer_Influence'] == 'Neutral']

    percent_po = (len(po_influ) / len(df_cleaned)) * 100
    percent_ne = (len(ne_influ) / len(df_cleaned)) * 100
    percent_neu = (len(neu_influ) / len(df_cleaned)) * 100

    insight = (
        "Thống kê mô tả về Ảnh hưởng từ bạn bè:\n"
        f"Phần trăm ảnh hưởng tích cực: {percent_po:.2f}%\n"
        f"Phần trăm ảnh hưởng tiêu cực: {percent_ne:.2f}%\n"
        f"Phần trăm ảnh hưởng trung lập: {percent_neu:.2f}%\n"
    )

    return insight

# Bar cho Physical_Activity
def plot_physical_activity_distribution():
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

def physical_activity_insight():
    # Đếm số lần xuất hiện của từng giá trị trong Physical_Activity
    physical_activity_counts = df_cleaned['Physical_Activity'].value_counts()
        
    # Tính phần trăm
    physical_activity_percentage = (physical_activity_counts / len(df_cleaned)) * 100
        
    # In kết quả
    insight = (
        "Thống kê mô tả về Số lần hoạt động thể chất mỗi tuần:\n"
        "Phần trăm của từng số giờ hoạt động thể chất:\n"
    )
    for activity, percent in physical_activity_percentage.items():
        insight += f"{activity} giờ: {percent:.2f}%\n"

    return insight

# Bar cho Learning_Disabilities
def plot_learning_disabilities_distribution():
    fig, ax = plt.subplots(figsize=(10,6))
    counts = df_cleaned['Learning_Disabilities'].value_counts()
    counts.plot(kind='bar', color=['coral', 'olive'], edgecolor='black', alpha=0.5, ax=ax)
    ax.set_title('Distribution of Learning Disabilities')
    ax.set_xlabel('Learning Disabilities')
    ax.set_ylabel('Frequency')
    ax.set_xticklabels(counts.index, rotation=0)
    plt.grid(axis='y', alpha=0.75)
    return fig

def learning_disabilities_insight():
    yes_disa = df_cleaned[df_cleaned['Learning_Disabilities'] == 'Yes']
    no_disa = df_cleaned[df_cleaned['Learning_Disabilities'] == 'No']

    percent_yes = (len(yes_disa) / len(df_cleaned)) * 100
    percent_no = (len(no_disa) / len(df_cleaned)) * 100

    insight = (
        "Thống kê mô tả về Khuyết tật học tập:\n"
        f"Phần trăm bị khuyết tậthọc tập: {percent_yes:.2f}%\n"
        f"Phần trăm không bị khuyết tật học tập: {percent_no:.2f}%\n"
    )

    return insight

# Bar cho Parental_Education_Level
def plot_parental_education_level_distribution():
    fig, ax = plt.subplots(figsize=(10,6))
    counts = df_cleaned['Parental_Education_Level'].value_counts()
    counts.plot(kind='bar', color=['green', 'blue', 'orange'], edgecolor='black', alpha=0.5, ax=ax)
    ax.set_title('Distribution of Parental Education Level')
    ax.set_xlabel('Parental Education Level')
    ax.set_ylabel('Frequency')
    ax.set_xticklabels(counts.index, rotation=0)
    plt.grid(axis='y', alpha=0.75)
    return fig

def parental_education_insight():
    hs = df_cleaned[df_cleaned['Parental_Education_Level'] == 'High School']
    co = df_cleaned[df_cleaned['Parental_Education_Level'] == 'College']
    po = df_cleaned[df_cleaned['Parental_Education_Level'] == 'Postgraduate']

    percent_hs = (len(hs) / len(df_cleaned)) * 100
    percent_co = (len(co) / len(df_cleaned)) * 100
    percent_po = (len(po) / len(df_cleaned)) * 100

    insight = (
        "Thống kê mô tả về Trình độ học vấn của phụ huynh:\n"
        f"Phần trăm ba mẹ học trung học: {percent_hs:.2f}%\n"
        f"Phần trăm ba mẹ học cao đẳng: {percent_co:.2f}%\n"
        f"Phần trăm ba mẹ học tiếp sau đại học: {percent_po:.2f}%\n"
    )

    return insight

# Bar cho Distance_from_Home
def plot_distance_from_home_distribution():
    fig, ax = plt.subplots(figsize=(10,6))  
    counts = df_cleaned['Distance_from_Home'].value_counts()
    counts.plot(kind='bar', color=['coral', 'olive', 'lime'], edgecolor='black', alpha=0.5, ax=ax)
    ax.set_title('Distribution of Distance from Home')
    ax.set_xlabel('Distance from Home')
    ax.set_ylabel('Frequency')
    ax.set_xticklabels(counts.index, rotation=0)
    plt.grid(axis='y', alpha=0.75)
    return fig

def distance_from_home_insight():
    ne = df_cleaned[df_cleaned['Distance_from_Home'] == 'Near']
    fa = df_cleaned[df_cleaned['Distance_from_Home'] == 'Far']
    mo = df_cleaned[df_cleaned['Distance_from_Home'] == 'Moderate']

    percent_ne = (len(ne) / len(df_cleaned)) * 100
    percent_fa = (len(fa) / len(df_cleaned)) * 100
    percent_mo = (len(mo) / len(df_cleaned)) * 100

    insight = (
        "Thống kê mô tả về Khoảng cách từ nhà đến trường:\n"
        f"Phần trăm nhà ở gần trường: {percent_ne:.2f}%\n"
        f"Phần trăm nhà ở xa trường: {percent_fa:.2f}%\n"
        f"Phần trăm nhà cách trường không xa: {percent_mo:.2f}%\n"
    )

    return insight

# Bar cho Gender
def plot_gender_distribution():
    fig, ax = plt.subplots(figsize=(10,6))
    counts = df_cleaned['Gender'].value_counts()
    counts.plot(kind='bar', color=['azure', 'cyan'], edgecolor='black', alpha=0.5, ax=ax)
    ax.set_title('Distribution of Gender')
    ax.set_xlabel('Gender')
    ax.set_ylabel('Frequency')
    ax.set_xticklabels(counts.index, rotation=0)
    plt.grid(axis='y', alpha=0.75)
    return fig

def gender_insight():
    ma = df_cleaned[df_cleaned['Gender'] == 'Male']
    fe= df_cleaned[df_cleaned['Gender'] == 'Female']

    percent_ma = (len(ma) / len(df_cleaned)) * 100
    percent_fe = (len(fe) / len(df_cleaned)) * 100

    insight = (
        "Thống kê mô tả về Giới tính:\n"
        f"Phần trăm nữ: {percent_fe:.2f}%\n"
        f"Phần trăm nam: {percent_ma:.2f}%\n"
    )

    return insight

# 2. VẼ BIỂU ĐỒ BIỂU DIỄN QUAN HỆ PHÂN TÁN (SỐ) VÀ BIỂU ĐỒ HỘP (PHÂN LOẠI) VỚI BIẾN MỤC TIÊU EXAM_SCORE
# Vẽ biểu đồ phân tán Hours Studied và Exam Score
def scatterplot_Hours_Studied_and_Exam_Score():
    fig, ax = plt.subplots(figsize=(10,6))
    sns.scatterplot(x=df_cleaned['Hours_Studied'], y=df_cleaned['Exam_Score'], color='green', alpha=0.7, ax=ax)
    ax.set_title('Scatter Plot: Hours Studied vs Exam Score')
    ax.set_xlabel('Hours Studied')
    ax.set_ylabel('Exam Score')
    plt.grid(True)
    return fig

# Vẽ biểu đồ phân tán Attendance và Exam Score
def scatterplot_Attendance_and_Exam_Score():
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(x=df_cleaned['Attendance'], y=df_cleaned['Exam_Score'], color='gray', alpha=0.7, ax=ax)
    ax.set_title('Scatter Plot: Attendance vs Exam Score')
    ax.set_xlabel('Attendance')
    ax.set_ylabel('Exam Score')
    plt.grid(True)
    return fig

# Vẽ biểu đồ phân tán Previous Scores và Exam Score
def scatterplot_Previous_Scores_and_Exam_Score():
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(x=df_cleaned['Previous_Scores'], y=df_cleaned['Exam_Score'], color='salmon', alpha=0.7, ax=ax)
    ax.set_title('Scatter Plot: Previous Scores vs Exam Score')
    ax.set_xlabel('Previous Scores')
    ax.set_ylabel('Exam Score')
    plt.grid(True)
    return fig

# Xây dựng sơ đồ phân tán dựa trên các đặc điểm số (tính đến các hoạt động ngoại khóa):
def scatterplot_Numcol_and_Exam_Score_with_Extracurricular_Activities():
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
    
    return fig

def compare_exam_scores_by_activity():
    """
    Thực hiện kiểm định t-test để so sánh điểm thi giữa hai nhóm sinh viên: 
    nhóm có tham gia hoạt động ngoại khóa và nhóm không tham gia.
    """
    # Chia thành 2 nhóm: tham gia và không tham gia
    group_yes = df_cleaned[df_cleaned['Extracurricular_Activities'] == 'Yes']['Exam_Score']
    group_no = df_cleaned[df_cleaned['Extracurricular_Activities'] == 'No']['Exam_Score']

    # Kiểm định t-test
    t_stat, p_value = ttest_ind(group_yes, group_no)

    insight = ("")
   # Kiểm tra p-value và in kết quả
    if p_value < 0.05:
        insight += f"T-statistic: {t_stat}, P-value: {p_value}\n"
        insight += "Kết luận: Có sự khác biệt có ý nghĩa thống kê giữa hai nhóm.\n"
    
    # Kiểm tra dấu của T-statistic để xác định nhóm nào có điểm cao hơn
        if t_stat > 0:
            insight += "Nhóm có hoạt động ngoại khóa có điểm thi cao hơn nhóm không có hoạt động ngoại khóa.\n"
        else:
            insight += ("Nhóm không có hoạt động ngoại khóa có điểm thi cao hơn nhóm có hoạt động ngoại khóa.\n")
    else:
        insight += (f"T-statistic: {t_stat}, P-value: {p_value}\n")
        insight += ("Kết luận: Không có sự khác biệt có ý nghĩa thống kê giữa hai nhóm.\n")

    return insight

# Xây dựng sơ đồ phân tán dựa trên các đặc điểm số (tính đến giới tính):
def scatterplot_Numcol_and_Exam_Score_with_Gender():
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

    return fig

def compare_exam_scores_by_gender():
    """
    Thực hiện kiểm định t-test để so sánh điểm thi giữa hai nhóm sinh viên nam và nữ.

    """
    # Chia thành 2 nhóm: nam và nữ
    group_male = df_cleaned[df_cleaned['Gender'] == 'Male']['Exam_Score']
    group_female = df_cleaned[df_cleaned['Gender'] == 'Female']['Exam_Score']

    # Kiểm định t-test
    t_stat, p_value = ttest_ind(group_male, group_female)

    insight = ("")
    # Kiểm tra p-value và in kết quả
    if p_value < 0.05:
        insight += (f"T-statistic: {t_stat}, P-value: {p_value}\n")
        insight += ("Kết luận: Có sự khác biệt có ý nghĩa thống kê giữa hai nhóm.\n")
    
    # Kiểm tra dấu của T-statistic để xác định nhóm nào có điểm cao hơn
        if t_stat > 0:
            insight += ("Nhóm sinh viên nam có điểm thi cao hơn nhóm sinh viên nữ.\n")
        else:
            insight += ("Nhóm sinh viên nữ có điểm thi cao hơn nhóm sinh viên nam.\n")
    else:
        insight += (f"T-statistic: {t_stat}, P-value: {p_value}\n")
        insight += ("Kết luận: Không có sự khác biệt có ý nghĩa thống kê giữa hai nhóm.\n")

    return insight

# Xây dựng sơ đồ phân tán dựa trên các đặc điểm số (tính đến việc truy cập Internet):
def scatterplot_Numcol_and_Exam_Score_with_Internet_Access():
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
    return fig

def compare_exam_scores_by_internet_access():
    """
    Thực hiện kiểm định t-test để so sánh điểm thi giữa hai nhóm sinh viên 
    có truy cập Internet và không truy cập Internet.
    """
    # Chia thành 2 nhóm: có truy cập và không truy cập Internet
    group_yes = df_cleaned[df_cleaned['Internet_Access'] == 'Yes']['Exam_Score']
    group_no = df_cleaned[df_cleaned['Internet_Access'] == 'No']['Exam_Score']

    # Kiểm định t-test
    t_stat, p_value = ttest_ind(group_yes, group_no)

    insight = ("")
    # Kiểm tra p-value và in kết quả
    if p_value < 0.05:
        insight += (f"T-statistic: {t_stat}, P-value: {p_value}\n")
        insight += ("Kết luận: Có sự khác biệt có ý nghĩa thống kê giữa hai nhóm.\n")
    
    # Kiểm tra dấu của T-statistic để xác định nhóm nào có điểm cao hơn
        if t_stat > 0:
            insight += ("Nhóm sinh viên được truy cập Internet có điểm thi cao hơn Nhóm sinh viên không được truy cập Internet.\n")
        else:
            insight += ("Nhóm sinh viên không được truy cập Internet có điểm thi cao hơn Nhóm sinh viên được truy cập Internet.\n")
    else:
        insight += (f"T-statistic: {t_stat}, P-value: {p_value}\n")
        insight += ("Kết luận: Không có sự khác biệt có ý nghĩa thống kê giữa hai nhóm.\n")

    return insight

# Xây dựng sơ đồ phân tán dựa trên các đặc điểm số (tính đến Khuyết tật học tập):
def scatterplot_Numcol_and_Exam_Score_with_Learning_Disabilities():
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
    return fig

def compare_exam_scores_by_learning_disabilities():
    """
    So sánh điểm thi giữa học sinh có khuyết tật học tập và không có khuyết tật học tập 
    bằng cách sử dụng kiểm định t-test độc lập và in kết quả.
    """
    # Chia thành 2 nhóm: có khuyết tật học tập và không có khuyết tật học tập
    group_yes = df_cleaned[df_cleaned['Learning_Disabilities'] == 'Yes']['Exam_Score']
    group_no = df_cleaned[df_cleaned['Learning_Disabilities'] == 'No']['Exam_Score']

    # Kiểm định t-test độc lập
    t_stat, p_value = ttest_ind(group_yes, group_no)

    insight = ("")
    # Kiểm tra p-value và in kết quả
    if p_value < 0.05:
        insight += (f"T-statistic: {t_stat}, P-value: {p_value}\n")
        insight += ("Kết luận: Có sự khác biệt có ý nghĩa thống kê giữa hai nhóm.\n")
    
    # Kiểm tra dấu của T-statistic để xác định nhóm nào có điểm cao hơn
        if t_stat > 0:
            insight += ("Nhóm sinh viên khuyết tật có điểm thi cao hơn Nhóm sinh viên không khuyết tật.\n")
        else:
            insight += ("Nhóm sinh viên không khuyết tật có điểm thi cao hơn Nhóm sinh viên khuyết tật.\n")
    else:
        insight += (f"T-statistic: {t_stat}, P-value: {p_value}\n")
        insight += ("Kết luận: Không có sự khác biệt có ý nghĩa thống kê giữa hai nhóm.\n")

    return insight

# Vẽ biểu đồ boxplot Exam_Score và Parental Involvement
def boxplot_Parental_Involvement_and_Exam_Score():
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(x=df_cleaned['Parental_Involvement'], y=df_cleaned['Exam_Score'], palette='Set2', ax=ax)
    ax.set_title('Boxplot: Exam Scores by Parental Involvement')
    ax.set_xlabel('Parental Involvement')
    ax.set_ylabel('Exam Score')
    return fig

# Vẽ biểu đồ boxplot Exam_Score và Access_to_Resources
def boxplot_Access_to_Resources_and_Exam_Score():
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(x=df_cleaned['Access_to_Resources'], y=df_cleaned['Exam_Score'], palette='Set2', ax=ax)
    ax.set_title('Boxplot: Exam Scores by Access to Resources')
    ax.set_xlabel('Access to Resources')
    ax.set_ylabel('Exam Score')
    return fig

# Vẽ biểu đồ boxplot Exam_Score và Extracurricular_Activities
def boxplot_Extracurricular_Activities_and_Exam_Score():
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(data=df_cleaned, x='Extracurricular_Activities', y='Exam_Score', palette=['pink', 'blue'], ax=ax)
    ax.set_title('Boxplot: Exam Score by Extracurricular Activities')
    ax.set_xlabel('Extracurricular Activities')
    ax.set_ylabel('Exam Score')
    return fig

# Vẽ biểu đồ boxplot Exam_Score và Sleep_Hours
def boxplot_Sleep_Hours_and_Exam_Score():
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(data=df_cleaned, x='Sleep_Hours', y='Exam_Score', palette='Paired', ax=ax)
    ax.set_title('Boxplot: Exam Score by Sleep Hours')
    ax.set_xlabel('Sleep Hours')
    ax.set_ylabel('Exam Score')
    return fig

# Vẽ biểu đồ boxplot Exam_Score và Motivation_Level
def boxplot_Motivation_Level_and_Exam_Score():
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(x=df_cleaned['Motivation_Level'], y=df_cleaned['Exam_Score'], palette='Set1', ax=ax)
    ax.set_title('Boxplot: Exam Scores by Motivation Level')
    ax.set_xlabel('Motivation Level')
    ax.set_ylabel('Exam Score')
    return fig

# Vẽ biểu đồ boxplot Exam_Score và Internet_Access
def boxplot_Internet_Access_and_Exam_Score():
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(data=df_cleaned, x='Internet_Access', y='Exam_Score', palette=['red', 'pink'], ax=ax)
    ax.set_title('Boxplot: Exam Score by Internet Access')
    ax.set_xlabel('Internet Access')
    ax.set_ylabel('Exam Score')
    return fig

# Vẽ biểu đồ boxplot Exam_Score và Tutoring_Sessions
def boxplot_Tutoring_Sessions_and_Exam_Score():
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(data=df_cleaned, x='Tutoring_Sessions', y='Exam_Score', palette='Set3', ax=ax)
    ax.set_title('Boxplot: Exam Score by Tutoring Sessions')
    ax.set_xlabel('Tutoring Sessions')
    ax.set_ylabel('Exam Score')
    return fig

# Vẽ biểu đồ boxplot Exam_Score và Family_Income
def boxplot_Family_Income_and_Exam_Score():
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(x=df_cleaned['Family_Income'], y=df_cleaned['Exam_Score'], palette='Set2', ax=ax)
    ax.set_title('Boxplot: Exam Scores by Family Income')
    ax.set_xlabel('Family Income')
    ax.set_ylabel('Exam Score')
    return fig

# Vẽ biểu đồ boxplot Exam_Score và Teacher_Quality
def boxplot_Teacher_Quality_and_Exam_Score():
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(x=df_cleaned['Teacher_Quality'], y=df_cleaned['Exam_Score'], palette='Set1', ax=ax)
    ax.set_title('Boxplot: Exam Scores by Teacher Quality')
    ax.set_xlabel('Teacher Quality')
    ax.set_ylabel('Exam Score')
    return fig

# Vẽ biểu đồ Boxplot cho Exam_Score và School_Type
def boxplot_School_Type_and_Exam_Score():
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(x=df_cleaned['School_Type'], y=df_cleaned['Exam_Score'], palette='Set2', ax=ax)
    ax.set_title('Boxplot: Exam Scores by School Type')
    ax.set_xlabel('School Type')
    ax.set_ylabel('Exam Score')
    return fig

# Vẽ biểu đồ boxplot Exam_Score và Peer_Influence
def boxplot_Peer_Influence_and_Exam_Score():
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(x=df_cleaned['Peer_Influence'], y=df_cleaned['Exam_Score'], palette='Set3', ax=ax)
    ax.set_title('Boxplot: Exam Scores by Peer Influence')
    ax.set_xlabel('Peer Influence')
    ax.set_ylabel('Exam Score')
    return fig

# Vẽ biểu đồ boxplot Exam_Score và Physical_Activity
def boxplot_Physical_Activity_and_Exam_Score():
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(data=df_cleaned, x='Physical_Activity', y='Exam_Score', palette='tab20', ax=ax)
    ax.set_title('Boxplot: Exam Score by Physical Activity')
    ax.set_xlabel('Physical Activity')
    ax.set_ylabel('Exam Score')
    return fig

# Vẽ biểu đồ Boxplot cho Exam_Score và Learning_Disabilities
def boxplot_Learning_Disabilities_and_Exam_Score():
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(x=df_cleaned['Learning_Disabilities'], y=df_cleaned['Exam_Score'], palette='Set2', ax=ax)
    ax.set_title('Boxplot: Exam Scores by Learning Disabilities')
    ax.set_xlabel('Learning Disabilities')
    ax.set_ylabel('Exam Score')
    return fig

# Vẽ biểu đồ boxplot Exam_Score và Parental_Education_Level
def boxplot_Parental_Education_Level_and_Exam_Score():
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(x=df_cleaned['Parental_Education_Level'], y=df_cleaned['Exam_Score'], palette='Set3', ax=ax)
    ax.set_title('Boxplot: Exam Scores by Parental Education Level')
    ax.set_xlabel('Parental Education Level')
    ax.set_ylabel('Exam Score')
    return fig

# Vẽ biểu đồ boxplot Exam_Score và Distance_from_Home
def boxplot_Distance_from_Home_and_Exam_Score():
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(x=df_cleaned['Distance_from_Home'], y=df_cleaned['Exam_Score'], palette='Set3', ax=ax)
    ax.set_title('Boxplot: Exam Scores by Distance from Home')
    ax.set_xlabel('Distance from Home')
    ax.set_ylabel('Exam Score')
    return fig

# Vẽ biểu đồ Boxplot cho Exam_Score và Gender
def boxplot_Gender_and_Exam_Score():
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(x=df_cleaned['Gender'], y=df_cleaned['Exam_Score'], palette='Set2', ax=ax)
    ax.set_title('Boxplot: Exam Scores by Gender')
    ax.set_xlabel('Gender')
    ax.set_ylabel('Exam Score')
    return fig

def heatmap():
    df_cleaned['Parental_Involvement_num'] = df_cleaned['Parental_Involvement'].map({'Low': 0, 'Medium': 1, 'High': 2})
    df_cleaned['Access_to_Resources_num'] = df_cleaned['Access_to_Resources'].map({'Low': 0, 'Medium': 1, 'High': 2})
    df_cleaned['Extracurricular_Activities_num'] = df_cleaned['Extracurricular_Activities'].map({'Yes': 1, 'No': 0})
    df_cleaned['Motivation_Level_num'] = df_cleaned['Motivation_Level'].map({'Low': 0, 'Medium': 1, 'High': 2})
    df_cleaned['Internet_Access_num'] = df_cleaned['Internet_Access'].map({'Yes': 1, 'No': 0})
    df_cleaned['Family_Income_num'] = df_cleaned['Family_Income'].map({'Low': 0, 'Medium': 1, 'High': 2})
    df_cleaned['Teacher_Quality_num'] = df_cleaned['Teacher_Quality'].map({'Low': 0, 'Medium': 1, 'High': 2})
    df_cleaned['School_Type_num'] = df_cleaned['School_Type'].map({'Public': 0, 'Private': 1})
    df_cleaned['Learning_Disabilities_num'] = df_cleaned['Learning_Disabilities'].map({'No': 0, 'Yes': 1})
    df_cleaned['Parental_Education_Level_num'] = df_cleaned['Parental_Education_Level'].map({'High School': 0, 'College': 1, 'Postgraduate': 2})
    df_cleaned['Distance_from_Home_num'] = df_cleaned['Distance_from_Home'].map({'Near': 0, 'Moderate': 1, 'Far': 2})
    df_cleaned['Gender_num'] = df_cleaned['Gender'].map({'Female': 0, 'Male': 1})

    numerical_df = df_cleaned.select_dtypes(include='number')
    corr_df = numerical_df.corr()
    fig, ax = plt.subplots(figsize=(9, 7)) 
    sns.heatmap(corr_df, annot=True, cmap='coolwarm', fmt=".2f",ax = ax)  
    plt.xticks(rotation=45, ha='right')  
    plt.title('Biểu đồ HEATMAP') 
    plt.tight_layout()
    return fig