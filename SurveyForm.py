import tkinter as tk
from tkinter import ttk, messagebox
import csv

def makecenter(root):
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

def save_to_csv(data):
    file_name = "data_source\\cleaned_data.csv"
    try:
        # Ghi dữ liệu vào tệp CSV
        with open(file_name, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=data.keys())
            
            # Kiểm tra tệp có trống không
            file_is_empty = file.tell() == 0
            if file_is_empty:
                writer.writeheader()  # Ghi tiêu đề nếu tệp trống
            
            writer.writerow(data)  # Ghi dữ liệu mới
            messagebox.showinfo("Thành công", "Dữ liệu đã được lưu vào tệp CSV.")

    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể ghi dữ liệu vào tệp CSV: {str(e)}")

def validate_data():
    try:
        # Lấy dữ liệu từ các trường
        hours_studied = num1_entry.get()
        attendance = num2_entry.get()
        parental_involvement = num3_combobox.get()
        access_to_resources = num4_combobox.get()
        extracurricular_activities = num5_combobox.get()
        sleep_hours = num6_entry.get()
        previous_scores = num7_entry.get()
        motivation_level = num8_combobox.get()
        internet_access = num9_combobox.get()
        tutoring_sessions = num10_entry.get()
        family_income = num11_combobox.get()
        teacher_quality = num12_combobox.get()
        school_type = num13_combobox.get()
        peer_influence = num14_combobox.get()
        physical_activity_hours = num15_entry.get()
        learning_disabilities = num16_combobox.get()
        parental_education_level = num17_combobox.get()
        distance_from_home = num18_combobox.get()
        gender = num19_combobox.get()
        exam_score = num20_entry.get()

        # Kiểm tra dữ liệu rỗng
        if not hours_studied or not attendance or not sleep_hours or not previous_scores or not tutoring_sessions or not physical_activity_hours or not exam_score:
            messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin các trường bắt buộc.")
            return False

        # Kiểm tra kiểu dữ liệu
        if not hours_studied.isdigit():
            messagebox.showerror("Giá trị không hợp lệ", "Số giờ học phải là số thực.")
            return False
        if not (0 <= float(hours_studied) <= 168):
            messagebox.showerror("Giá trị không hợp lệ", "Số giờ học phải nằm trong khoảng 0-168.")
            return False
        if not attendance.isdigit():
            messagebox.showerror("Giá trị không hợp lệ", "Tỷ lệ tham gia phải là số thực.")
            return False
        if not (0 <= float(attendance) <= 100):
            messagebox.showerror("Giá trị không hợp lệ", "Tỷ lệ tham gia phải nằm trong khoảng 0-100.")
            return False
        if not sleep_hours.isdigit():
            messagebox.showerror("Giá trị không hợp lệ", "Số giờ ngủ phải là số thực.")
            return False
        if not (0 <= float(sleep_hours) <= 24) :
            messagebox.showerror("Giá trị không hợp lệ", "Số giờ ngủ phải là nằm trong khoảng 0-24.")
            return False
        if not previous_scores.isdigit():
            messagebox.showerror("Giá trị không hợp lệ", "Điểm số trước đó phải là số thực.")
            return False
        if not (0 <= float(previous_scores) <= 100):
            messagebox.showerror("Giá trị không hợp lệ", "Điểm số trước đó phải nằm trong khoảng 0-100.")
            return False
        if not tutoring_sessions.isdigit():
            messagebox.showerror("Giá trị không hợp lệ", "Số buổi học thêm phải là số nguyên.")
            return False
        if not (0 <= int(tutoring_sessions) <= 10):
            messagebox.showerror("Giá trị không hợp lệ", "Số buổi học thêm phải là nằm trong khoảng 0-10.")
            return False
        if not physical_activity_hours.isdigit():
            messagebox.showerror("Giá trị không hợp lệ", "Số giờ học phải là số thực.")
            return False
        if not (0 <= float(physical_activity_hours) <= 168):
            messagebox.showerror("Giá trị không hợp lệ", "Số giờ học phải là nằm trong khoảng 0-168.")
            return False
        if not exam_score.isdigit():
            messagebox.showerror("Giá trị không hợp lệ", "Điểm thi phải là số thực.")
            return False
        if not (0 <= float(exam_score) <= 100):
            messagebox.showerror("Giá trị không hợp lệ", "Điểm thi phải nằm trong khoảng 0-100.")
            return False
        
        combobox_fields = [
        ("Parental Involvement", parental_involvement),
        ("Access to Resources", access_to_resources),
        ("Extracurricular Activities", extracurricular_activities),
        ("Motivation Level", motivation_level),
        ("Internet Access", internet_access),
        ("Family Income", family_income),
        ("Teacher Quality", teacher_quality),
        ("School Type", school_type),
        ("Peer Influence", peer_influence),
        ("Learning Disabilities", learning_disabilities),
        ("Parental Education Level", parental_education_level),
        ("Distance from Home", distance_from_home),
        ("Gender", gender)]

        for label, combobox in combobox_fields:
            if combobox == "Chọn một":
                messagebox.showerror("Lỗi dữ liệu", f"Vui lòng chọn một giá trị cho '{label}'.")
                return False

        return True
    except Exception as e:
        messagebox.showerror("Lỗi", f"Đã xảy ra lỗi khi kiểm tra dữ liệu: {str(e)}")
        return False
    
def apply_filters():
    data = {
        "Hours Studied": num1_entry.get(),
        "Attendance (%)": num2_entry.get(),
        "Parental Involvement": num3_combobox.get(),
        "Access to Resources": num4_combobox.get(),
        "Extracurricular Activities": num5_combobox.get(),
        "Sleep Hours": num6_entry.get(),
        "Previous Scores": num7_entry.get(),
        "Motivation Level": num8_combobox.get(),
        "Internet Access": num9_combobox.get(),
        "Number of Tutoring Sessions": num10_entry.get(),
        "Family Income": num11_combobox.get(),
        "Teacher Quality": num12_combobox.get(),
        "School Type": num13_combobox.get(),
        "Peer Influence": num14_combobox.get(),
        "Physical Activity Hours": num15_entry.get(),
        "Learning Disabilities": num16_combobox.get(),
        "Parental Education Level": num17_combobox.get(),
        "Distance from Home": num18_combobox.get(),
        "Gender": num19_combobox.get(),
        "Exam Score": num20_entry.get()}

    if validate_data():
        save_to_csv(data)
    
def clear_filters():
    # Reset giá trị ô nhập liệu
    num1_entry.delete(0, tk.END)
    num2_entry.delete(0, tk.END)
    num6_entry.delete(0, tk.END)
    num7_entry.delete(0, tk.END)
    num10_entry.delete(0, tk.END)
    num15_entry.delete(0, tk.END)
    num20_entry.delete(0, tk.END)
    
    # Reset giá trị combobox
    num3_combobox.set("Chọn một")
    num4_combobox.set("Chọn một")
    num5_combobox.set("Chọn một")
    num8_combobox.set("Chọn một")
    num9_combobox.set("Chọn một")
    num11_combobox.set("Chọn một")
    num12_combobox.set("Chọn một")
    num13_combobox.set("Chọn một")
    num14_combobox.set("Chọn một")
    num16_combobox.set("Chọn một")
    num17_combobox.set("Chọn một")
    num18_combobox.set("Chọn một")
    num19_combobox.set("Chọn một")

root = tk.Tk()
root.title("Survey Form")
root.geometry("640x600")
root.configure(bg="#f5e7df")

tk.Label(root, text="Khảo Sát Các Yếu Tố Ảnh Hưởng Đến Kết Quả Học Tập", bg="#f5e7df", font=("Arial", 16, "bold"), justify="center").pack(pady=(10, 20))

# Frame cuộn cho giao diện
canvas = tk.Canvas(root, bg="#f5e7df", highlightthickness=0)
scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas, bg="#f5e7df")

scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Câu 1
tk.Label(scrollable_frame, text="1. Hours Studied (Số giờ học mỗi tuần).", bg="#f5e7df", font=("Arial", 12)).pack(anchor="w", padx=20, pady=(20, 5))
num1 = tk.Frame(scrollable_frame, bg="#f5e7df")
num1.pack(fill="x", padx=20)
num1_entry = tk.Entry(num1, width=10, justify="right")
num1_entry.pack(side="left", expand=True, fill='both')

# Câu 2
tk.Label(scrollable_frame, text="2. Attendance (Tỷ lệ % tham gia lớp học).", bg="#f5e7df", font=("Arial", 12)).pack(anchor="w", padx=20, pady=(20, 5))
num2 = tk.Frame(scrollable_frame, bg="#f5e7df")
num2.pack(fill="x", padx=20)
num2_entry = tk.Entry(num2, width=10, justify="right")
num2_entry.pack(side="left", expand=True, fill='both')

# Câu 3
tk.Label(scrollable_frame, text="3. Parental Involvement (Mức độ tham gia của phụ huynh vào việc học của sinh viên).", bg="#f5e7df", font=("Arial", 12)).pack(anchor="w", padx=20, pady=(20, 5))
num3_combobox = ttk.Combobox(scrollable_frame, values=["Low", "Medium", "High"], state="readonly")
num3_combobox.pack(fill="x", padx=20)
num3_combobox.set("Chọn một")

# Câu 4
tk.Label(scrollable_frame, text="4. Access to Resources (Mức độ có sẵn các tài nguyên học tập).", bg="#f5e7df", font=("Arial", 12)).pack(anchor="w", padx=20, pady=(20, 5))
num4_combobox = ttk.Combobox(scrollable_frame, values=["Low", "Medium", "High"], state="readonly")
num4_combobox.pack(fill="x", padx=20)
num4_combobox.set("Chọn một")

# Câu 5
tk.Label(scrollable_frame, text="5. Extracurricular Activities (Có tham gia hoạt động ngoại khóa hay không?).", bg="#f5e7df", font=("Arial", 12)).pack(anchor="w", padx=20, pady=(20, 5))
num5_combobox = ttk.Combobox(scrollable_frame, values=["Yes", "No"], state="readonly")
num5_combobox.pack(fill="x", padx=20)
num5_combobox.set("Chọn một")

# Câu 6
tk.Label(scrollable_frame, text="6. Sleep Hours (Số giờ ngủ trung bình mỗi đêm.", bg="#f5e7df", font=("Arial", 12)).pack(anchor="w", padx=20, pady=(20, 5))
num6 = tk.Frame(scrollable_frame, bg="#f5e7df")
num6.pack(fill="x", padx=20)
num6_entry = tk.Entry(num6, width=10, justify="right")
num6_entry.pack(side="left", expand=True, fill='both')

# Câu 7
tk.Label(scrollable_frame, text="7. Previous Scores (Điểm số bài kiểm tra trước đó 0-100).", bg="#f5e7df", font=("Arial", 12)).pack(anchor="w", padx=20, pady=(20, 5))
num7 = tk.Frame(scrollable_frame, bg="#f5e7df")
num7.pack(fill="x", padx=20)
num7_entry = tk.Entry(num7, width=10, justify="right")
num7_entry.pack(side="left", expand=True, fill='both')

# Câu 8
tk.Label(scrollable_frame, text="8. Motivation Level (Mức độ động lực của sinh viên).", bg="#f5e7df", font=("Arial", 12)).pack(anchor="w", padx=20, pady=(20, 5))
num8_combobox = ttk.Combobox(scrollable_frame, values=["Low", "Medium", "High"], state="readonly")
num8_combobox.pack(fill="x", padx=20)
num8_combobox.set("Chọn một")

# Câu 9
tk.Label(scrollable_frame, text="9. Internet Access (Có sử dụng Internet không?)", bg="#f5e7df", font=("Arial", 12)).pack(anchor="w", padx=20, pady=(20, 5))
num9_combobox = ttk.Combobox(scrollable_frame, values=["Yes", "No"], state="readonly")
num9_combobox.pack(fill="x", padx=20)
num9_combobox.set("Chọn một")

# Câu 10
tk.Label(scrollable_frame, text="10. Number of Tutoring Sessions (Số buổi học thêm mỗi tháng).", bg="#f5e7df", font=("Arial", 12)).pack(anchor="w", padx=20, pady=(20, 5))
num10 = tk.Frame(scrollable_frame, bg="#f5e7df")
num10.pack(fill="x", padx=20)
num10_entry = tk.Entry(num10, width=10, justify="right")
num10_entry.pack(side="left", expand=True, fill='both')

# Câu 11
tk.Label(scrollable_frame, text="11. Family Income (Mức thu nhập của gia đình).", bg="#f5e7df", font=("Arial", 12)).pack(anchor="w", padx=20, pady=(20, 5))
num11_combobox = ttk.Combobox(scrollable_frame, values=["Low", "Medium", "High"], state="readonly")
num11_combobox.pack(fill="x", padx=20)
num11_combobox.set("Chọn một")

# Câu 12
tk.Label(scrollable_frame, text="12. Teacher Quality (Chất lượng của giáo viên).", bg="#f5e7df", font=("Arial", 12)).pack(anchor="w", padx=20, pady=(20, 5))
num12_combobox = ttk.Combobox(scrollable_frame, values=["Low", "Medium", "High"], state="readonly")
num12_combobox.pack(fill="x", padx=20)
num12_combobox.set("Chọn một")

# Câu 13
tk.Label(scrollable_frame, text="13. School Type (Loại trường sinh viên đang học).", bg="#f5e7df", font=("Arial", 12)).pack(anchor="w", padx=20, pady=(20, 5))
num13_combobox = ttk.Combobox(scrollable_frame, values=["Public", "Private"], state="readonly")
num13_combobox.pack(fill="x", padx=20)
num13_combobox.set("Chọn một")

# Câu 14
tk.Label(scrollable_frame, text="14. Peer Influence (Ảnh hưởng của bạn bè đối với kết quả học tập).", bg="#f5e7df", font=("Arial", 12)).pack(anchor="w", padx=20, pady=(20, 5))
num14_combobox = ttk.Combobox(scrollable_frame, values=["Positive", "Neutral", "Negative"], state="readonly")
num14_combobox.pack(fill="x", padx=20)
num14_combobox.set("Chọn một")

# Câu 15
tk.Label(scrollable_frame, text="15. Physical Activity (Số giờ tham gia hoạt động thể chất mỗi tuần).", bg="#f5e7df", font=("Arial", 12)).pack(anchor="w", padx=20, pady=(20, 5))
num15 = tk.Frame(scrollable_frame, bg="#f5e7df")
num15.pack(fill="x", padx=20)
num15_entry = tk.Entry(num15, width=10, justify="right")
num15_entry.pack(side="left", expand=True, fill='both')

# Câu 16
tk.Label(scrollable_frame, text="16. Learning Disabilities (Sinh viên có khuyết tật học tập không? (Gặp khó khăn khi nghe, suy nghĩ, nói, viết, đánh vần hoặc tính toán)).", bg="#f5e7df", font=("Arial", 12), wraplength=600, justify='left').pack(anchor="w", padx=20, pady=(20, 5))
num16_combobox = ttk.Combobox(scrollable_frame, values=["Yes", "No"], state="readonly")
num16_combobox.pack(fill="x", padx=20)
num16_combobox.set("Chọn một")

# Câu 17
tk.Label(scrollable_frame, text="17. Parental Education Level (Trình độ học vấn cao nhất của phụ huynh).", bg="#f5e7df", font=("Arial", 12)).pack(anchor="w", padx=20, pady=(20, 5))
num17_combobox = ttk.Combobox(scrollable_frame, values=["High School", "College", "Postgraduate"], state="readonly")
num17_combobox.pack(fill="x", padx=20)
num17_combobox.set("Chọn một")

# Câu 18
tk.Label(scrollable_frame, text="18. Distance from Home (Khoảng cách từ nhà đến trường, km).", bg="#f5e7df", font=("Arial", 12)).pack(anchor="w", padx=20, pady=(20, 5))
num18_combobox = ttk.Combobox(scrollable_frame, values=["Near", "Moderate", "Far"], state="readonly")
num18_combobox.pack(fill="x", padx=20)
num18_combobox.set("Chọn một")

# Câu 19
tk.Label(scrollable_frame, text="19. Gender (Giới tính của sinh viên).", bg="#f5e7df", font=("Arial", 12)).pack(anchor="w", padx=20, pady=(20, 5))
num19_combobox = ttk.Combobox(scrollable_frame, values=["Male", "Female"], state="readonly")
num19_combobox.pack(fill="x", padx=20)
num19_combobox.set("Chọn một")

# Câu 20
tk.Label(scrollable_frame, text="20. Exam Score (Điểm thi cuối kì 0-100).", bg="#f5e7df", font=("Arial", 12)).pack(anchor="w", padx=20, pady=(20, 5))
num20 = tk.Frame(scrollable_frame, bg="#f5e7df")
num20.pack(fill="x", padx=20)
num20_entry = tk.Entry(num20, width=10, justify="right")
num20_entry.pack(side="left", expand=True, fill='both')

# Buttons Section
button_frame = tk.Frame(scrollable_frame, bg="#f5e7df")
button_frame.pack(fill="x", pady=(20, 20), padx=20)

clear_button = tk.Button(button_frame, text="Clear", command=clear_filters, bg="#ffffff", font=("Arial", 10), width=10)
clear_button.pack(side="left", padx=10)
apply_button = tk.Button(button_frame, text="Apply", command=apply_filters, bg="#000000", fg="#ffffff", font=("Arial", 10), width=10)
apply_button.pack(side="right", padx=10)

makecenter(root)
root.mainloop()