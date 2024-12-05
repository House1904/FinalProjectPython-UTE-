import tkinter as tk
from tkinter import ttk, messagebox, simpledialog, Menu
import csv
import subprocess
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import visualization_for_GUI
import warnings
warnings.filterwarnings("ignore")

def makecenter(root, width, height):
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

# Dữ liệu bảng: Attribute và Description
attributes_data = [
    ("Hours_Studied", "Number of hours spent studying per week."),
    ("Attendance", "Percentage of classes attended."),
    ("Parental_Involvement", "Level of parental involvement in education (Low, Medium, High)."),
    ("Access_to_Resources", "Availability of educational resources (Low, Medium, High)."),  
    ("Extracurricular_Activities", "Participation in extracurricular activities (Yes, No)."),
    ("Sleep_Hours", "Average number of hours of sleep per night."),    
    ("Previous_Scores", "Scores from previous exams."),
    ("Motivation_Level", "Student's level of motivation (Low, Medium, High)."),    
    ("Internet_Access", "Availability of internet access (Yes, No)."),
    ("Tutoring_Sessions", "Number of tutoring sessions attended per month."),
    ("Family_Income", "Family income level (Low, Medium, High)."),
    ("Teacher_Quality", "Quality of the teachers (Low, Medium, High)"),
    ("School_Type", "Type of school attended (Public, Private)."),
    ("Peer_Influence", "Influence of peers on academic performance (Positive, Neutral, Negative)."),
    ("Physical_Activity", "Average number of hours of physical activity per week"),
    ("Learning_Disabilities", "Presence of learning disabilities (Yes, No)"),
    ("Parental_Education_Level", "Highest education level of parents (High School, College, Postgraduate)"),
    ("Distance_from_Home", "Distance from home to school (Near, Moderate, Far)."),
    ("Gender", "Gender of the student (Male, Female)."),
    ("Exam_Score", "Final exam score.")
]

text_columns = ["Parental_Involvement", "Access_to_Resources",
                        "Extracurricular_Activities", "Motivation_Level",
                        "Internet_Access", "Family_Income", "Teacher_Quality",
                        "School_Type", "Peer_Influence","Learning_Disabilities", 
                        "Parental_Education_Level", "Distance_from_Home", "Gender"]

numeric_columns = ["Hours_Studied", "Attendance", "Sleep_Hours",
                    "Previous_Scores", "Tutoring_Sessions", "Physical_Activity", "Exam_Score"]

# File CSV chứa dữ liệu câu trả lời
csv_file = "data_source\\cleaned_data.csv"

# Hàm đọc dữ liệu từ file CSV
def load_csv_data(file_path):
    data = []
    headers = []
    try:
        with open(file_path, mode="r", encoding="utf-8") as file:
            reader = csv.reader(file)
            headers = next(reader)  # Lấy tiêu đề cột
            for row in reader:
                data.append(row)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    return headers, data

headers, data = load_csv_data(csv_file)

# Hàm ghi dữ liệu vào file CSV
def write_csv_data(file_path, headers, data):
    try:
        with open(file_path, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            writer.writerows(data)
    except Exception as e:
        print(f"Error writing to {file_path}: {e}")

# Hàm hiển thị dữ liệu trong bảng với phân trang
def display_page(tree, data, page, rows_per_page):
    # Xóa dữ liệu cũ trong Treeview
    for row in tree.get_children():
        tree.delete(row)

    # Tính chỉ số bắt đầu và kết thúc
    start_idx = page * rows_per_page
    end_idx = min(start_idx + rows_per_page, len(data))
    page_data = data[start_idx:end_idx]

    # Thêm dữ liệu vào bảng
    for i, row in enumerate(page_data, start=start_idx + 1):
        tree.insert("", "end", values=[i] + row)

def convert_to_number(value):
            """Chuyển đổi giá trị sang số (float). Nếu không thể chuyển đổi, trả về giá trị lớn để đưa xuống cuối."""
            try:
                return float(value)
            except ValueError:
                return float('inf')  # Giá trị lớn để đưa các giá trị không hợp lệ xuống cuối

# Tạo giao diện ứng dụng
def create_gui():
    # Tạo cửa sổ chính
    root = tk.Tk()
    root.title("Survey Application")
   
    # Tạo Notebook với các tab
    notebook = ttk.Notebook(root)
    notebook.pack(fill="both", expand=True)

    # Tab 1: Bảng câu hỏi
    questions_tab = ttk.Frame(notebook)
    notebook.add(questions_tab, text="Data Description")

    # Tab 2: Câu trả lời
    answers_tab = ttk.Frame(notebook)
    notebook.add(answers_tab, text="View Answers")

    # Tab 3: Bảng quản lý
    manage_tab = ttk.Frame(notebook)
    notebook.add(manage_tab, text="Manage Data")

    # Tab 4: Bảng biểu đồ
    chart_tab = ttk.Frame(notebook)
    notebook.add(chart_tab, text="Chart")

    # ===== Tab 1: Bảng câu hỏi =====
    table_frame = ttk.LabelFrame(questions_tab, text="Description")
    table_frame.pack(fill="both", expand=True, padx=10, pady=10)

    # Sử dụng Treeview để hiển thị bảng
    attributes_table = ttk.Treeview(table_frame, columns=("Attribute", "Description"), show="headings", height=15)
    attributes_table.heading("Attribute", text="Attribute")
    attributes_table.heading("Description", text="Description")
    attributes_table.column("Attribute", width=200, anchor="w")
    attributes_table.column("Description", width=500, anchor="w")
    attributes_table.pack(fill="both", expand=True, padx=10, pady=10)

    # Thêm dữ liệu vào bảng
    for attr, desc in attributes_data:
        attributes_table.insert("", "end", values=(attr, desc))

    # ===== Tab 2: Hiển thị câu trả lời =====
    def filter_by_text():
        """Lọc dữ liệu theo giá trị chữ."""
        # Hiển thị danh sách cột có giá trị chữ
        column_info = "\n".join([f"{idx + 1}. {header}" for idx, header in enumerate(text_columns)])
        input_message = f"Các cột có sẵn:\n{column_info}\n\nNhập chỉ số các cột cần in ra, cách nhau bằng dấu phẩy:"
        
        # Hộp thoại nhập
        column_indices_str = simpledialog.askstring("Input", input_message)
        if not column_indices_str:
            messagebox.showwarning("Invalid Input", "No indices entered!")
            return

        try:
            # Chuyển đổi chỉ số cột nhập vào thành danh sách số nguyên
            column_indices = sorted(set(int(idx.strip()) - 1 for idx in column_indices_str.split(",")))  # Chỉ số bắt đầu từ 0
        except ValueError:
            messagebox.showerror("Error", "Invalid column indices! Please enter valid numbers.")
            return

        # Kiểm tra tính hợp lệ của chỉ số
        invalid_indices = [idx for idx in column_indices if idx < 0 or idx >= len(headers)]
        if invalid_indices:
            messagebox.showerror(
                "Error", f"Invalid column indices: {', '.join(str(idx + 1) for idx in invalid_indices)}"
            )
            return

        # Lấy tên cột từ chỉ số
        selected_columns = [text_columns[idx] for idx in column_indices]

        # Tạo cửa sổ để nhập giá trị lọc cho từng cột
        filter_window = tk.Toplevel(root)
        filter_window.title("Enter Filter Values for Columns")
        filter_window.geometry("400x400")
        filter_window.grab_set()  # Modal window

        filter_comboboxes = {}
        for idx, col in enumerate(selected_columns):
            label = ttk.Label(filter_window, text=f"Value for {col}:")
            label.grid(row=idx, column=0, padx=10, pady=5, sticky="w")

            # Lấy các giá trị duy nhất trong cột từ dữ liệu
            column_index = headers.index(col)
            unique_values = sorted(set(row[column_index] for row in data if row[column_index]))  # Các giá trị duy nhất

            # Tạo Combobox
            combobox = ttk.Combobox(filter_window, values=unique_values, state="readonly", width=20)
            combobox.grid(row=idx, column=1, padx=10, pady=5, sticky="w")
            filter_comboboxes[col] = combobox

        def apply_filter():
            filter_values = {}
            for col, entry in filter_comboboxes.items():
                value = entry.get().strip()
                if value:  # Chỉ lưu giá trị đã nhập
                    filter_values[col] = value

            if not filter_values:
                raise ValueError("No filter values entered for any column!")

            # Lọc dữ liệu
            filtered_data = []
            column_indices_map = {col: headers.index(col) for col in filter_values.keys()}
            for row in data:
                match = all(row[column_indices_map[col]] == value for col, value in filter_values.items())
                if match:
                    filtered_data.append(row)

            if not filtered_data:
                messagebox.showinfo("Fail", "No matching rows found for the specified filters.")
                return

            # Cập nhật bảng với dữ liệu đã lọc
            tree.delete(*tree.get_children())
            for idx, row in enumerate(filtered_data, start=1):
                tree.insert("", "end", values=[idx] + row)

            filter_window.destroy()
            messagebox.showinfo("Success", "Filtered rows by value in columns")

        # Nút OK và Cancel
        button_frame = ttk.Frame(filter_window)
        button_frame.grid(row=len(selected_columns), columnspan=2, pady=10)

        ok_button = ttk.Button(button_frame, text="OK", command=apply_filter)
        ok_button.pack(side="left", padx=5)

        cancel_button = ttk.Button(button_frame, text="Cancel", command=filter_window.destroy)
        cancel_button.pack(side="left", padx=5)

    def filter_by_single_value():
        """Lọc dữ liệu theo một giá trị duy nhất trong một cột."""
        column_info = "\n".join([f"{idx + 1}. {header}" for idx, header in enumerate(numeric_columns)])
        input_message = f"Các cột có sẵn:\n{column_info}\n\nNhập chỉ số các cột cần in ra, cách nhau bằng dấu phẩy:"
        
        # Hộp thoại nhập
        column_indices_str = simpledialog.askstring("Input", input_message)
        if not column_indices_str:
            messagebox.showwarning("Invalid Input", "No indices entered!")
            return

        try:
            # Lấy chỉ số cột (1-based) và chuyển sang 0-based
            column_index = int(column_indices_str.strip()) - 1
            if column_index < 0 or column_index >= len(numeric_columns):
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Invalid column index! Please enter a valid number.")
            return

        # Lấy tên cột tương ứng
        column_name = numeric_columns[column_index]

        try:
            filter_value = float(simpledialog.askstring("Input", f"Enter value to filter in column '{column_name}':"))
        except ValueError:
            messagebox.showerror("Error", "Invalid numeric value entered!")
            return

        # Lọc dữ liệu
        column_index = headers.index(column_name)
        filtered_data = [row for row in data if convert_to_number(row[column_index]) == filter_value]

        # Cập nhật bảng với dữ liệu đã lọc
        update_treeview(filtered_data)
        messagebox.showinfo("Success", f"Filtered rows where '{column_indices_str}' equals {filter_value}.")

    def filter_by_multiple_values():
        """Lọc dữ liệu theo nhiều giá trị trong một cột."""
        column_info = "\n".join([f"{idx + 1}. {header}" for idx, header in enumerate(numeric_columns)])
        input_message = f"Các cột có sẵn:\n{column_info}\n\nNhập chỉ số các cột cần in ra, cách nhau bằng dấu phẩy:"
        
        # Hộp thoại nhập
        column_indices_str = simpledialog.askstring("Input", input_message)
        if not column_indices_str:
            messagebox.showwarning("Invalid Input", "No indices entered!")
            return

        try:
            # Lấy chỉ số cột (1-based) và chuyển sang 0-based
            column_index = int(column_indices_str.strip()) - 1
            if column_index < 0 or column_index >= len(numeric_columns):
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Invalid column index! Please enter a valid number.")
            return

        # Lấy tên cột tương ứng
        column_name = numeric_columns[column_index]
        try:
            filter_values = list(map(float, simpledialog.askstring(
                "Input", f"Enter values to filter in column '{column_name}' (comma-separated):").split(',')))
        except ValueError:
            messagebox.showerror("Error", "Invalid numeric values entered!")
            return

        # Lọc dữ liệu
        column_index = headers.index(column_name)
        filtered_data = [row for row in data if convert_to_number(row[column_index]) in filter_values]

        # Cập nhật bảng với dữ liệu đã lọc
        update_treeview(filtered_data)

    def filter_by_range():
        """Lọc dữ liệu trong phạm vi giá trị của một cột."""
        column_info = "\n".join([f"{idx + 1}. {header}" for idx, header in enumerate(numeric_columns)])
        input_message = f"Các cột có sẵn:\n{column_info}\n\nNhập chỉ số các cột cần in ra, cách nhau bằng dấu phẩy:"
        
        # Hộp thoại nhập
        column_indices_str = simpledialog.askstring("Input", input_message)
        if not column_indices_str:
            messagebox.showwarning("Invalid Input", "No indices entered!")
            return

        try:
            # Lấy chỉ số cột (1-based) và chuyển sang 0-based
            column_index = int(column_indices_str.strip()) - 1
            if column_index < 0 or column_index >= len(numeric_columns):
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Invalid column index! Please enter a valid number.")
            return

        # Lấy tên cột tương ứng
        column_name = numeric_columns[column_index]

        try:
            min_value = float(simpledialog.askstring("Input", f"Enter minimum value for column '{column_name}':"))
            max_value = float(simpledialog.askstring("Input", f"Enter maximum value for column '{column_name}':"))
        except ValueError:
            messagebox.showerror("Error", "Invalid numeric values entered!")
            return

        # Lọc dữ liệu
        column_index = headers.index(column_name)
        filtered_data = [row for row in data if min_value <= convert_to_number(row[column_index]) <= max_value]

        # Cập nhật bảng với dữ liệu đã lọc
        update_treeview(filtered_data)
    def update_treeview(filtered_data):
        """Cập nhật bảng Treeview với dữ liệu đã lọc."""
        tree.delete(*tree.get_children())  # Xóa dữ liệu cũ
        for idx, row in enumerate(filtered_data, start=1):
            tree.insert("", "end", values=[idx] + row)

    def ask_numeric_column():
        """Hiển thị cửa sổ với Combobox để người dùng chọn cột muốn sắp xếp."""
        sort_window = tk.Toplevel(root)
        sort_window.title("Select Column")
        sort_window.geometry("300x150")
        sort_window.grab_set()  # Đặt cửa sổ ở chế độ modal (ngăn người dùng tương tác với cửa sổ khác)

        # Label hướng dẫn
        label = ttk.Label(sort_window, text="Select a column:")
        label.pack(pady=10)

        # Combobox để chọn cột
        selected_column = tk.StringVar()
        combobox2 = ttk.Combobox(sort_window, textvariable=selected_column, state="readonly", values=numeric_columns)
        combobox2.pack(pady=5)
        combobox2.set(numeric_columns[0])  # Giá trị mặc định

        # Xử lý khi nhấn nút OK
        def confirm_selection():
            sort_window.destroy()  # Đóng cửa sổ

        # Nút OK và Cancel
        button_frame = ttk.Frame(sort_window)
        button_frame.pack(pady=10)

        ok_button = ttk.Button(button_frame, text="OK", command=confirm_selection)
        ok_button.pack(side="left", padx=5)

        cancel_button = ttk.Button(button_frame, text="Cancel", command=sort_window.destroy)
        cancel_button.pack(side="left", padx=5)

        sort_window.wait_window()  # Chờ người dùng đóng cửa sổ
        return selected_column.get()
    
    def ask_text_column():
        """Hiển thị cửa sổ với Combobox để người dùng chọn cột muốn sắp xếp."""
        sort_window = tk.Toplevel(root)
        sort_window.title("Select Column")
        sort_window.geometry("300x150")
        sort_window.grab_set()  # Đặt cửa sổ ở chế độ modal (ngăn người dùng tương tác với cửa sổ khác)

        # Label hướng dẫn
        label = ttk.Label(sort_window, text="Select a column:")
        label.pack(pady=10)

        # Combobox để chọn cột
        selected_column = tk.StringVar()
        combobox2 = ttk.Combobox(sort_window, textvariable=selected_column, state="readonly", values=text_columns)
        combobox2.pack(pady=5)
        combobox2.set(text_columns[0])  # Giá trị mặc định

        # Xử lý khi nhấn nút OK
        def confirm_selection():
            sort_window.destroy()  # Đóng cửa sổ

        # Nút OK và Cancel
        button_frame = ttk.Frame(sort_window)
        button_frame.pack(pady=10)

        ok_button = ttk.Button(button_frame, text="OK", command=confirm_selection)
        ok_button.pack(side="left", padx=5)

        cancel_button = ttk.Button(button_frame, text="Cancel", command=sort_window.destroy)
        cancel_button.pack(side="left", padx=5)

        sort_window.wait_window()  # Chờ người dùng đóng cửa sổ
        return selected_column.get()

    def sort_data(order="asc"):
        """Hàm sắp xếp dữ liệu tăng dần hoặc giảm dần.""" 
        # Hiển thị cửa sổ hỏi người dùng muốn sắp xếp cột nào
        column_to_sort = ask_numeric_column()  # Hiển thị cửa sổ chọn cột
        if not column_to_sort:  # Nếu người dùng hủy, không làm gì
            return
        
        # Xác định chỉ số cột
        if column_to_sort not in headers:
            messagebox.showerror("Error", f"Invalid column name: {column_to_sort}")
            return
        column_index = headers.index(column_to_sort)

        # Sắp xếp dữ liệu
        try:
            if order == "asc":
                data_with_index = [(idx + 1, row) for idx, row in enumerate(data)]  # Lưu chỉ số gốc
                sorted_data = sorted(data_with_index, key=lambda x: convert_to_number(x[1][column_index]))  # Sắp xếp
            else:
                data_with_index = [(idx + 1, row) for idx, row in enumerate(data)]  # Lưu chỉ số gốc
                sorted_data = sorted(data_with_index, key=lambda x: convert_to_number(x[1][column_index]), reverse=True)  # Sắp xếp

        except ValueError:
            messagebox.showerror("Error", f"Cannot sort column '{column_to_sort}' due to invalid data!")
            return

        # Cập nhật lại bảng
        tree.delete(*tree.get_children())  # Xóa dữ liệu cũ

        for idx, (original_index, row) in enumerate(sorted_data, start=1):
            tree.insert("", "end", values=[original_index] + row)

        # Thông báo thành công
        messagebox.showinfo("Success", f"Data sorted by '{column_to_sort}' in {'ascending' if order == 'asc' else 'descending'} order!")

    def show_n_rows(n):
        """Hiển thị n dòng đầu tiên."""
        if n > len(data) or n < 1:
            messagebox.showerror("Giá trị không hợp lệ", f"Vui lòng nhập số trong khoảng 1 -> {len(data)}!")
            return

        tree.delete(*tree.get_children())  # Xóa dữ liệu cũ
        for idx, row in enumerate(data[:n], start=1):  # Lấy n dòng đầu tiên
            tree.insert("", "end", values=[idx] + row)
        messagebox.showinfo("Success", f"Hiển thị từ dòng 1 đến {n}")
    
    def show_n_columns(n):
        """Hiển thị n cột đầu tiên."""
        if n < 1 or n > len(headers):
            messagebox.showerror("Error", "Please enter a valid number of columns!")
            return
        
        tree["columns"] = ["STT"] + headers[:n]  # Cập nhật cột hiển thị
        tree.heading("STT", text="STT")
        tree.column("STT", width=50, anchor="center")

        for header in headers[:n]:
            tree.heading(header, text=header)
            column_width_n = max(len(header) * 8, 10)
            tree.column(header, width=column_width_n, anchor="w")

        tree.delete(*tree.get_children())  # Xóa dữ liệu cũ
        for idx, row in enumerate(data, start=1):
            tree.insert("", "end", values=[idx] + row[:n])  # Lấy n cột đầu tiên
        messagebox.showinfo("Success", f"Displayed the first {n} columns.")
    
    def show_specific_columns():
        """Hiển thị các cột cụ thể."""
        column_info = "\n".join([f"{idx + 1}. {header}" for idx, header in enumerate(headers)])
        input_message = f"Các cột có sẵn:\n{column_info}\n\nNhập chỉ số các cột cần in ra, cách nhau bằng dấu phẩy:"
        
        # Hộp thoại nhập
        column_indices_str = simpledialog.askstring("Input", input_message)
        if not column_indices_str:
            messagebox.showwarning("Invalid Input", "No indices entered!")
            return

        try:
            # Chuyển đổi chỉ số cột nhập vào thành danh sách số nguyên
            column_indices = sorted(set(int(idx.strip()) - 1 for idx in column_indices_str.split(",")))  # Chỉ số bắt đầu từ 0
        except ValueError:
            messagebox.showerror("Error", "Invalid column indices! Please enter valid numbers.")
            return

        # Kiểm tra tính hợp lệ của chỉ số
        invalid_indices = [idx for idx in column_indices if idx < 0 or idx >= len(headers)]
        if invalid_indices:
            messagebox.showerror(
                "Error", f"Invalid column indices: {', '.join(str(idx + 1) for idx in invalid_indices)}"
            )
            return

        # Lấy tên cột từ chỉ số
        selected_columns = [headers[idx] for idx in column_indices]
        
        tree["columns"] = ["STT"] + selected_columns  # Cập nhật cột hiển thị
        tree.heading("STT", text="STT")
        tree.column("STT", width=50, anchor="center")
        
        for col in selected_columns:
            tree.heading(col, text=col)
            tree.column(col, width=150, anchor="center")
        
        tree.delete(*tree.get_children())  # Xóa dữ liệu cũ
        
        for idx, row in enumerate(data, start=1):
            selected_columns = [row[i] for i in column_indices]
            tree.insert("", "end", values=[idx] + selected_columns)
        
    def show_specific_columns_with_rows():
        """Hiển thị các cột cụ thể với số hàng."""
        input_window = tk.Toplevel(root)
        input_window.title("Select Columns and Rows")
        input_window.geometry("400x550")
        input_window.grab_set()

        # Hiển thị danh sách chỉ mục và tên cột
        column_info = "\n".join([f"{idx + 1}. {header}" for idx, header in enumerate(headers)])
        instructions = ttk.Label(
            input_window, 
            text=f"Các cột có sẵn:\n{column_info}\n"
        )
        instructions.pack(pady=10)

        # Frame chứa các Entry
        entry_frame = ttk.Frame(input_window)
        entry_frame.pack(pady=10)

        # Entry nhập chỉ mục cột
        column_label = ttk.Label(entry_frame, text="Nhập chỉ số các cột cần in ra, cách nhau bằng dấu phẩy:")
        column_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        column_entry = ttk.Entry(entry_frame, width=25)
        column_entry.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        # Entry nhập số hàng
        rows_label = ttk.Label(entry_frame, text="Nhập số hàng muốn hiển thị:")
        rows_label.grid(row=2, column=0, sticky="w")
        rows_entry = ttk.Entry(entry_frame, width=25)
        rows_entry.grid(row=3, column=0, sticky='w')

        def confirm_selection():
            """Xử lý khi người dùng nhấn OK."""
            try:
                # Lấy chỉ mục cột
                column_indices = sorted(set(int(idx.strip()) - 1 for idx in column_entry.get().split(",")))

                # Lấy số hàng
                num_rows = int(rows_entry.get())
                if num_rows < 1:
                    raise ValueError("Number of rows must be greater than 0!")

                # Kiểm tra chỉ số hợp lệ
                invalid_indices = [idx for idx in column_indices if idx < 0 or idx >= len(headers)]
                if invalid_indices:
                    raise ValueError(f"Invalid column indices: {', '.join(str(idx + 1) for idx in invalid_indices)}")

                # Lấy tên cột từ chỉ số
                selected_columns = [headers[idx] for idx in column_indices]

                # Hiển thị cột và số hàng trong Treeview
                tree["columns"] = ["STT"] + selected_columns  # Cập nhật cột hiển thị
                tree.heading("STT", text="STT")
                tree.column("STT", width=50, anchor="center")
                for col in selected_columns:
                    tree.heading(col, text=col)
                    tree.column(col, width=150, anchor="center")
                tree.delete(*tree.get_children())  # Xóa dữ liệu cũ
                for idx, row in enumerate(data[:num_rows], start=1):  # Lấy num_rows đầu tiên
                    selected_data = [row[i] for i in column_indices]
                    tree.insert("", "end", values=[idx] + selected_data)

                # Đóng cửa sổ và thông báo thành công
                input_window.destroy()
                messagebox.showinfo("Success", f"Displayed columns {', '.join(selected_columns)} with the first {num_rows} rows.")
            except ValueError as e:
                messagebox.showerror("Error", f"Invalid input: {e}")

        # Nút OK và Cancel
        button_frame = ttk.Frame(input_window)
        button_frame.pack(pady=10)

        ok_button = ttk.Button(button_frame, text="OK", command=confirm_selection)
        ok_button.pack(side="left", padx=5)

        cancel_button = ttk.Button(button_frame, text="Cancel", command=input_window.destroy)
        cancel_button.pack(side="left", padx=5)

    def ask_row_indices():
        """Hiển thị cửa sổ để người dùng nhập chỉ số bắt đầu và kết thúc."""
        indices_window = tk.Toplevel(root)
        indices_window.title("Enter Row Indices")
        indices_window.geometry("300x200")
        indices_window.grab_set()  # Đặt cửa sổ modal

        # Label hướng dẫn
        label = ttk.Label(indices_window, text="Enter the row range (1-based):")
        label.pack(pady=10)

        # Frame chứa các Entry
        entry_frame = ttk.Frame(indices_window)
        entry_frame.pack(pady=10)

        # Entry cho chỉ số bắt đầu
        start_label = ttk.Label(entry_frame, text="Start Index:")
        start_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        start_entry = ttk.Entry(entry_frame, width=10)
        start_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        # Entry cho chỉ số kết thúc
        end_label = ttk.Label(entry_frame, text="End Index:")
        end_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        end_entry = ttk.Entry(entry_frame, width=10)
        end_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        # Biến lưu kết quả
        result = {"start_index": None, "end_index": None}

        def confirm_selection():
            """Xác nhận lựa chọn và đóng cửa sổ."""
            try:
                start_index = int(start_entry.get())
                end_index = int(end_entry.get())
                if start_index < 1 or end_index < start_index:  # Kiểm tra tính hợp lệ
                    raise ValueError("Invalid range")
                result["start_index"] = start_index
                result["end_index"] = end_index
                indices_window.destroy()
            except ValueError:
                messagebox.showerror("Error", "Please enter valid numeric indices!")

        # Nút OK và Cancel
        button_frame = ttk.Frame(indices_window)
        button_frame.pack(pady=10)

        ok_button = ttk.Button(button_frame, text="OK", command=confirm_selection)
        ok_button.pack(side="left", padx=5)

        cancel_button = ttk.Button(button_frame, text="Cancel", command=indices_window.destroy)
        cancel_button.pack(side="left", padx=5)

        indices_window.wait_window()  # Chờ cửa sổ đóng
        return result["start_index"], result["end_index"]

    def show_specific_rows():
        """Hiển thị các dòng mong muốn."""
        start_index, end_index = ask_row_indices()

        if start_index is None or end_index is None:
            messagebox.showinfo("Cancelled", "Operation cancelled by user.")

        if end_index > len(data):  # Đảm bảo không vượt quá số dòng trong dữ liệu
            messagebox.showerror("Error", f"End index exceeds the number of rows ({len(data)}).")
            return

        # Hiển thị các dòng từ start_index đến end_index
        tree.delete(*tree.get_children())  # Xóa dữ liệu cũ
        for idx, row in enumerate(data[start_index - 1:end_index], start=start_index):  # 1-based index
            tree.insert("", "end", values=[idx] + row)

        messagebox.showinfo("Success", f"Displayed rows {start_index} to {end_index}.")

    # Tạo thanh Menu
    menu_frame = tk.Frame(answers_tab, bg="lightgrey")
    menu_frame.pack(fill="x", pady=5) 
    menu = Menu(menu_frame, tearoff=0)

    # Menu 1: Xem
    Xem_menu = Menu(menu, tearoff=0)
    Xem_menu.add_command(label="Hiển thị n dòng đầu tiên", 
                        command=lambda: show_n_rows(simpledialog.askinteger("Input", "Nhập số dòng muốn hiển thị:")))
    Xem_menu.add_command(label="Hiển thị n cột đầu tiên",
                        command=lambda: show_n_columns(simpledialog.askinteger("Input", "Nhập số cột muốn hiển thị:")))
    Xem_menu.add_command(label="Hiển thị các cột cụ thể",
                        command=show_specific_columns)
    Xem_menu.add_command(label="Hiển thị các dòng cụ thể",
                        command=show_specific_rows)
    Xem_menu.add_command(label="Hiển thị các cột với số hàng cụ thể",
                        command=show_specific_columns_with_rows)

    # Menu 2: Sắp xếp
    SXep_menu = Menu(menu, tearoff=0)
    SXep_menu.add_command(label="Sắp xếp giá trị tăng dần của một cột",
                        command=lambda: sort_data(order="asc"))
    SXep_menu.add_command(label="Sắp xếp giá trị giảm dần của một cột",
                        command=lambda: sort_data(order="desc"))

    # Menu 3: Lọc
    Loc_menu = Menu(menu, tearoff=0)
    Loc_menu.add_command(label="Lọc theo thuộc tính có giá trị chữ", command=filter_by_text)

    # menu con của Lọc
    Loccon_menu = Menu(Loc_menu, tearoff=0)
    Loccon_menu.add_command(label="Lọc một giá trị duy nhất", command=filter_by_single_value)
    Loccon_menu.add_command(label="Lọc nhiều giá trị", command=filter_by_multiple_values)
    Loccon_menu.add_command(label="Lọc giá trị trong phạm vi", command=filter_by_range)
    Loc_menu.add_cascade(label="Lọc theo thuộc tính có giá trị số", menu=Loccon_menu)

    # Thêm các menu con vào Menu chính
    menu.add_cascade(label="Xem", menu=Xem_menu)
    menu.add_cascade(label="Sắp Xếp", menu=SXep_menu)
    menu.add_cascade(label="Lọc", menu=Loc_menu)

    # Menu Button hiển thị menu
    menubutton = ttk.Menubutton(menu_frame, text="Menu", menu=menu)
    menubutton.pack(side="left", padx=10, pady=5)
    
    table_frame = ttk.Frame(answers_tab)
    table_frame.pack(fill="both", expand=True, padx=10, pady=10)

    # Bảng hiển thị dữ liệu
    tree = ttk.Treeview(table_frame,
                        columns=["STT"] + headers,
                        show="headings",
                        height=17)
    tree.heading("STT", text="STT")
    tree.column("STT", width=50, anchor="center")

    # Thêm tiêu đề cột từ CSV
    for header in headers:
        tree.heading(header, text=header)
        # Tính độ rộng cột dựa trên độ dài tiêu đề
        column_width = max(len(header) * 8, 10)
        tree.column(header, width=column_width, anchor="w")

    # Thanh cuộn dọc
    vertical_scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=tree.yview)
    vertical_scrollbar.pack(side="right", fill="y")

    # Thanh cuộn ngang
    horizontal_scrollbar = ttk.Scrollbar(table_frame, orient="horizontal", command=tree.xview)
    horizontal_scrollbar.pack(side="bottom", fill="x")

    # Kết nối thanh cuộn với Treeview
    tree.configure(yscrollcommand=vertical_scrollbar.set, xscrollcommand=horizontal_scrollbar.set)

    tree.pack(fill="both", expand=True)

    # Thông tin phân trang
    rows_per_page = 500
    current_page = tk.IntVar(value=0)  # Biến lưu trạng thái trang hiện tại
    total_pages = (len(data) + rows_per_page - 1) // rows_per_page  # Tính tổng số trang

    # Hiển thị số trang
    page_info_label = ttk.Label(answers_tab, text=f"{current_page.get() + 1}/{total_pages}")
    page_info_label.pack()

    # Nút điều hướng phân trang
    navigation_frame = ttk.Frame(answers_tab)
    navigation_frame.pack(fill="x", pady=10)

    def update_navigation_buttons():
        """Cập nhật trạng thái của nút điều hướng."""
        prev_button["state"] = "normal" if current_page.get() > 0 else "disabled"
        next_button["state"] = "normal" if current_page.get() < total_pages - 1 else "disabled"
        page_info_label.config(text=f"{current_page.get() + 1}/{total_pages}")

    def go_to_previous_page():
        """Đi đến trang trước."""
        if current_page.get() > 0:
            current_page.set(current_page.get() - 1)
            display_page(tree, data, current_page.get(), rows_per_page)
            update_navigation_buttons()

    def go_to_next_page():
        """Đi đến trang sau."""
        if current_page.get() < total_pages - 1:
            current_page.set(current_page.get() + 1)
            display_page(tree, data, current_page.get(), rows_per_page)
            update_navigation_buttons()

    def refresh_data():
        """làm mới dữ liệu hiển thị trong bảng"""
        # Tính toán lại tổng số trang
        total_pages = (len(data) + rows_per_page - 1) // rows_per_page
        current_page.set(0)  # Reset về trang đầu tiên

        for column in tree["columns"]:
            tree.heading(column, text="")  # Xóa tiêu đề
            tree.column(column, width=0)   # Ẩn cột
        tree["columns"] = ()  # Reset cấu trúc cột
        tree.delete(*tree.get_children())  # Xóa toàn bộ dữ liệu

        tree["columns"] = ["STT"] + headers
        tree.heading("STT", text="STT")
        tree.column("STT", width=50, anchor="center")

        for header in headers:
            tree.heading(header, text=header)
            column_width = max(len(header)*8, 10)  # Sử dụng độ rộng cột ban đầu
            tree.column(header, width=column_width, anchor="w")
    
        display_page(tree, data, current_page.get(), rows_per_page)

        tree.configure(yscrollcommand=vertical_scrollbar.set, xscrollcommand=horizontal_scrollbar.set)

        # Cập nhật thông tin số trang
        page_info_label.config(text=f"{current_page.get() + 1}/{total_pages}")

        # Cập nhật trạng thái nút điều hướng
        update_navigation_buttons()

        # Thông báo làm mới thành công
        messagebox.showinfo("Success", "Data has been refreshed!")
          
    prev_button = ttk.Button(navigation_frame, text="Trang trước", command=go_to_previous_page)
    prev_button.pack(side="left", padx=5)

    refresh_button = ttk.Button(navigation_frame, text="Refresh", command=refresh_data)
    refresh_button.pack(side="left", padx=5, expand=True)

    next_button = ttk.Button(navigation_frame, text="Trang sau", command=go_to_next_page)
    next_button.pack(side="right", padx=5)

    # Hiển thị dữ liệu trang đầu tiên
    update_navigation_buttons()
    display_page(tree, data, current_page.get(), rows_per_page)

# ===== Tab 3: Quản lý dữ liệu =====
    def add_data():
        """Thêm thông tin khảo sát mới."""
        try:
            subprocess.run(["python", "SurveyForm.py"], check=True) # Gọi chương trình SurveyForm.py
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"Error running the external program: {e}")
 
    def update_data():
        row_num = selected_row_num.get()

        if row_num == -1:  # Kiểm tra nếu chưa có dòng nào được chọn
            messagebox.showwarning("No Selection", "No row has been selected for deletion.")
            return

        updated_datas = []
        errors = []

        for attribute, widget in input_widgets.items():
            value = widget.get()

            if isinstance(widget, ttk.Combobox):
                updated_datas.append(widget.get())
            elif attribute in ("Hours_Studied", "Sleep_Hours", "Attendance", "Previous_Scores", "Tutoring_Sessions", "Physical_Activity", "Exam_Score"):
                try:
                    number = float(value)
                    if number < 0:
                        errors.append(f"'{attribute}' must be a non-negative number.")
                    else:
                        updated_datas.append(widget.get())
                except ValueError:
                    errors.append(f"'{attribute}' must be a valid number.")

        # Nếu có lỗi, hiển thị thông báo và dừng xử lý
        if errors:
            messagebox.showerror("Invalid Input", "\n".join(errors))
            return

        # Kiểm tra chỉ số hợp lệ
        if row_num < 0 or row_num >= len(data):
            messagebox.showerror("Error", "Invalid row number selected.")
            return
        
        # Cập nhật dữ liệu trong danh sách attributes_data
        data[row_num - 1][0:] = updated_datas  # Chỉ cập nhật phần giá trị, không sửa "Attribute"

        # Cập nhật lại bảng
        selected_item = treeba.selection()
        treeba.item(selected_item, values=data[row_num] + updated_datas)
        
        # Lưu thay đổi vào file CSV
        write_csv_data(csv_file, headers, data)
        # Hiển thị thông báo thành công
        messagebox.showinfo("Success", "Row updated successfully!")

        display_row()
    
    def delete_data():
        """Xóa 1 hoặc nhiều hàng."""
        # Yêu cầu người dùng nhập các chỉ số dòng muốn xóa
        row_indices_str = simpledialog.askstring("Input", "Nhập chỉ số dòng cần xóa (phân cách bằng dấu phẩy:")
        if not row_indices_str:
            messagebox.showwarning("Invalid Input", "Vui lòng nhập các chỉ số dòng hợp lệ!")
            return

        try:
            # Chuyển đổi các chỉ số dòng nhập vào thành danh sách các số nguyên
            row_indices = list(map(int, row_indices_str.split(',')))
        except ValueError:
            messagebox.showwarning("Invalid Input", "Chỉ được nhập số!")
            return

        # Kiểm tra nếu chỉ số dòng hợp lệ (không vượt quá số dòng trong data)
        max_index = len(data)
        invalid_indices = [idx for idx in row_indices if idx < 1 or idx > max_index]
            
        if invalid_indices:
            messagebox.showwarning("Invalid Row Indices", f"The following indices are out of range: {', '.join(map(str, invalid_indices))}")
            return
            
        # Hiển thị các dòng được chọn trong bảng Treeba
        treeba.delete(*treeba.get_children())  # Xóa dữ liệu cũ trong bảng
        selected_rows = [data[idx - 1] for idx in row_indices]  # Lấy dữ liệu dòng được chọn
        for row in selected_rows:
            treeba.insert("", "end", values= row)

        # Hỏi người dùng xác nhận xóa
        confirm = messagebox.askyesno(
            "Confirm Deletion", 
            f"Do you want to delete the selected rows: {', '.join(map(str, row_indices))}?"
        )
        if not confirm:
            return

        # Xóa các dòng trong data và Treeview
        for idx in sorted(row_indices, reverse=True):  # Xóa từ cuối lên để tránh thay đổi chỉ số
            del data[idx - 1]  # Xóa dữ liệu khỏi data

        # Xóa tất cả dữ liệu khỏi Treeview và hiển thị lại sau khi xóa
        treeba.delete(*treeba.get_children())

        messagebox.showinfo("Success", "Deleted successfully!")
        # Cập nhật lại dữ liệu trong file CSV
        write_csv_data(csv_file, headers, data)

    # Nút điều khiển
    button_frame = ttk.Frame(manage_tab)
    button_frame.pack(fill="x", pady=10)

    add_button = ttk.Button(button_frame, text="Add Data", command=add_data)
    add_button.pack(side="left", padx=5)

    update_button = ttk.Button(button_frame, text="Update Data", command=update_data)
    update_button.pack(side="left", padx=5)

    delete_button = ttk.Button(button_frame, text="Delete Data", command=delete_data)
    delete_button.pack(side="left", padx=5)

    # Entry nhập số dòng
    input_frame = ttk.Frame(manage_tab)
    input_frame.pack(pady=10)

    row_num_label = ttk.Label(input_frame, text="Enter row number to display:")
    row_num_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

    row_num_entry = ttk.Entry(input_frame)
    row_num_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

    # Hiển thị bảng 1 dòng
    table_frameba = ttk.Frame(manage_tab)
    table_frameba.pack(fill="both", expand=True, padx=10, pady=10)

    treeba = ttk.Treeview(table_frameba,
                        columns=headers,
                        show="headings",
                        height=7)  
    for header in headers:
         treeba.heading(header, text=header)
         treeba.column(header, width=150, anchor="w")
    treeba.pack(fill="x", padx=10, pady=5)

    # Thanh cuộn ngang
    horizontal_scrollbar_ba = ttk.Scrollbar(table_frameba, orient="horizontal", command=treeba.xview)
    horizontal_scrollbar_ba.pack(side="top", fill="x")

    # Kết nối thanh cuộn với Treeview
    treeba.configure(xscrollcommand=horizontal_scrollbar_ba.set)

    selected_row_num = tk.IntVar(value=-1)  # Biến lưu trạng thái dòng được chọn (mặc định là -1)

    def display_row(event=None):
        """Hiển thị dòng dữ liệu theo số thứ tự đã nhập."""
        try:
            row_num = int(row_num_entry.get())  # Lấy số hàng người dùng nhập
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter a valid number!")
            return

        # Kiểm tra số thứ tự hàng hợp lệ
        if row_num < 1 or row_num > len(data):
            messagebox.showwarning("Invalid Row", f"Row number must be between 1 and {len(data)}.")
            return
        
        # Lưu số thứ tự dòng được chọn
        selected_row_num.set(row_num)

        # Lấy dòng dữ liệu tương ứng và hiển thị trên bảng
        treeba.delete(*treeba.get_children())  # Xóa dữ liệu cũ
        treeba.insert("", "end", values=data[row_num - 1])  # Hiển thị dòng dữ liệu

        # Hiển thị dữ liệu trong các ô nhập liệu
        row_values = data[row_num - 1]
        for header, value in zip(headers, row_values):
            widget = input_widgets.get(header)

            if isinstance(widget, ttk.Combobox):
                if value and value in widget['values']:  # Kiểm tra giá trị hợp lệ
                    widget.set(value)  # Đặt giá trị của Combobox
                else:
                    widget.set("")  # Nếu không có giá trị, để ô Combobox trống
            else:
                # Nếu widget không phải là Combobox, sử dụng Entry để hiển thị
                widget.delete(0, tk.END)
                widget.insert(0, value)

    # Hiển thị
    row_num_entry.bind("<Return>", display_row)  # Khi nhấn Enter, gọi hàm display_row()

    input_widgets = {}  # Dictionary lưu các Entry tương ứng với cột

    # Frame chứa các ô nhập liệu
    entry_frame = ttk.Frame(manage_tab)
    entry_frame.pack(fill="x", padx=10, pady=10)
        
    for i, (attribute, description) in enumerate(attributes_data):
        row = i // 5  # Tính hàng dựa trên chỉ số
        col = i % 5   # Tính cột dựa trên chỉ số

        # Nhãn cho từng ô
        label = ttk.Label(entry_frame, text=attribute)
        label.grid(row=row * 2, column=col, padx=5, pady=5, sticky="n")
        
        # Tạo các ô nhập liệu dựa trên dữ liệu
        if "Yes" in description or "Low" in description or "Male" in description or "Public" in description or "Positive" in description or "Near" in description or "High School" in description:
            options = []
            if "Yes, No" in description:
                options = ["Yes", "No"]
            elif "Low, Medium, High" in description:
                options = ["Low", "Medium", "High"]
            elif "Male, Female" in description:
                options = ["Male", "Female"]
            elif "Public, Private" in description:
                options = ["Public", "Private"]
            elif "Positive, Neutral, Negative" in description:
                options = ["Positive", "Neutral", "Negative"]
            elif "Near, Moderate, Far" in description:
                options = ["Near", "Moderate", "Far"]
            elif "High School, College, Postgraduate" in description:
                options = ["High School", "College", "Postgraduate"]

            combobox = ttk.Combobox(entry_frame, values=options, state="readonly", width=22)
            combobox.grid(row=row * 2 + 1, column=col, padx=5, pady=5, sticky="n")
            input_widgets[attribute] = combobox
        else:
            # Entry cho dữ liệu tự do
            entry = ttk.Entry(entry_frame, width=25)
            entry.grid(row=row * 2 + 1, column=col, padx=5, pady=5, sticky="n")
            input_widgets[attribute] = entry
            
    # ===== Tab 4: Bảng biểu đồ =====
    # Tạo thanh Menu
    menu_frame4 = tk.Frame(chart_tab, bg="lightgrey")
    menu_frame4.pack(fill="x", pady=5) 

    menu4 = Menu(menu_frame4, tearoff=0)

    chart_frame = tk.Frame(chart_tab)
    chart_frame.pack(side="top", fill="both", expand=True)

    label = ttk.Label(chart_frame, text="Biểu đồ sẽ hiển thị ở đây", font=50)
    label.pack(expand=True)

    def plot_on_canvas(plot_function):
        # Xóa tất cả trước khi vẽ lại
        for widget in chart_frame.winfo_children():
            widget.destroy()

        # Tạo biểu đồ mới từ hàm plot_function
        fig = plot_function()

        canvas = FigureCanvasTkAgg(fig, master=chart_frame)
        canvas.draw()
        
        cw = canvas.get_tk_widget()
        cw.config(width=1300, height=700)
        cw.pack()

    # Tạo một menu con trong menu bar
    file1_menu = tk.Menu(menu4, tearoff=0)  # tearoff=0 để không cho phép menu rời khỏi thanh menu
    file1_menu.add_command(label="Hours_Studied", command=lambda: plot_on_canvas(visualization_for_GUI.plot_hours_studied_distribution))
    file1_menu.add_command(label="Attendance", command=lambda: plot_on_canvas(visualization_for_GUI.plot_attendance_distribution))
    file1_menu.add_command(label="Parental_Involvement", command=lambda: plot_on_canvas(visualization_for_GUI.plot_parental_involvement_distribution))
    file1_menu.add_command(label="Access_to_Resources", command=lambda: plot_on_canvas(visualization_for_GUI.plot_access_to_resources_distribution))
    file1_menu.add_command(label="Extracurricular_Activities", command=lambda: plot_on_canvas(visualization_for_GUI.plot_extracurricular_activities_distribution))
    file1_menu.add_command(label="Sleep_Hours", command=lambda: plot_on_canvas(visualization_for_GUI.plot_sleep_hours_distribution))
    file1_menu.add_command(label="Previous_Scores", command=lambda: plot_on_canvas(visualization_for_GUI.plot_previous_scores_distribution))
    file1_menu.add_command(label="Motivation_Level", command=lambda: plot_on_canvas(visualization_for_GUI.plot_motivation_level_distribution))
    file1_menu.add_command(label="Internet_Access", command=lambda: plot_on_canvas(visualization_for_GUI.plot_internet_access_distribution))
    file1_menu.add_command(label="Tutoring_Sessions", command=lambda: plot_on_canvas(visualization_for_GUI.plot_tutoring_sessions_distribution))
    file1_menu.add_command(label="Family_Income	", command=lambda: plot_on_canvas(visualization_for_GUI.plot_family_income_distribution))
    file1_menu.add_command(label="Teacher_Quality", command=lambda: plot_on_canvas(visualization_for_GUI.plot_teacher_quality_distribution))
    file1_menu.add_command(label="School_Type", command=lambda: plot_on_canvas(visualization_for_GUI.plot_school_type_distribution))
    file1_menu.add_command(label="Peer_Influence", command=lambda: plot_on_canvas(visualization_for_GUI.plot_peer_influence_distribution))
    file1_menu.add_command(label="Physical_Activity	", command=lambda: plot_on_canvas(visualization_for_GUI.plot_physical_activity_distribution))
    file1_menu.add_command(label="Learning_Disabilities", command=lambda: plot_on_canvas(visualization_for_GUI.plot_learning_disabilities_distribution))
    file1_menu.add_command(label="Parental_Education_Level", command=lambda: plot_on_canvas(visualization_for_GUI.plot_parental_education_level_distribution))
    file1_menu.add_command(label="Distance_from_Home", command=lambda: plot_on_canvas(visualization_for_GUI.plot_distance_from_home_distribution))
    file1_menu.add_command(label="Gender", command=lambda: plot_on_canvas(visualization_for_GUI.plot_gender_distribution))
    file1_menu.add_command(label="Exam_Score", command=lambda: plot_on_canvas(visualization_for_GUI.plot_exam_score_distribution))
    

    file2_menu = tk.Menu(menu4, tearoff=0)  # tearoff=0 để không cho phép menu rời khỏi thanh menu
    file2_menu.add_command(label="Vẽ biểu đồ phân tán Hours Studied và Exam Score", command=lambda: plot_on_canvas(visualization_for_GUI.scatterplot_Hours_Studied_and_Exam_Score))
    file2_menu.add_command(label="Vẽ biểu đồ phân tán Attendance và Exam Score", command=lambda: plot_on_canvas(visualization_for_GUI.scatterplot_Attendance_and_Exam_Score))
    file2_menu.add_command(label="Vẽ biểu đồ phân tán Previous Scores và Exam Score", command=lambda: plot_on_canvas(visualization_for_GUI.scatterplot_Previous_Scores_and_Exam_Score))
    file2_menu.add_command(label="Xây dựng sơ đồ phân tán dựa trên các đặc điểm số (tính đến các hoạt động ngoại khóa)", command=lambda: plot_on_canvas(visualization_for_GUI.scatterplot_Numcol_and_Exam_Score_with_Extracurricular_Activities))
    file2_menu.add_command(label="Xây dựng sơ đồ phân tán dựa trên các đặc điểm số (tính đến giới tính)", command=lambda: plot_on_canvas(visualization_for_GUI.scatterplot_Numcol_and_Exam_Score_with_Gender))
    file2_menu.add_command(label="Xây dựng sơ đồ phân tán dựa trên các đặc điểm số (tính đến việc truy cập Internet)", command=lambda: plot_on_canvas(visualization_for_GUI.scatterplot_Numcol_and_Exam_Score_with_Internet_Access))
    file2_menu.add_command(label="Xây dựng sơ đồ phân tán dựa trên các đặc điểm số (tính đến Khuyết tật học tập)", command=lambda: plot_on_canvas(visualization_for_GUI.scatterplot_Numcol_and_Exam_Score_with_Learning_Disabilities))
    file2_menu.add_command(label="Vẽ biểu đồ boxplot Exam_Score và Parental Involvement", command=lambda: plot_on_canvas(visualization_for_GUI.boxplot_Parental_Involvement_and_Exam_Score))
    file2_menu.add_command(label="Vẽ biểu đồ boxplot Exam_Score và Access_to_Resources", command=lambda: plot_on_canvas(visualization_for_GUI.boxplot_Access_to_Resources_and_Exam_Score))
    file2_menu.add_command(label="Vẽ biểu đồ boxplot Exam_Score và Extracurricular_Activities", command=lambda: plot_on_canvas(visualization_for_GUI.boxplot_Extracurricular_Activities_and_Exam_Score))
    file2_menu.add_command(label="Vẽ biểu đồ boxplot Exam_Score và Sleep_Hours", command=lambda: plot_on_canvas(visualization_for_GUI.boxplot_Sleep_Hours_and_Exam_Score))
    file2_menu.add_command(label="Vẽ biểu đồ boxplot Exam_Score và Motivation_Level", command=lambda: plot_on_canvas(visualization_for_GUI.boxplot_Motivation_Level_and_Exam_Score))
    file2_menu.add_command(label="Vẽ biểu đồ boxplot Exam_Score và Internet_Access", command=lambda: plot_on_canvas(visualization_for_GUI.boxplot_Internet_Access_and_Exam_Score))
    file2_menu.add_command(label="Vẽ biểu đồ boxplot Exam_Score và Tutoring_Sessions", command=lambda: plot_on_canvas(visualization_for_GUI.boxplot_Tutoring_Sessions_and_Exam_Score))
    file2_menu.add_command(label="Vẽ biểu đồ boxplot Exam_Score và Family_Income", command=lambda: plot_on_canvas(visualization_for_GUI.boxplot_Family_Income_and_Exam_Score))
    file2_menu.add_command(label="Vẽ biểu đồ boxplot Exam_Score và Teacher_Quality", command=lambda: plot_on_canvas(visualization_for_GUI.boxplot_Teacher_Quality_and_Exam_Score))
    file2_menu.add_command(label="Vẽ biểu đồ boxplot cho Exam_Score và School_Type", command=lambda: plot_on_canvas(visualization_for_GUI.boxplot_School_Type_and_Exam_Score))
    file2_menu.add_command(label="Vẽ biểu đồ boxplot Exam_Score và Peer_Influence", command=lambda: plot_on_canvas(visualization_for_GUI.boxplot_Peer_Influence_and_Exam_Score))   
    file2_menu.add_command(label="Vẽ biểu đồ boxplot Exam_Score và Physical_Activity", command=lambda: plot_on_canvas(visualization_for_GUI.boxplot_Physical_Activity_and_Exam_Score))
    file2_menu.add_command(label="Vẽ biểu đồ boxplot cho Exam_Score và Learning_Disabilities", command=lambda: plot_on_canvas(visualization_for_GUI.boxplot_Learning_Disabilities_and_Exam_Score))
    file2_menu.add_command(label="Vẽ biểu đồ boxplot Exam_Score và Parental_Education_Level", command=lambda: plot_on_canvas(visualization_for_GUI.boxplot_Parental_Education_Level_and_Exam_Score))
    file2_menu.add_command(label="Vẽ biểu đồ boxplot Exam_Score và Distance_from_Home", command=lambda: plot_on_canvas(visualization_for_GUI.boxplot_Distance_from_Home_and_Exam_Score))
    file2_menu.add_command(label="Vẽ biểu đồ boxplot cho Exam_Score và Gender", command=lambda: plot_on_canvas(visualization_for_GUI.boxplot_Gender_and_Exam_Score))

     
    menu4.add_cascade(label="BIỂU ĐỒ TẦN SUẤT VÀ CỘT CHO CÁC THUỘC TÍNH ĐƠN LẺ", menu=file1_menu)
    menu4.add_cascade(label="BIỂU ĐỒ BIỂU DIỄN QUAN HỆ PHÂN TÁN (SỐ) VÀ BIỂU ĐỒ HỘP (PHÂN LOẠI) VỚI BIẾN MỤC TIÊU EXAM_SCORE", menu=file2_menu)
    menu4.add_command(label="HEATMAP", command=lambda: plot_on_canvas(visualization_for_GUI.heatmap))

    # Menu Button hiển thị menu
    menubutton4 = ttk.Menubutton(menu_frame4, text="Menu", menu=menu4)
    menubutton4.pack(side="left", padx=10, pady=5)

    makecenter(root, 1000, 600)
    root.mainloop() 

# Chạy ứng dụng
create_gui()