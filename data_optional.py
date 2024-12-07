import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import subprocess
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import data_visualization

file_path = "data_source\\cleaned_data.csv"
recent_files_data = pd.read_csv(file_path)

edited_data = recent_files_data.copy()

# Tạo danh sách các hàm vẽ
plot_one = [  
    data_visualization.plot_hours_studied_distribution, 
    data_visualization.plot_attendance_distribution,
    data_visualization.plot_parental_involvement_distribution,
    data_visualization.plot_access_to_resources_distribution,
    data_visualization.plot_extracurricular_activities_distribution,
    data_visualization.plot_sleep_hours_distribution,
    data_visualization.plot_previous_scores_distribution,
    data_visualization.plot_motivation_level_distribution,
    data_visualization.plot_internet_access_distribution,
    data_visualization.plot_tutoring_sessions_distribution,
    data_visualization.plot_family_income_distribution,
    data_visualization.plot_teacher_quality_distribution,
    data_visualization.plot_school_type_distribution,
    data_visualization.plot_peer_influence_distribution,
    data_visualization.plot_physical_activity_distribution,
    data_visualization.plot_learning_disabilities_distribution,
    data_visualization.plot_parental_education_level_distribution,
    data_visualization.plot_distance_from_home_distribution,
    data_visualization.plot_gender_distribution,
    data_visualization.plot_exam_score_distribution,
]

insight_one = [
    data_visualization.hours_studied_insight,
    data_visualization.attendance_insight,
    data_visualization.parental_involvement_insight,
    data_visualization.access_to_resources_insight,
    data_visualization.extracurricular_activities_insight,
    data_visualization.sleep_hours_insight,
    data_visualization.previous_scores_insight,
    data_visualization.motivation_level_insight,
    data_visualization.internet_access_insight,
    data_visualization.tutoring_sessions_insight,
    data_visualization.family_income_insight,
    data_visualization.teacher_quality_insight,
    data_visualization.school_type_insight,
    data_visualization.peer_influence_insight,
    data_visualization.physical_activity_insight,
    data_visualization.learning_disabilities_insight,
    data_visualization.parental_education_insight,
    data_visualization.distance_from_home_insight,
    data_visualization.gender_insight,
    data_visualization.exam_score_insight,
]

plots_and_insights_two = [  
    (data_visualization.scatterplot_Hours_Studied_and_Exam_Score, None),
    (data_visualization.scatterplot_Attendance_and_Exam_Score, None),
    (data_visualization.scatterplot_Previous_Scores_and_Exam_Score, None),
    (data_visualization.scatterplot_Numcol_and_Exam_Score_with_Extracurricular_Activities, 
     data_visualization.compare_exam_scores_by_activity),
    (data_visualization.scatterplot_Numcol_and_Exam_Score_with_Gender, 
     data_visualization.compare_exam_scores_by_gender),
    (data_visualization.scatterplot_Numcol_and_Exam_Score_with_Internet_Access, 
     data_visualization.compare_exam_scores_by_internet_access),
    (data_visualization.scatterplot_Numcol_and_Exam_Score_with_Learning_Disabilities, 
     data_visualization.compare_exam_scores_by_learning_disabilities),
    (data_visualization.boxplot_Parental_Involvement_and_Exam_Score, None),
    (data_visualization.boxplot_Access_to_Resources_and_Exam_Score, None),
    (data_visualization.boxplot_Extracurricular_Activities_and_Exam_Score, None),
    (data_visualization.boxplot_Sleep_Hours_and_Exam_Score, None),
    (data_visualization.boxplot_Motivation_Level_and_Exam_Score, None),
    (data_visualization.boxplot_Internet_Access_and_Exam_Score, None),
    (data_visualization.boxplot_Tutoring_Sessions_and_Exam_Score, None),
    (data_visualization.boxplot_Family_Income_and_Exam_Score, None),
    (data_visualization.boxplot_Teacher_Quality_and_Exam_Score, None),
    (data_visualization.boxplot_School_Type_and_Exam_Score, None),
    (data_visualization.boxplot_Peer_Influence_and_Exam_Score, None),
    (data_visualization.boxplot_Physical_Activity_and_Exam_Score, None),
    (data_visualization.boxplot_Learning_Disabilities_and_Exam_Score, None),
    (data_visualization.boxplot_Parental_Education_Level_and_Exam_Score, None),
    (data_visualization.boxplot_Distance_from_Home_and_Exam_Score, None),
    (data_visualization.boxplot_Gender_and_Exam_Score, None)
]

categories = [
    ("QUẢN LÍ", "#F52F57"),
    ("PHÂN TÍCH", "#3DDE86"),
]

# Biến lưu trạng thái danh mục hiện tại
current_category = None
buttons = {}

def update_category_colors(selected_category):
    """Cập nhật màu sắc các nút danh mục."""
    for category, button in buttons.items():
        if category == selected_category:
            button.config(bg="#ffffff", fg="#000000")  # Đổi màu
        else:
            button.config(bg=category_colors[category])  # Trả lại màu gốc

def show_category(category_name):
    global current_category
    current_category = category_name
    update_category_colors(category_name)

    # Xóa bảng Recent Files
    for widget in content_frame.winfo_children():
        widget.destroy()

    if category_name == "QUẢN LÍ":
        show_recent_files()
    elif category_name == "PHÂN TÍCH":
        show_chart1()

def makecenter(root, width, height):
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

def edit_cell(event):
    """Cho phép chỉnh sửa ô dữ liệu khi nhấp đúp."""
    selected_item = tree.focus()  # Lấy item đang được chọn
    if not selected_item:
        return

    col = tree.identify_column(event.x)  # Lấy cột đang nhấp
    col_index = int(col.replace("#", "")) - 1  # Chuyển cột thành chỉ số
    # Không cho phép chỉnh sửa cột STT
    if col_index == 0:  # Cột đầu tiên (STT)
        return
    column_name = recent_files_data.columns[col_index-1]  # Lấy tên cột
    row_id = tree.index(selected_item)  # Lấy chỉ số hàng

    numeric_columns = {
        "Hours_Studied": (0,168),
        "Attendance": (0,100),
        "Sleep_Hours":(4,12),
        "Previous_Scores": (0,100),
        "Tutoring_Sessions": (0,8),
        "Phycical_Activity": (0,6),
        "Exam_Score": (0,100),
        }

    # Hiện giá trị hiện tại
    current_value = tree.item(selected_item, "values")[col_index]

    # Tạo Entry hoặc Combobox tùy theo kiểu dữ liệu
    if column_name in numeric_columns:  # Nếu cột thuộc loại số, dùng Entry
        entry = tk.Entry(content_frame, font=("Arial", 10))
        entry.insert(0, current_value)
        entry.place(
            x=event.x_root - content_frame.winfo_rootx(),
            y=event.y_root - content_frame.winfo_rooty(),
        )
        entry.focus_set()

        def save_edit(event):
            """Lưu giá trị mới và cập nhật Treeview."""
            new_value = entry.get()
            try:
                new_value = int(new_value)
                min_value, max_value = numeric_columns[column_name]  # Lấy giới hạn cho cột
                if not (min_value <= new_value <= max_value):
                    messagebox.showerror("Lỗi", f"Giá trị phải nằm trong khoảng từ {min_value} đến {max_value}.")
                    return
            except ValueError:
                messagebox.showerror("Lỗi", "Giá trị nhập vào không hợp lệ.")
                return
            tree.set(selected_item, column=column_name, value=new_value)  # Cập nhật giá trị Treeview
            edited_data.at[row_id, column_name] = new_value  # Cập nhật vào DataFrame
            entry.destroy()

        entry.bind("<Return>", save_edit)  # Lưu thay đổi khi nhấn Enter
        entry.bind("<FocusOut>", lambda _: entry.destroy())  # Hủy khi mất tiêu điểm

    else:  # Nếu cột không thuộc loại số, dùng Combobox
        unique_values = recent_files_data[column_name].dropna().unique().tolist()  # Lấy giá trị duy nhất
        combobox = ttk.Combobox(content_frame, values=unique_values, font=("Arial", 10))
        combobox.set(current_value)
        combobox.place(
            x=event.x_root - content_frame.winfo_rootx(),
            y=event.y_root - content_frame.winfo_rooty(),
        )
        combobox.focus_set()
        combobox.event_generate("<Button-1>")

        def save_edit(event):
            """Lưu giá trị mới và cập nhật Treeview."""
            new_value = combobox.get()
            tree.set(selected_item, column=column_name, value=new_value)  # Cập nhật giá trị Treeview
            edited_data.at[row_id, column_name] = new_value  # Cập nhật vào DataFrame
            combobox.destroy()
        
        combobox.bind("<Return>", save_edit)  # Lưu thay đổi khi nhấn Enter
        combobox.bind("<FocusOut>", lambda _: combobox.destroy())  # Hủy khi mất tiêu

def update_csv():
    """Lưu thay đổi vào file CSV với xác nhận từ người dùng."""
    confirm = messagebox.askyesno("Xác nhận", "Bạn có chắc chắn muốn lưu thay đổi vào file CSV?")
    if confirm:
        edited_data.to_csv(file_path, index=False)  # Ghi dữ liệu vào file
        messagebox.showinfo("Thành công", "Dữ liệu đã được lưu thành công!")
    else:
        messagebox.showinfo("Hủy bỏ", "Dữ liệu chưa được lưu.")

def delete_selected_rows():
    """Xóa các dòng được chọn sau khi xác nhận."""
    selected_items = tree.selection()  # Lấy các dòng được chọn

    if not selected_items:
        messagebox.showwarning("Cảnh báo", "Vui lòng chọn ít nhất một dòng để xóa.")
        return

    confirm = messagebox.askyesno("Xác nhận", "Bạn có chắc chắn muốn xóa dòng đã chọn?")
    if confirm:
        for item in selected_items:
            # Lấy giá trị STT từ Treeview
            stt = int(tree.item(item, "values")[0])  # Cột STT là cột đầu tiên, giá trị tại index 0

            # Xóa dòng trong DataFrame dựa trên STT
            index_to_drop = stt - 1  # STT bắt đầu từ 1, trong khi DataFrame index bắt đầu từ 0
            if 0 <= index_to_drop < len(edited_data):
                edited_data.drop(index=edited_data.index[index_to_drop], inplace=True)

            # Xóa dòng khỏi Treeview
            tree.delete(item)

        # Cập nhật lại DataFrame để làm mới chỉ số
        edited_data.reset_index(drop=True, inplace=True)
        messagebox.showinfo("Thành công", "Dòng đã được xóa thành công!")

def add_data():
    """Thêm thông tin khảo sát mới."""
    try:
        subprocess.run(["python", "New_survey.py"], check=True) # Gọi chương trình New_survey.py
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Error running the external program: {e}")

def display_data_in_treeview(data):
    """Hiển thị DataFrame trong Treeview."""
    # Xóa dữ liệu cũ
    tree.delete(*tree.get_children())

    # Cập nhật cột
    tree["columns"] = ['STT'] + list(data.columns)
    tree.heading("STT", text="STT")
    tree.column("STT", width=50, anchor="center")
    for col in data.columns:
        tree.heading(col, text=col)
        tree.column(col, anchor="w", width=100)

    # Thêm dữ liệu mới
    for _, row in data.iterrows():
        tree.insert("", "end", values= [_+1] + list(row))

def filter_by_text():
    """Lọc dữ liệu theo giá trị chữ trong các cột đã chọn."""
    # Tạo cửa sổ chọn cột
    filter_window = tk.Toplevel(root)
    filter_window.title("Lọc theo giá trị chữ")
    filter_window.geometry("400x600")

    # Lọc các cột có kiểu dữ liệu là string
    text_columns = [col for col in recent_files_data.columns if recent_files_data[col].dtype == 'object']

    if not text_columns:
        tk.Label(filter_window, text="Không có cột nào chứa giá trị chữ.", font=("Arial", 12)).pack(pady=10)
        return

    # Biến lưu trạng thái của các cột được chọn
    column_selected = {col: tk.BooleanVar(value=False) for col in text_columns}
    column_to_value = {col: tk.StringVar(value="") for col in text_columns}

    # Hiển thị danh sách các cột với Checkbutton và Combobox để chọn giá trị
    tk.Label(filter_window, text="Chọn các cột và giá trị muốn lọc:", font=("Arial", 12)).pack(pady=10)

    columns_frame = tk.Frame(filter_window)
    columns_frame.pack(pady=10, fill=tk.BOTH, expand=True)

    # Thanh cuộn cho danh sách cột
    columns_canvas = tk.Canvas(columns_frame)
    scrollbar = ttk.Scrollbar(columns_frame, orient="vertical", command=columns_canvas.yview)
    columns_container = tk.Frame(columns_canvas)

    columns_container.bind("<Configure>", lambda e: columns_canvas.configure(scrollregion=columns_canvas.bbox("all")))
    columns_canvas.create_window((0, 0), window=columns_container, anchor="nw")
    columns_canvas.configure(yscrollcommand=scrollbar.set)

    columns_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    for col in text_columns:
        frame = tk.Frame(columns_container)
        frame.pack(fill=tk.X, pady=2)

        # Checkbutton để chọn cột
        tk.Checkbutton(frame, text=col, variable=column_selected[col], font=("Arial", 10)).pack(side=tk.LEFT, padx=5)

        # Combobox để chọn giá trị
        unique_values = recent_files_data[col].dropna().unique().tolist()
        combobox = ttk.Combobox(frame, textvariable=column_to_value[col], font=("Arial", 10), width=20)
        combobox['values'] = unique_values  # Gán danh sách giá trị duy nhất
        combobox.pack(side=tk.RIGHT, padx=5)

    def apply_filter():
        """Áp dụng bộ lọc dựa trên các giá trị đã chọn."""
        global edited_data, current_page, total_pages

        recent_files_data = pd.read_csv(file_path)
        filtered_data = recent_files_data

        # Lọc dữ liệu theo các cột được chọn
        for col, selected in column_selected.items():
            if selected.get():  # Nếu cột được chọn
                value = column_to_value[col].get().strip()
                if value:  # Nếu giá trị được chọn
                    filtered_data = filtered_data[filtered_data[col] == value]

        # Cập nhật dữ liệu đã chỉnh sửa
        edited_data = filtered_data.copy()

        # Giữ nguyên STT ban đầu
        if "Original_STT" not in edited_data.columns:
            edited_data["Original_STT"] = range(1, len(edited_data) + 1)

        # Cập nhật phân trang
        current_page = 0
        total_pages = (len(edited_data) + rows_per_page - 1) // rows_per_page

        # Hiển thị lại dữ liệu
        update_treeview(current_page)

        filter_window.destroy()
    
    tk.Button(filter_window, text="Lọc", command=apply_filter, bg="#56CBF9", fg="#FFFFFF").pack(pady=10)

def filter_by_single_value():
    """Lọc dữ liệu theo một giá trị duy nhất trong một cột."""
    recent_files_data = pd.read_csv(file_path)
    filter_window = tk.Toplevel(root)
    filter_window.title("Lọc theo giá trị duy nhất")
    filter_window.geometry("300x200")
    # Label chọn cột
    tk.Label(filter_window, text="Chọn cột để lọc:", font=("Arial", 12)).pack(pady=5)

    # Lọc các cột có kiểu dữ liệu số
    numeric_columns = [col for col in recent_files_data.columns if recent_files_data[col].dtype in ['int64', 'float64']]

    if not numeric_columns:
        tk.Label(filter_window, text="Không có cột nào chứa giá trị số.", font=("Arial", 12)).pack(pady=10)
        return

    # Biến để lưu cột được chọn và danh sách các giá trị để lọc
    selected_column = tk.StringVar(value="")
    input_value = tk.StringVar(value="")

    # Dropdown menu để chọn cột
    column_dropdown = ttk.Combobox(filter_window, textvariable=selected_column, state="readonly", font=("Arial", 11))
    column_dropdown['values'] = numeric_columns
    column_dropdown.pack(pady=5)

    # Label nhập giá trị
    tk.Label(filter_window, text="Nhập giá trị muốn lọc:", font=("Arial", 12)).pack(pady=5)

    # Entry để nhập các giá trị cần lọc
    values_entry = tk.Entry(filter_window, textvariable=input_value, font=("Arial", 11), width=25)
    values_entry.pack(pady=5)

    def apply_filter():
        """Áp dụng bộ lọc với cột và danh sách giá trị đã nhập."""
        global edited_data, current_page, total_pages

        column_name = selected_column.get()
        value = input_value.get()

        if column_name and value:
            try:
                value = float(value)  # Chuyển giá trị sang dạng số
                edited_data = recent_files_data[recent_files_data[column_name] == value]

                current_page = 0
                total_pages = (len(edited_data) + rows_per_page - 1) // rows_per_page

                update_treeview(current_page)
                filter_window.destroy()
            except ValueError:
                tk.messagebox.showerror("Lỗi", "Vui lòng nhập các giá trị hợp lệ (số).")
        else:
            tk.messagebox.showerror("Lỗi", "Vui lòng chọn một cột và nhập giá trị để lọc.")
    
    tk.Button(filter_window, text="Lọc", command=apply_filter, bg="#56CBF9", fg="#FFFFFF").pack(pady=10)

def filter_by_multiple_values():
    filter_window = tk.Toplevel(root)
    filter_window.title("Lọc theo nhiều giá trị")
    filter_window.geometry("400x200")

    # Nhập tên cột cần lọc
    tk.Label(filter_window, text="Chọn cột để lọc:", font=("Arial", 12)).pack(pady=10)
    
    # Lọc các cột có kiểu dữ liệu số
    numeric_columns = [col for col in recent_files_data.columns if recent_files_data[col].dtype in ['int64', 'float64']]

    if not numeric_columns:
        tk.Label(filter_window, text="Không có cột nào chứa giá trị số.", font=("Arial", 12)).pack(pady=10)
        return

    # Biến để lưu cột được chọn và danh sách các giá trị để lọc
    selected_column = tk.StringVar(value="")
    entered_values = tk.StringVar(value="")  # Lưu các giá trị được nhập (ngăn cách bằng dấu phẩy)

    # Dropdown menu để chọn cột
    column_dropdown = ttk.Combobox(filter_window, textvariable=selected_column, state="readonly", font=("Arial", 11))
    column_dropdown['values'] = numeric_columns
    column_dropdown.pack(pady=5)

    # Label nhập giá trị
    tk.Label(filter_window, text="Nhập các giá trị muốn lọc (ngăn cách bằng dấu phẩy):", font=("Arial", 12)).pack(pady=5)

    # Entry để nhập các giá trị cần lọc
    values_entry = tk.Entry(filter_window, textvariable=entered_values, font=("Arial", 11), width=40)
    values_entry.pack(pady=5)

    def apply_filter():
        """Áp dụng bộ lọc với cột và danh sách giá trị đã nhập."""
        recent_files_data = pd.read_csv(file_path)
        global edited_data, current_page, total_pages

        column_name = selected_column.get()
        values_text = entered_values.get()

        if column_name and values_text:
            try:
                # Chuyển danh sách giá trị từ chuỗi sang list số
                filter_values = [float(v.strip()) for v in values_text.split(",")]

                # Lọc dữ liệu
                edited_data = recent_files_data[recent_files_data[column_name].isin(filter_values)]

                current_page = 0
                total_pages = (len(edited_data) + rows_per_page - 1) // rows_per_page

                update_treeview(current_page)
                filter_window.destroy()
            except ValueError:
                tk.messagebox.showerror("Lỗi", "Vui lòng nhập các giá trị hợp lệ (số).")
        else:
            tk.messagebox.showerror("Lỗi", "Vui lòng chọn một cột và nhập giá trị để lọc.")
    
    tk.Button(filter_window, text="Lọc", command=apply_filter, bg="#56CBF9", fg="#FFFFFF").pack(pady=10)

def filter_by_range():
    recent_files_data = pd.read_csv(file_path)
    filter_window = tk.Toplevel(root)
    filter_window.title("Lọc theo phạm vi giá trị")
    filter_window.geometry("500x350")

    # Lọc các cột có kiểu dữ liệu số
    numeric_columns = [col for col in recent_files_data.columns if recent_files_data[col].dtype in ['int64', 'float64']]

    if not numeric_columns:
        tk.Label(filter_window, text="Không có cột nào chứa giá trị số.", font=("Arial", 12)).pack(pady=10)
        return

    # Biến lưu cột được chọn
    selected_column = tk.StringVar(value=numeric_columns[0])
    min_value = tk.DoubleVar()
    max_value = tk.DoubleVar()

    def update_scales(*args):
        """Cập nhật phạm vi của thanh kéo theo cột được chọn."""
        column_name = selected_column.get()
        if column_name:
            col_min = recent_files_data[column_name].min()
            col_max = recent_files_data[column_name].max()
            scale_min.config(from_=col_min, to=col_max)
            scale_max.config(from_=col_min, to=col_max)
            min_value.set(col_min)
            max_value.set(col_max)

    # Label chọn cột
    tk.Label(filter_window, text="Chọn cột để lọc:", font=("Arial", 12)).pack(pady=5)

    # Dropdown menu để chọn cột
    column_dropdown = ttk.Combobox(filter_window, textvariable=selected_column, state="readonly", font=("Arial", 11))
    column_dropdown['values'] = numeric_columns
    column_dropdown.pack(pady=5)
    column_dropdown.bind("<<ComboboxSelected>>", update_scales)

    # Thanh kéo chọn giá trị nhỏ nhất
    tk.Label(filter_window, text="Giá trị nhỏ nhất:", font=("Arial", 12)).pack(pady=5)
    scale_min = tk.Scale(filter_window, variable=min_value, orient="horizontal", length=400, resolution=1)
    scale_min.pack(pady=5)

    # Thanh kéo chọn giá trị lớn nhất
    tk.Label(filter_window, text="Giá trị lớn nhất:", font=("Arial", 12)).pack(pady=5)
    scale_max = tk.Scale(filter_window, variable=max_value, orient="horizontal", length=400, resolution=1)
    scale_max.pack(pady=5)

    def apply_filter():
        global edited_data, current_page, total_pages

        column_name = selected_column.get()
        if column_name:
            lower_bound = min_value.get()
            upper_bound = max_value.get()
            edited_data = recent_files_data[
                (recent_files_data[column_name] >= lower_bound) & (recent_files_data[column_name] <= upper_bound)
            ]

            current_page = 0
            total_pages = (len(edited_data) + rows_per_page - 1) // rows_per_page

            update_treeview(current_page)
            filter_window.destroy()

    tk.Button(filter_window, text="Lọc", command=apply_filter, bg="#56CBF9", fg="#FFFFFF").pack(pady=10)
    update_scales()

def sort_data(order="asc"):
    """Hàm sắp xếp dữ liệu tăng dần hoặc giảm dần.""" 
    recent_files_data = pd.read_csv(file_path)
    sort_window = tk.Toplevel(root)
    sort_window.title("Chọn cột để sắp xếp")
    sort_window.geometry("300x350")

    # Lọc ra các cột có giá trị số
    numeric_columns = [col for col in recent_files_data.columns if recent_files_data[col].dtype in ['int64', 'float64']]

    selected_column = tk.StringVar()
    selected_column.set(0)

    for col in numeric_columns:
        tk.Radiobutton(
            sort_window,
            text=col,
            variable=selected_column,
            value=col,
            font=("Arial", 12),
            anchor="w"
        ).pack(fill=tk.X, pady=2)

    # Nút xác nhận
    def apply_sort():
        column_to_sort = selected_column.get()
        if not column_to_sort:
            tk.messagebox.showwarning("Thông báo", "Vui lòng chọn một cột để sắp xếp!")
            return
        sort_window.destroy()

        global edited_data, current_page, total_pages

        # Sắp xếp theo thứ tự tăng dần hoặc giảm dần
        edited_data = recent_files_data.sort_values(by=column_to_sort, ascending=(order == "asc"))

        current_page = 0
        total_pages = (len(edited_data) + rows_per_page - 1) // rows_per_page

        # Hiển thị dữ liệu của trang đầu tiên
        update_treeview(current_page)

    tk.Button(
        sort_window,
        text="Áp dụng sắp xếp",
        font=("Arial", 12, "bold"),
        bg="#56CBF9",
        fg="#FFFFFF",
        command=apply_sort
    ).pack(pady=10)

def show_n_rows(n):
        global edited_data, current_page, total_pages
        """Hiển thị n dòng đầu tiên."""
        recent_files_data = pd.read_csv(file_path)
        if n is None:  # Người dùng nhấn Cancel hoặc không nhập gì
            return

        if n <= 0 or n > len(recent_files_data):
            messagebox.showwarning("Thông báo", f"Số dòng từ 1 đến {len(recent_files_data)}!")
            return

        # Lọc dữ liệu chỉ lấy n dòng đầu tiên
        edited_data = recent_files_data.head(n).copy()

        # Reset phân trang
        current_page = 0
        total_pages = (len(edited_data) + rows_per_page - 1) // rows_per_page

        # Hiển thị dữ liệu của trang đầu tiên
        update_treeview(current_page)
        messagebox.showinfo("Success", f"Hiển thị từ dòng 1 đến {n}")
    
def show_n_columns(n):
        """Hiển thị n cột đầu tiên."""
        recent_files_data = pd.read_csv(file_path)
        if n is None:  # Người dùng nhấn Cancel hoặc không nhập gì
            return

        if n <= 0:
            tk.messagebox.showwarning("Thông báo", "Số cột phải lớn hơn 0!")
            return

        if n > len(recent_files_data.columns):
            tk.messagebox.showwarning("Thông báo", f"Dữ liệu chỉ có {len(recent_files_data.columns)} cột!")
            n = len(recent_files_data.columns)

        # Lấy n cột đầu tiên
        tree.delete(*tree.get_children())  # Xóa các hàng cũ
        tree["columns"] = ["STT"] + list(recent_files_data.columns[:n])  # Lấy n cột đầu tiên

        # Cấu hình lại cột trong Treeview
        for col in tree["columns"]:
            tree.heading(col, text=col)
            tree.column(col, anchor="w", width=100)

        # Thêm dữ liệu vào bảng
        for _, row in recent_files_data.iterrows():
            tree.insert("", "end", values=[_+1] + list(row[:n]))

        tk.messagebox.showinfo("Success", f"Đã hiển thị {n} cột đầu tiên.")    

def show_specific_columns():
    """Hiển thị các cột cụ thể."""
    recent_files_data = pd.read_csv(file_path)
    column_window = tk.Toplevel(root)
    column_window.title("Chọn các cột muốn hiển thị")
    column_window.geometry("400x400")

    # Frame cuộn cho giao diện
    canvas = tk.Canvas(column_window)
    scrollbar = ttk.Scrollbar(column_window, 
                              orient="vertical", 
                              command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), 
                         window=scrollable_frame, 
                         anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", 
                fill="both", 
                expand=True)
    scrollbar.pack(side="right", 
                   fill="y")

    # Danh sách checkbox
    column_vars = {}
    for col in recent_files_data.columns:
        var = tk.BooleanVar(value=False)  # Mặc định tích chọn
        column_vars[col] = var
        tk.Checkbutton(
            scrollable_frame,
            text=col,
            variable=var,
            font=("Arial", 12),
            anchor="w"
        ).pack(fill=tk.X, pady=2)
        

    # Nút xác nhận
    def apply_selection():
        selected_columns = [col for col, var in column_vars.items() if var.get()]
        if not selected_columns:
            tk.messagebox.showwarning("Thông báo", "Vui lòng chọn ít nhất một cột!")
            return
        column_window.destroy()
        # Hiển thị dữ liệu các cột được chọn
        data = recent_files_data[selected_columns]
        display_data_in_treeview(data)

    tk.Button(
        scrollable_frame,
        text="Xem",
        font=("Arial", 12, "bold"),
        bg="#56CBF9",
        fg="#FFFFFF",
        command=apply_selection
    ).pack(pady=10, fill=tk.X, anchor='center')
        
def show_specific_columns_with_rows():
    recent_files_data = pd.read_csv(file_path)
    column_window = tk.Toplevel(root)
    column_window.title("Chọn các cột muốn hiển thị")
    column_window.geometry("400x400")

    # Frame cuộn cho giao diện
    canvas = tk.Canvas(column_window)
    scrollbar = ttk.Scrollbar(column_window, 
                              orient="vertical", 
                              command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), 
                         window=scrollable_frame, 
                         anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", 
                fill="both", 
                expand=True)
    scrollbar.pack(side="right", 
                   fill="y")

    # Danh sách checkbox
    column_vars = {}
    for col in recent_files_data.columns:
        var = tk.BooleanVar(value=False)
        column_vars[col] = var
        tk.Checkbutton(
            scrollable_frame,
            text=col,
            variable=var,
            font=("Arial", 12),
            anchor="w"
        ).pack(fill=tk.X, pady=2)

    # Entry nhập số hàng
    rows_label = ttk.Label(scrollable_frame, text="Nhập số hàng muốn hiển thị:")
    rows_label.pack()
    rows_entry = ttk.Entry(scrollable_frame, width=25)
    rows_entry.pack()

    # Nút xác nhận
    def apply_selection():   
        global edited_data, current_page, total_pages     
        selected_columns = [col for col, var in column_vars.items() if var.get()]
        if not selected_columns:
            tk.messagebox.showwarning("Thông báo", "Vui lòng chọn ít nhất một cột!")
            return
        
        num_rows = int(rows_entry.get())
        if num_rows < 1:
            raise ValueError("Number of rows must be greater than 0!")

        column_window.destroy()
        # Hiển thị dữ liệu các cột được chọn

        edited_data = recent_files_data[selected_columns].head(num_rows)
        current_page = 0
        total_pages = (len(edited_data) + rows_per_page - 1) // rows_per_page
        display_data_in_treeview(edited_data)

        update_treeview(current_page)

    tk.Button(
        scrollable_frame,
        text="Áp dụng",
        font=("Arial", 12, "bold"),
        bg="#56CBF9",
        fg="#FFFFFF",
        command=apply_selection
    ).pack(pady=10, fill=tk.X)

def show_specific_rows():
        global edited_data, current_page, total_pages
        recent_files_data = pd.read_csv(file_path)
        """Hiển thị các dòng mong muốn."""
        input_range = simpledialog.askstring("Hiển thị các dòng mong muốn", "Nhập khoảng dòng (ví dụ: 5-15):")
        if not input_range:
            return

        try:
            # Tách chỉ số bắt đầu và kết thúc
            start, end = map(int, input_range.split("-"))
            start -= 1  # Chuyển sang chỉ số bắt đầu từ 0
            end -= 1
        except ValueError:
            messagebox.showerror("Lỗi", "Vui lòng nhập khoảng dòng hợp lệ (dạng số, ví dụ: 5-15)!")
            return
                    
        max_index = len(recent_files_data) - 1
        if start < 0 or end > max_index or start > end:
            messagebox.showerror(
                "Lỗi",
                f"Khoảng dòng không hợp lệ. Vui lòng nhập giá trị từ 1 đến {max_index + 1} và đảm bảo chỉ số bắt đầu <= chỉ số kết thúc."
            )
            return

        # Lấy dữ liệu của các dòng cụ thể
        edited_data = recent_files_data.iloc[start:end + 1]
        current_page = 0
        total_pages = (len(edited_data) + rows_per_page - 1) // rows_per_page

        update_treeview(current_page)

def update_treeview(page):
    """Cập nhật Treeview để hiển thị dữ liệu của trang hiện tại."""
    global current_page, total_pages

    if edited_data.empty:
        messagebox.showinfo("Thông báo", "Không có dữ liệu để hiển thị.")
        return

    # Tính toán số trang
    total_pages = (len(edited_data) + rows_per_page - 1) // rows_per_page

    if total_pages == 0:
        total_pages = 1  # Đảm bảo luôn có ít nhất 1 trang

    # Kiểm tra nếu trang nằm trong giới hạn
    if page < 0 or page >= total_pages:
        return

    # Xóa dữ liệu cũ trong Treeview
    tree.delete(*tree.get_children())

    # Lấy dữ liệu cho trang hiện tại
    start_index = page * rows_per_page
    end_index = min(start_index + rows_per_page, len(edited_data))
    page_data = edited_data.iloc[start_index:end_index]

    # Chèn dữ liệu vào Treeview
    for _, row in page_data.iterrows():
        tree.insert("", "end", values=[_+1] + list(row))
        
    # Cập nhật chỉ số trang hiện tại
    current_page = page

    # Cập nhật nhãn số trang
    page_label.config(text=f"{current_page + 1} / {total_pages}")

def show_dropdown_menu(event, button_name):
        """Hiển thị menu bật xuống phía dưới nút."""
        # Xóa các mục cũ trong menu
        popup_menu.delete(0, "end")

        # Thêm mục menu tùy theo button_name
        if button_name == "Xem":
            popup_menu.add_command(label="Hiển thị n dòng đầu tiên", 
                                   command=lambda: show_n_rows(simpledialog.askinteger("Input", "Nhập số dòng muốn hiển thị:")))
            popup_menu.add_command(label="Hiển thị n cột đầu tiên", command=lambda: show_n_columns(simpledialog.askinteger("Input", "Nhập số cột muốn hiển thị:")))
            popup_menu.add_command(label="Hiển thị các cột cụ thể",
                                    command=show_specific_columns)
            popup_menu.add_command(label="Hiển thị các dòng cụ thể",
                                   command=show_specific_rows)
            popup_menu.add_command(label="Hiển thị các cột với số hàng cụ thể",
                                   command=show_specific_columns_with_rows)

        elif button_name == "Sắp Xếp":
            popup_menu.add_command(label="Sắp xếp giá trị tăng dần của một cột",
                        command=lambda: sort_data(order="asc"))
            popup_menu.add_command(label="Sắp xếp giá trị giảm dần của một cột",
                        command=lambda: sort_data(order="desc"))
        elif button_name == "Lọc":
            Loccon_menu = tk.Menu(popup_menu, tearoff=0)
            Loccon_menu.add_command(label="Lọc một giá trị duy nhất", command=filter_by_single_value)
            Loccon_menu.add_command(label="Lọc nhiều giá trị", command=filter_by_multiple_values)
            Loccon_menu.add_command(label="Lọc giá trị trong phạm vi", command=filter_by_range)
            popup_menu.add_cascade(label="Lọc theo thuộc tính có giá trị số", menu=Loccon_menu)
            
            popup_menu.add_command(label="Lọc theo thuộc tính có giá trị chữ", command=filter_by_text)

        # Hiển thị menu ngay dưới nút nhấn
        popup_menu.post(event.x_root, event.y_root)

def show_recent_files():
    # Xóa nội dung hiện tại trong phần content_frame
    for widget in content_frame.winfo_children():
        widget.destroy()

    # Title for recent files
    title_frame = tk.Frame(content_frame, bg="#f5e7df")
    title_frame.pack(fill=tk.X, padx=10, pady=5)

    ViewS = tk.Button(title_frame, text="Xem", bg="#F18F01", font=("Arial", 14, "bold"), fg="#333333", width=10)
    ViewS.pack(side=tk.LEFT)
    SortS = tk.Button(title_frame, text="Sắp Xếp", bg="#35CE8D", font=("Arial", 14, "bold"), fg="#333333", width=10)
    SortS.pack(side=tk.LEFT, padx=5)
    FilterS = tk.Button(title_frame, text="Lọc", bg="#E16F7C", font=("Arial", 14, "bold"), fg="#333333", width=10)
    FilterS.pack(side=tk.LEFT, padx=5)
    tk.Button(title_frame, text="Cập Nhật", bg="#6A69FF", font=("Arial", 14, "bold"), fg="#FFFFFF", width=10, command=update_csv).pack(side=tk.RIGHT)
    tk.Button(title_frame, text="Xóa", bg="#89043D", font=("Arial", 14, "bold"), fg="#FFFFFF", width=10, command=delete_selected_rows).pack(side=tk.RIGHT, padx=5)
    tk.Button(title_frame, text="Thêm", bg="#1C448E", font=("Arial", 14, "bold"), fg="#FFFFFF", width=10, command=add_data).pack(side=tk.RIGHT, padx=5)
    tk.Button(title_frame, text="Tải lại", bg="#56CBF9", font=("Arial", 14, "bold"), fg="#FFFFFF", width=10, command=show_recent_files).pack(side=tk.RIGHT, padx=5)

    global popup_menu
    popup_menu = tk.Menu(content_frame, tearoff=0)

    ViewS.bind("<Button-1>", lambda event: show_dropdown_menu(event, "Xem"))
    SortS.bind("<Button-1>", lambda event: show_dropdown_menu(event, "Sắp Xếp"))
    FilterS.bind("<Button-1>", lambda event: show_dropdown_menu(event, "Lọc"))   

    page_frame = tk.Frame(content_frame, bg="#FFFFFF")
    page_frame.pack(fill=tk.X, padx=10, pady=5)

    # Nút điều hướng phân trang
    navigation_frame = tk.Frame(page_frame, bg="#f5e7df")
    navigation_frame.pack(fill="x", pady=10)

    # Nút điều hướng
    prev = tk.Button(navigation_frame, text="Trước", bg="#121211", font=("Arial", 14, "bold"), fg="#FFFFFF",
              command=lambda: update_treeview(current_page - 1))
    prev.pack(side=tk.LEFT, padx=5)
    next = tk.Button(navigation_frame, text="Tiếp", bg="#121211", font=("Arial", 14, "bold"), fg="#FFFFFF",
              command=lambda: update_treeview(current_page + 1))
    next.pack(side=tk.RIGHT, padx=5)

    # Nhãn hiển thị số trang
    global page_label, edited_data
    page_label = tk.Label(navigation_frame, text="", bg="#f5e7df", font=("Arial", 14), fg="#333333")
    page_label.pack(padx=10, anchor='center')

    edited_data = pd.read_csv(file_path)

    # Treeview
    global tree
    tree = ttk.Treeview(
        content_frame,
        columns=["STT"] + list(edited_data.columns),
        show="headings",
        height=7,
    )
    tree.heading("STT", text="STT")
    tree.column("STT", width=50, anchor="center")

    # Configure Treeview columns
    for col in edited_data.columns:
        tree.heading(col, text=col)
        column_width = max(len(col) * 10, 100)
        tree.column(col, anchor="w", width=column_width)

    # Style configuration for Treeview
    style = ttk.Style()
    style.configure("Treeview", font=("Arial", 10), rowheight=30)
    style.configure("Treeview.Heading", font=("Arial", 11, "bold"))
    style.map("Treeview", background=[("selected", "#EAF6FF")], foreground=[("selected", "#000")])

    tree.bind("<Double-1>", edit_cell)

    vertical_scrollbar = ttk.Scrollbar(content_frame, orient="vertical", command=tree.yview)
    vertical_scrollbar.pack(side="right", fill="y")

    horizontal_scrollbar = ttk.Scrollbar(content_frame, orient="horizontal", command=tree.xview)
    horizontal_scrollbar.pack(side="bottom", fill="x")

    # Kết nối thanh cuộn với Treeview
    tree.configure(yscrollcommand=vertical_scrollbar.set, xscrollcommand=horizontal_scrollbar.set)
    tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

    global total_pages, current_page
    current_page = 0
    rows_per_page = 200
    total_pages = (len(edited_data) + rows_per_page - 1) // rows_per_page

    update_treeview(0)

def show_chart1():
    # Xóa nội dung hiện tại trong phần content_frame
    for widget in content_frame.winfo_children():
        widget.destroy()

    title_frame2 = tk.Frame(content_frame, bg="#f5e7df")
    title_frame2.pack(fill=tk.X, padx=10, pady=5)

    tk.Button(title_frame2, text="Thống Kê Mô Tả", bg="#ffffff", fg="#000000", font=("Arial", 14, "bold"), width=15, command=show_chart1).pack(side=tk.LEFT, padx=10)
    tk.Button(title_frame2, text="PT Quan Hệ", bg="#E072A4", font=("Arial", 14, "bold"), fg="#333333", width=15, command=show_chart2).pack(side=tk.LEFT, padx=10)
    tk.Button(title_frame2, text="PT Tương Quan", bg="#FF4B3E", font=("Arial", 14, "bold"), fg="#333333", width=15, command=show_chart3).pack(side=tk.LEFT, padx=10)
    
    # Canvas để đặt các biểu đồ
    canvas = tk.Canvas(content_frame)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    # Thanh cuộn dọc
    scrollbar = ttk.Scrollbar(content_frame, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Kết nối canvas với thanh cuộn
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    # Frame trong canvas để chứa các widget
    second_frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=second_frame, anchor="nw")

    plots_and_insights = list(zip(plot_one, insight_one))

    # Thêm biểu đồ vào Frame
    for plot, insight in plots_and_insights:
        try:
            fig = plot()  # Gọi hàm vẽ biểu đồ
            canvas_chart = FigureCanvasTkAgg(fig, master=second_frame)
            canvas_chart.draw()
            widget = canvas_chart.get_tk_widget()
            widget.config(width=1300, height=700)
            widget.pack()  # Thêm khoảng cách giữa các biểu đồ

            insi = insight()
            label = tk.Label(second_frame, text=insi, font=("Arial", 10), wraplength=800, justify="left")
            label.pack(pady=10)
        except Exception as e:
            print(f"Error while plotting: {e}")

def show_chart2():
    # Xóa nội dung hiện tại trong phần content_frame
    for widget in content_frame.winfo_children():
        widget.destroy()

    title_frame2 = tk.Frame(content_frame, bg="#f5e7df")
    title_frame2.pack(fill=tk.X, padx=10, pady=5)

    tk.Button(title_frame2, text="Thống Kê Mô Tả", bg="#61C9A8", font=("Arial", 14, "bold"), fg="#333333", width=15, command=show_chart1).pack(side=tk.LEFT, padx=10)
    tk.Button(title_frame2, text="PT Quan Hệ", bg="#ffffff", fg="#000000", font=("Arial", 14, "bold"), width=15, command=show_chart2).pack(side=tk.LEFT, padx=10)
    tk.Button(title_frame2, text="PT Tương Quan", bg="#FF4B3E", font=("Arial", 14, "bold"), fg="#333333", width=15, command=show_chart3).pack(side=tk.LEFT, padx=10)

    # Canvas để đặt các biểu đồ
    canvas = tk.Canvas(content_frame)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    # Thanh cuộn dọc
    scrollbar = ttk.Scrollbar(content_frame, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Kết nối canvas với thanh cuộn
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    # Frame trong canvas để chứa các widget
    second_frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=second_frame, anchor="nw")

    # Thêm biểu đồ vào Frame
    for (plot, insight) in plots_and_insights_two:
        try:
            fig = plot()  # Gọi hàm vẽ biểu đồ
            canvas_chart = FigureCanvasTkAgg(fig, master=second_frame)
            canvas_chart.draw()
            widget = canvas_chart.get_tk_widget()
            widget.pack(pady=10)  # Thêm khoảng cách giữa các biểu đồ

            if insight is not None:
                insi = insight()
                label = tk.Label(second_frame, text=insi, font=("Arial", 10), wraplength=800, justify="left")
                label.pack(pady=10)
        except Exception as e:
            print(f"Error while plotting: {plot.__name__}")

def show_chart3():
    # Xóa nội dung hiện tại trong phần content_frame
    for widget in content_frame.winfo_children():
        widget.destroy()

    title_frame2 = tk.Frame(content_frame, bg="#f5e7df")
    title_frame2.pack(fill=tk.X, padx=10, pady=5)
    
    tk.Button(title_frame2, text="Thống Kê Mô Tả", bg="#61C9A8", font=("Arial", 14, "bold"), fg="#333333", width=15, command=show_chart1).pack(side=tk.LEFT, padx=10)
    tk.Button(title_frame2, text="PT Quan Hệ", bg="#E072A4", font=("Arial", 14, "bold"), fg="#333333", width=15, command=show_chart2).pack(side=tk.LEFT, padx=10)
    tk.Button(title_frame2, text="PT Tương Quan", bg="#ffffff", fg="#000000", font=("Arial", 14, "bold"), width=15, command=show_chart3).pack(side=tk.LEFT, padx=10)

    # Canvas để đặt các biểu đồ
    canvas = tk.Canvas(content_frame)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    # Thanh cuộn dọc
    scrollbar = ttk.Scrollbar(content_frame, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Kết nối canvas với thanh cuộn
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    # Frame trong canvas để chứa các widget
    second_frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=second_frame, anchor="nw")

    # Thêm biểu đồ vào Frame
    try:
            fig = data_visualization.heatmap()  # Gọi hàm vẽ biểu đồ
            canvas_chart = FigureCanvasTkAgg(fig, master=second_frame)
            canvas_chart.draw()
            widget = canvas_chart.get_tk_widget()
            widget.config(width=1300, height=700)
            widget.pack(fill=tk.BOTH, expand=True)
    except Exception as e:
            print(f"Error while plotting {data_visualization.heatmap.__name__}: {e}")

def main_page():
    """Hàm thiết lập giao diện chính với các nút danh mục."""
    # Header area for file categories
    categories_frame = tk.Frame(root, bg="#f5e7df")
    categories_frame.pack(fill=tk.X, padx=10, pady=10)

    # Sử dụng lưới để chia đều các nút
    categories_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)  # 4 cột với kích thước đều nhau

    for i, (category, color) in enumerate(categories):
        category_colors[category] = color
        button = tk.Button(
            categories_frame,
            text=category,
            font=("Arial", 12, "bold"),
            command=lambda c=category: show_category(c),
            bg=color,
            fg="#FFFFFF",
            relief=tk.FLAT,
            width=70,
            height=2,
        )
        button.grid(row=0, column=i, padx=10, pady=10, sticky="nsew")

        buttons[category] = button

    # Hiển thị Recent Files ban đầu
    show_category("QUẢN LÍ")

# Main application
root = tk.Tk()
root.title("File Manager")
root.geometry("900x500")
root.configure(bg="#F2F4F8")

category_colors = {}
rows_per_page = 200  # Số dòng mỗi trang

# Content frame (phần thay đổi nội dung)
content_frame = tk.Frame(root, bg="#f5e7df", bd=1, relief=tk.GROOVE)
content_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Load main page
main_page()

makecenter(root, 1000, 600)
root.mainloop()