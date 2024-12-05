import pandas as pd
from tabulate import tabulate

# Đọc dữ liệu từ file CSV
data = pd.read_csv('data_source\\cleaned_data.csv')
pd.set_option('display.max_columns', None)  # Hiển thị tất cả các cột
pd.set_option('display.expand_frame_repr', False)

def add_student_record():
    """Thêm một dữ liệu khảo sát mới vào tập dữ liệu."""
    print("Nhập dữ liệu khảo sát mới:")
    
    # Kiểm tra và nhập liệu cho từng trường
    def input_float(prompt, min_value=0, max_value=100):
        while True:
            try:
                value = float(input(prompt))
                if min_value <= value <= max_value:
                    return value
                else:
                    print(f"Giá trị không hợp lệ. Vui lòng nhập số trong khoảng {min_value}-{max_value}.")
            except ValueError:
                print("Giá trị không hợp lệ. Vui lòng nhập một số thực.")
    def input_int(prompt, min_value=0, max_value=100):
        while True:
            try:
                value = int(input(prompt))
                if min_value <= value <= max_value:
                    return value
                else:
                    print(f"Giá trị không hợp lệ. Vui lòng nhập số trong khoảng {min_value}-{max_value}.")
            except ValueError:
                print("Giá trị không hợp lệ. Vui lòng nhập một số nguyên.")

    def input_str(prompt, valid_options=None):
        if valid_options:
            print(f"Các giá trị hợp lệ cho yếu tố bên dưới: {', '.join(valid_options)}")  # In ra các giá trị hợp lệ
        while True:
            value = input(prompt).strip().lower()  # Chuyển giá trị nhập vào thành chữ thường
            if valid_options:
                valid_options_lower = [option.lower() for option in valid_options]  # Chuyển các giá trị hợp lệ thành chữ thường
                if value not in valid_options_lower:
                    print(f"Giá trị không hợp lệ. Vui lòng chọn từ {valid_options}.")
                else:
                    # Trả về giá trị ban đầu trong valid_options (giữ nguyên kiểu viết hoa viết thường gốc)
                    return valid_options[valid_options_lower.index(value)]
            else:
                return value

    new_record = {
        'Hours_Studied': input_float("Hours Studied (Số giờ học mỗi tuần): ",0,168),
        'Attendance': input_float("Attendance (Tỷ lệ % tham gia lớp học), 0-100): "),
        'Parental_Involvement': input_str("Parental Involvement (Mức độ tham gia của phụ huynh vào việc học của sinh viên): ", valid_options=['Low', 'Medium', 'High']),
        'Access_to_Resources': input_str("Access to Resources (Mức độ có sẵn các tài nguyên học tập): ", valid_options=['Low', 'Medium', 'High']),
        'Extracurricular_Activities': input_str("Extracurricular Activities (Có tham gia hoạt động ngoại khóa hay không?): ", valid_options=['Yes', 'No']),
        'Sleep_Hours': input_float("Sleep Hours (Số giờ ngủ trung bình mỗi đêm): ", 0, 24),  # Giả định số giờ ngủ tối đa là 24
        'Previous_Scores': input_float("Previous Scores (Điểm số bài kiểm tra trước đó 0-100): ", 0, 100), #điểm số tối đa 100
        'Motivation_Level': input_str("Motivation Level (Mức độ động lực của sinh viên): ", valid_options=['Low', 'Medium', 'High']),
        'Internet_Access': input_str("Internet Access (Có sử dụng Internet không?): ", valid_options=['Yes', 'No']),
        'Tutoring_Sessions': input_int("Number of Tutoring Sessions (Số buổi học thêm mỗi tháng): ",0,10),
        'Family_Income': input_str("Family Income (Mức thu nhập của gia đình): ", valid_options=['Low', 'Medium', 'High']),
        'Teacher_Quality': input_str("Teacher Quality (Chất lượng của giáo viên): ", valid_options=['Low', 'Medium', 'High']),
        'School_Type': input_str("School Type (Loại trường sinh viên đang học): ", valid_options=['Public', 'Private']),
        'Peer_Influence': input_str("Peer Influence (Ảnh hưởng của bạn bè đối với kết quả học tập): ", valid_options=['Positive', 'Negative', 'Neutral']),
        'Physical_Activity': input_float("Physical Activity (Số giờ tham gia hoạt động thể chất mỗi tuần): ",0,168),
        'Learning_Disabilities': input_str("Learning Disabilities (Sinh viên có khuyết tật học tập không? (Gặp khó khăn khi nghe, suy nghĩ, nói, viết, đánh vần hoặc tính toán ): ", valid_options=['Yes', 'No']),
        'Parental_Education_Level': input_str("Parental Education Level (Trình độ học vấn cao nhất của phụ huynh ): ", valid_options=['High School', 'College', 'Postgraduate']),
        'Distance_from_Home': input_str("Distance from Home (Khoảng cách từ nhà đến trường, km): ", valid_options=['Near', 'Moderate', 'Far']),
        'Gender': input_str("Gender (Giới tính của sinh viên): ", valid_options=['Male', 'Female']),
        'Exam_Score': input_float("Exam Score (Điểm thi cuối kì 0-100): ", 0, 100)
    }
    
    global data  # Cập nhật biến toàn cục
    new_record_df = pd.DataFrame([new_record])  # Chuyển đổi dictionary thành DataFrame
    data = pd.concat([data, new_record_df], ignore_index=True)
    data.to_csv('data_source\\cleaned_data.csv', index=False)  # Lưu lại vào file CSV
    print("Thêm thành công dữ liệu khảo sát mới!")

def paginate(data_to_display, page_size=100):
    """Hàm phân trang cho dữ liệu."""
    total_rows = len(data_to_display)
    total_pages = (total_rows + page_size - 1) // page_size  # Tính số trang

    current_page = 1
    while True:
        start_idx = (current_page - 1) * page_size
        end_idx = min(start_idx + page_size, total_rows)

        print(f"\nTrang {current_page}/{total_pages} (Hiển thị từ dòng {start_idx + 1} đến {end_idx}):")
        print(tabulate(data_to_display.iloc[start_idx:end_idx], headers='keys', tablefmt='pretty'))

        if current_page == total_pages:
            print("Đây là trang cuối cùng.")
        elif current_page == 1:
            print("Đây là trang đầu tiên.")

        print("\nCác tùy chọn:")
        print("1. Tiếp theo (Next)")
        print("2. Quay lại (Previous)")
        print("3. Thoát")
        choice = input("Chọn hành động: ").strip().lower()

        if choice in ['1', 'next']:
            if current_page < total_pages:
                current_page += 1
            else:
                print("Bạn đang ở trang cuối.")
        elif choice in ['2', 'previous']:
            if current_page > 1:
                current_page -= 1
            else:
                print("Bạn đang ở trang đầu.")
        elif choice in ['3', 'exit']:
            break
        else:
            print("Lựa chọn không hợp lệ.")

def read_full_data(page_size=100):
    paginate(data, page_size)

def read_n_rows(n, page_size=100):
    """Hiển thị n dòng đầu tiên với phân trang."""
    subset = data.iloc[:n]
    paginate(subset, page_size)

def print_n_columns(n, page_size=100):
    """In ra n cột đầu tiên của dữ liệu, phân trang 100 dòng."""
    subset = data.iloc[:, :n]
    paginate(subset, page_size)

def print_specific_columns(columns, page_size=100):
    """In ra các cột cụ thể và số hàng, phân trang 100 dòng."""
    subset = data[columns]
    paginate(subset, page_size)

def user_select_columns(page_size=100):
    """Cho phép người dùng nhập chỉ số cột để in ra."""
    print("Các cột có sẵn:")
    for idx, col in enumerate(data.columns):
        print(f"{idx + 1}. {col}")  # In ra từng cột theo thứ tự
    
    while True:
        columns_to_display = input("Nhập chỉ số các cột cần in ra, cách nhau bằng dấu phẩy: ").split(',') #in ra cột theo thứ tự nhập
        try:
            # Chuyển các chỉ số từ dạng 1-indexed sang 0-indexed
            columns_to_display = [int(col.strip()) - 1 for col in columns_to_display]
            if all(0 <= index < len(data.columns) for index in columns_to_display):
                break  # Thoát vòng lặp nếu tất cả chỉ số hợp lệ
            else:
                print("Có chỉ số cột không hợp lệ. Vui lòng nhập lại.")
        except ValueError:
            print("Giá trị không hợp lệ. Vui lòng nhập các chỉ số nguyên, cách nhau bằng dấu phẩy.")

    # Tạo tập dữ liệu con với các cột được chọn
    selected_columns = data.iloc[:, columns_to_display]
    
    # Gọi hàm paginate để hiển thị dữ liệu với phân trang
    paginate(selected_columns, page_size)

def print_selected_columns_with_index(columns, n_rows, page_size=100):
    """In ra các cột cụ thể và số hàng với phân trang."""
    # Lấy dữ liệu con chỉ với các cột và số dòng mong muốn
    data_subset = data[columns].iloc[:n_rows]
    
    # Gọi hàm paginate để hiển thị
    paginate(data_subset, page_size)

def user_select_columns_and_rows():
    """Cho phép người dùng nhập chỉ số cột và số hàng để in ra."""
    print("Các cột có sẵn:")
    for idx, col in enumerate(data.columns):
        print(f"{idx + 1}. {col}")  # In ra từng cột theo thứ tự
    while True:
        columns_to_display = input("Nhập chỉ số các cột cần in ra, cách nhau bằng dấu phẩy: ").split(',') #in ra cột theo thứ tự nhập
        try:
            columns_to_display = [int(col.strip()) - 1 for col in columns_to_display]  # Chuyển chỉ số thành 0-indexed
            if all(0 <= index < len(data.columns) for index in columns_to_display):
                break  # Thoát vòng lặp nếu tất cả chỉ số hợp lệ
            else:
                print("Có chỉ số cột không hợp lệ. Vui lòng nhập lại.")
        except ValueError:
            print("Giá trị không hợp lệ. Vui lòng nhập các chỉ số nguyên, cách nhau bằng dấu phẩy.")

    # Nhập số hàng muốn hiển thị
    while True:
        try:
            n_rows = int(input("Nhập số hàng muốn hiển thị: ")) #n hàng đầu tiên
            if n_rows < 1 or n_rows > len(data):
                print(f"Số hàng phải trong phạm vi từ 1 đến {len(data)}.")
            else:
                break
        except ValueError:
            print("Vui lòng nhập một số nguyên hợp lệ.")

    # Hiển thị các cột người dùng chọn
    print_selected_columns_with_index(data.columns[columns_to_display], n_rows)

def display_valid_row_range():
    """Hiển thị khoảng chỉ số dòng hợp lệ có thể in."""
    total_rows = len(data)
    print(f"Có tổng cộng {total_rows} dòng dữ liệu.")
    print(f"Bạn có thể nhập từ dòng 0 đến dòng {total_rows - 1} .")

def print_rows_range(start, end, page_size=100):
    """Hiển thị các dòng trong khoảng với phân trang."""
    # Kiểm tra giới hạn phạm vi
    if start < 0 or end >= len(data):
        print(f"Chỉ số dòng nằm ngoài phạm vi! Vui lòng nhập từ 0 đến {len(data) - 1}.")
        return
    if start > end:
        print("Giá trị bắt đầu không thể lớn hơn giá trị kết thúc.")
        return

    # Lấy dữ liệu trong phạm vi
    data_subset = data.iloc[start:end + 1]

    # Gọi hàm phân trang chung
    paginate(data_subset, page_size=page_size)

 # Cập nhật lại dữ liệu mới
def update_student_record(data):
    def input_float(prompt, min_value=0, max_value=100):
        while True:
            try:
                value = float(input(prompt))
                if min_value <= value <= max_value:
                    return value
                else:
                    print(f"Giá trị không hợp lệ. Vui lòng nhập số trong khoảng {min_value}-{max_value}.")
            except ValueError:
                print("Giá trị không hợp lệ. Vui lòng nhập một số thực.")

    def input_int(prompt, min_value=0, max_value=100):
        while True:
            try:
                value = int(input(prompt))
                if min_value <= value <= max_value:
                    return value
                else:
                    print(f"Giá trị không hợp lệ. Vui lòng nhập số trong khoảng {min_value}-{max_value}.")
            except ValueError:
                print("Giá trị không hợp lệ. Vui lòng nhập một số nguyên.")

    def input_str(prompt, valid_options=None):
        if valid_options:
            print(f"Các giá trị hợp lệ: {', '.join(valid_options)}")  # In các giá trị hợp lệ
        while True:
            value = input(prompt).strip().lower()  # Chuyển nhập thành chữ thường
            if valid_options:
                valid_options_lower = [option.lower() for option in valid_options]  # Chuyển các giá trị hợp lệ thành chữ thường
                if value not in valid_options_lower:
                    print(f"Giá trị không hợp lệ. Vui lòng chọn từ {valid_options}.")
                else:
                    return valid_options[valid_options_lower.index(value)]  # Trả về giá trị gốc
            else:
                return value

    # Nhập chỉ số hàng muốn cập nhật
    row_index = input_int("Nhập chỉ số hàng muốn cập nhật: ", 0, len(data) - 1)

    # In ra hàng được chọn trước khi cập nhật
    print("\nHàng bạn đã chọn để cập nhật:")
    print(tabulate([data.iloc[row_index]], headers="keys", tablefmt="pretty", showindex=True))
    
    while True:
        # Hỏi người dùng muốn cập nhật toàn bộ hàng hay một cột cụ thể
        update_all = input_str("Có muốn cập nhật toàn bộ hàng? (Yes or No): ", valid_options=["Yes", "No"])

        if update_all.lower() == "yes":
            # Cập nhật toàn bộ cột trong hàng
            for column in data.columns:
                current_value = data.loc[row_index, column]
                if column in ['Hours_Studied', 'Physical_Activity']:
                    if not pd.api.types.is_float_dtype(data[column]):
                        data[column] = data[column].astype(float)
                    data.loc[row_index, column] = input_float(f"{column} (hiện tại: {current_value}): ", 0, 168)
                elif column == 'Sleep_Hours':
                    if not pd.api.types.is_float_dtype(data[column]):
                        data[column] = data[column].astype(float)
                    data.loc[row_index, column] = input_float(f"{column} (hiện tại: {current_value}): ", 0, 24)
                elif column in ['Exam_Score', 'Attendance', 'Previous_Scores']:
                    if not pd.api.types.is_float_dtype(data[column]):
                        data[column] = data[column].astype(float)
                    data.loc[row_index, column] = input_float(f"{column} (hiện tại: {current_value}): ", 0, 100)
                elif column == 'Tutoring_Sessions':
                    if not pd.api.types.is_integer_dtype(data[column]):
                        data[column] = data[column].astype(int)
                    data.loc[row_index, column] = input_int(f"{column} (hiện tại: {current_value}): ", 0, 10)
                else:
                    valid_options = {
                        'Parental_Involvement': ['Low', 'Medium', 'High'],
                        'Access_to_Resources': ['Low', 'Medium', 'High'],
                        'Extracurricular_Activities': ['Yes', 'No'],
                        'Motivation_Level': ['Low', 'Medium', 'High'],
                        'Internet_Access': ['Yes', 'No'],
                        'Family_Income': ['Low', 'Medium', 'High'],
                        'Teacher_Quality': ['Low', 'Medium', 'High'],
                        'School_Type': ['Public', 'Private'],
                        'Peer_Influence': ['Positive', 'Negative', 'Neutral'],
                        'Learning_Disabilities': ['Yes', 'No'],
                        'Parental_Education_Level': ['High School', 'College', 'Postgraduate'],
                        'Distance_from_Home': ['Near', 'Moderate', 'Far'],
                        'Gender': ['Male', 'Female']
                    }
                    if column in valid_options:
                        new_value = input_str(f"{column} (hiện tại: {current_value}): ", valid_options=valid_options[column])
                        data.loc[row_index, column] = new_value
        else:
            # Hiển thị danh sách các cột để chọn
            print("\nDanh sách các cột có thể cập nhật:")
            for i, column in enumerate(data.columns):
                print(f"{i + 1}. {column}")

            # Nhập số cột muốn cập nhật
            column_index = input_int("Nhập số tương ứng với cột muốn cập nhật: ", 1, len(data.columns)) - 1
            column_to_update = data.columns[column_index]
            current_value = data.loc[row_index, column_to_update]

            # Cập nhật cột được chọn
            if column_to_update in ['Hours_Studied', 'Physical_Activity']:
                if not pd.api.types.is_float_dtype(data[column_to_update]):
                    data[column_to_update] = data[column_to_update].astype(float)
                data.loc[row_index, column_to_update] = input_float(f"{column_to_update} (hiện tại: {current_value}): ", 0, 168)
            elif column_to_update == 'Sleep_Hours':
                if not pd.api.types.is_float_dtype(data[column_to_update]):
                    data[column_to_update] = data[column_to_update].astype(float)
                data.loc[row_index, column_to_update] = input_float(f"{column_to_update} (hiện tại: {current_value}): ", 0, 24)
            elif column_to_update in ['Exam_Score', 'Attendance', 'Previous_Scores']:
                if not pd.api.types.is_float_dtype(data[column_to_update]):
                    data[column_to_update] = data[column_to_update].astype(float)
                data.loc[row_index, column_to_update] = input_float(f"{column_to_update} (hiện tại: {current_value}): ", 0, 100)
            elif column_to_update == 'Tutoring_Sessions':
                if not pd.api.types.is_integer_dtype(data[column_to_update]):
                    data[column_to_update] = data[column_to_update].astype(int)
                data.loc[row_index, column_to_update] = input_int(f"{column_to_update} (hiện tại: {current_value}): ", 0, 10)
            else:
                valid_options = {
                    'Parental_Involvement': ['Low', 'Medium', 'High'],
                    'Access_to_Resources': ['Low', 'Medium', 'High'],
                    'Extracurricular_Activities': ['Yes', 'No'],
                    'Motivation_Level': ['Low', 'Medium', 'High'],
                    'Internet_Access': ['Yes', 'No'],
                    'Family_Income': ['Low', 'Medium', 'High'],
                    'Teacher_Quality': ['Low', 'Medium', 'High'],
                    'School_Type': ['Public', 'Private'],
                    'Peer_Influence': ['Positive', 'Negative', 'Neutral'],
                    'Learning_Disabilities': ['Yes', 'No'],
                    'Parental_Education_Level': ['High School', 'College', 'Postgraduate'],
                    'Distance_from_Home': ['Near', 'Moderate', 'Far'],
                    'Gender': ['Male', 'Female']
                }
                if column_to_update in valid_options:
                    new_value = input_str(f"{column_to_update} (hiện tại: {current_value}): ", valid_options=valid_options[column_to_update])
                    data.loc[row_index, column_to_update] = new_value

        # Hỏi xem có muốn tiếp tục cập nhật không
        continue_update = input_str("Có muốn tiếp tục cập nhật? (Yes or No): ", valid_options=["Yes", "No"])
        if continue_update.lower() == "no":
            break

    # Lưu dữ liệu vào file CSV
    data.to_csv('data_source\\cleaned_data.csv', index=False)
    print("Đã cập nhật thành công.")

def delete_student_record():
    """Xóa một hoặc nhiều dòng từ DataFrame sau khi xác nhận."""
    global data
    try:
        if data.empty:
            print("Dữ liệu hiện tại trống. Không thể thực hiện thao tác xóa.")
            return

        # Nhập các chỉ số dòng cần xóa (hỗ trợ xóa nhiều dòng)
        while True:
            try:
                row_indices = input(
                    f"Nhập chỉ số dòng cần xóa (phân cách bằng dấu phẩy, từ 0 đến {len(data) - 1}): "
                ).strip()
                row_indices = [int(idx.strip()) for idx in row_indices.split(",")]

                # Kiểm tra xem tất cả các chỉ số dòng có hợp lệ hay không
                if all(0 <= idx < len(data) for idx in row_indices):
                    break
                else:
                    print("Có chỉ số dòng không hợp lệ. Vui lòng nhập lại.")
            except ValueError:
                print("Giá trị nhập không hợp lệ. Vui lòng nhập danh sách các số nguyên phân cách bằng dấu phẩy.")

        # Hiển thị các dòng muốn xóa với dấu gạch phân cách
        print("\nCác dòng bạn đã chọn để xóa:")
        rows_to_display = data.loc[row_indices]
        print(tabulate(rows_to_display, headers="keys", tablefmt="pretty", showindex=True))

        # Yêu cầu xác nhận trước khi xóa
        confirm = input("Bạn có chắc chắn muốn xóa các dòng này? (Yes/No): ").strip().lower()
        if confirm == "yes":
            # Xóa các dòng và đặt lại chỉ số
            data = data.drop(index=row_indices).reset_index(drop=True)
            print(f"Đã xóa thành công các dòng: {row_indices}")

            # Lưu lại dữ liệu vào file CSV
            data.to_csv('data_source\\cleaned_data.csv', index=False)
            print("Dữ liệu đã được lưu thành công vào file 'cleaned_data.csv'.")
        else:
            print("Hành động xóa đã bị hủy.")

    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

#Sắp xếp giá trị tăng dần của một cột
def sort_numeric_column():
    """Sắp xếp dữ liệu theo cột chứa giá trị số (tăng dần)."""
    # Lọc các cột số từ dataframe
    numeric_columns = data.select_dtypes(include=['number']).columns.tolist()
    
    if not numeric_columns:
        print("Không có cột số nào trong dữ liệu để sắp xếp.")
        return
    
    print("Danh sách các cột số có thể sắp xếp:")
    for idx, column in enumerate(numeric_columns):
        print(f"{idx + 1}. {column}")
    
    while True:
        try:
            choice = int(input(f"Chọn một cột để sắp xếp (1-{len(numeric_columns)}): "))
            if 1 <= choice <= len(numeric_columns):
                selected_column = numeric_columns[choice - 1]
                break
            else:
                print(f"Vui lòng chọn số trong khoảng từ 1 đến {len(numeric_columns)}.")
        except ValueError:
            print("Lựa chọn không hợp lệ. Vui lòng nhập một số nguyên.")
    
    # Sắp xếp dữ liệu tăng dần theo cột đã chọn
    sorted_data = data.sort_values(by=selected_column, ascending=True)
    print(f"Dữ liệu đã được sắp xếp tăng dần theo cột '{selected_column}':")

    # Cho phép người dùng xem dữ liệu sắp xếp với phân trang
    paginate(sorted_data)

# Sắp xếp giá trị giảm dầm của một cột
def sort_numeric_column_desc():
    """Sắp xếp dữ liệu giảm dần theo một cột có giá trị số."""
    # Lấy danh sách các cột chỉ chứa giá trị số
    numeric_columns = data.select_dtypes(include='number').columns.tolist()

    if not numeric_columns:
        print("Không có cột số nào để sắp xếp.")
        return

    print("Các cột có thể sắp xếp:")
    for idx, column in enumerate(numeric_columns, start=1):
        print(f"{idx}. {column}")

    while True:
        try:
            choice = int(input("Chọn số tương ứng với cột muốn sắp xếp: "))
            if 1 <= choice <= len(numeric_columns):
                selected_column = numeric_columns[choice - 1]
                # Sắp xếp dữ liệu theo cột đã chọn (giảm dần)
                sorted_data = data.sort_values(by=selected_column, ascending=False)
                paginate(sorted_data)  # Hiển thị dữ liệu đã sắp xếp với phân trang
                break
            else:
                print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
        except ValueError:
            print("Dữ liệu không hợp lệ. Vui lòng nhập một số nguyên.")

# Lọc theo thuộc tính có giá trị chữ.
def search_by_attribute(data):
    def input_str(prompt, valid_options=None):
        #Hàm nhập chuỗi với kiểm tra giá trị hợp lệ.
        if valid_options:
            print(f"Các giá trị hợp lệ cho yêu cầu bên dưới: {', '.join(valid_options)}")
        while True:
            value = input(prompt).strip().lower()
            if valid_options:
                valid_options_lower = [option.lower() for option in valid_options]
                if value not in valid_options_lower:
                    print(f"Giá trị không hợp lệ. Vui lòng chọn từ {valid_options}.")
                else:
                    return valid_options[valid_options_lower.index(value)]
            else:
                return value

    def input_int(prompt, min_value, max_value):
        #Hàm nhập số nguyên trong khoảng hợp lệ.
        while True:
            try:
                value = int(input(prompt))
                if min_value <= value <= max_value:
                    return value
                else:
                    print(f"Giá trị không hợp lệ. Vui lòng nhập số trong khoảng {min_value}-{max_value}.")
            except ValueError:
                print("Giá trị không hợp lệ. Vui lòng nhập một số nguyên.")

    valid_options = {
        'Parental_Involvement': ['Low', 'Medium', 'High'],
        'Access_to_Resources': ['Low', 'Medium', 'High'],
        'Extracurricular_Activities': ['Yes', 'No'],
        'Motivation_Level': ['Low', 'Medium', 'High'],
        'Internet_Access': ['Yes', 'No'],
        'Family_Income': ['Low', 'Medium', 'High'],
        'Teacher_Quality': ['Low', 'Medium', 'High'],
        'School_Type': ['Public', 'Private'],
        'Peer_Influence': ['Positive', 'Negative', 'Neutral'],
        'Learning_Disabilities': ['Yes', 'No'],
        'Parental_Education_Level': ['High School', 'College', 'Postgraduate'],
        'Distance_from_Home': ['Near', 'Moderate', 'Far'],
        'Gender': ['Male', 'Female']
    }

    # Hiển thị danh sách các cột có thể tìm kiếm
    print("Danh sách các cột bạn có thể lọc:")
    columns_list = list(valid_options.keys())

    # Nhập số tiêu chí muốn tìm kiếm
    num_criteria = input_int("Nhập số tiêu chí bạn muốn lọc (tối thiểu 1): ", 1, len(columns_list))

    # Khởi tạo bộ lọc cho dữ liệu
    filters = {}

    # Lặp qua từng tiêu chí, loại bỏ cột đã chọn khỏi danh sách
    for i in range(num_criteria):
        print(f"\nTiêu chí {i + 1}:")
        for j, column in enumerate(columns_list, start=1):
            print(f"{j}. {column}")
        column_index = input_int("Nhập số tương ứng với cột muốn lọc: ", 1, len(columns_list))
        column = columns_list.pop(column_index - 1)  # Loại bỏ cột đã chọn khỏi danh sách
        search_value = input_str(f"Nhập giá trị muốn tìm trong cột '{column}': ", valid_options=valid_options[column])
        filters[column] = search_value

    # Lọc dữ liệu dựa trên các tiêu chí
    filtered_data = data
    for column, value in filters.items():
        filtered_data = filtered_data[filtered_data[column] == value]

    # Kiểm tra và hiển thị kết quả
    if filtered_data.empty:
        print("Không tìm thấy kết quả nào cho các tiêu chí đã chọn.")
        return
    print("Kết quả tìm kiếm:")
    paginate(filtered_data)

# Chức năng trích lọc dữ liệu 1 số có giá trị số
def filter_numeric_columns():
    """Lọc dữ liệu dựa trên các cột số học (float hoặc int)."""
    
    # Xác định các cột có kiểu dữ liệu số
    numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns

    # Hiển thị các cột số để người dùng lựa chọn
    print("Các cột có sẵn để lọc theo phạm vi:")
    for idx, col in enumerate(numeric_columns, start=1):
        print(f"{idx}. {col}")

    # Người dùng nhập chỉ số cột muốn lọc
    while True:
        try:
            column_index = int(input("Nhập chỉ số cột muốn lọc: ").strip()) - 1
            if 0 <= column_index < len(numeric_columns):
                column_name = numeric_columns[column_index]
                break
            else:
                print("Chỉ số không hợp lệ. Vui lòng thử lại.")
        except ValueError:
            print("Vui lòng nhập một số nguyên hợp lệ.")

    # Xác định phạm vi giá trị của cột được chọn
    min_possible = data[column_name].min()
    max_possible = data[column_name].max()
    print(f"Phạm vi giá trị có thể nhập cho cột '{column_name}': {min_possible} đến {max_possible}")

    # Nhập phạm vi giá trị để lọc
    while True: 
        try:
            min_value = float(input(f"Nhập giá trị nhỏ nhất cho cột '{column_name}': "))
            max_value = float(input(f"Nhập giá trị lớn nhất cho cột '{column_name}': "))
            
            # Kiểm tra nếu giá trị nhập nằm ngoài phạm vi hợp lệ
            if min_value < min_possible or max_value > max_possible:
                print("Giá trị nằm ngoài phạm vi. Vui lòng nhập lại.")
                continue

            if min_value > max_value:
                print("Giá trị nhỏ nhất không được lớn hơn giá trị lớn nhất. Vui lòng nhập lại.")
                continue

        # Thực hiện lọc dữ liệu
            filtered_data = data[(data[column_name] >= min_value) & (data[column_name] <= max_value)]
            if filtered_data.empty:
                print("Không có dữ liệu thỏa mãn điều kiện lọc.")
            else:
                print("\nKết quả lọc dữ liệu:")
                paginate(filtered_data)
                break
        except ValueError:
            print("Giá trị nhập không hợp lệ. Vui lòng nhập số.")

def filter_unique_value():
    """Lọc một giá trị duy nhất."""
    
    # Xác định các cột có kiểu dữ liệu số
    numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns

    # Hiển thị các cột số để người dùng lựa chọn
    print("Các cột có sẵn để lọc theo phạm vi:")
    for idx, col in enumerate(numeric_columns, start=1):
        print(f"{idx}. {col}")

    # Người dùng nhập chỉ số cột muốn lọc
    while True:
        try:
            column_index = int(input("Nhập chỉ số cột muốn lọc: ").strip()) - 1
            if 0 <= column_index < len(numeric_columns):
                column_name = numeric_columns[column_index]
                break
            else:
                print("Chỉ số không hợp lệ. Vui lòng thử lại.")
        except ValueError:
            print("Vui lòng nhập một số nguyên hợp lệ.")

    # Xác định phạm vi giá trị của cột được chọn
    min_possible = data[column_name].min()
    max_possible = data[column_name].max()
    print(f"Phạm vi giá trị có thể nhập cho cột '{column_name}': {min_possible} đến {max_possible}")
    # Người dùng nhập giá trị cần lọc
    while True:
        try:
            value = float(input(f"Nhập giá trị cần lọc trong cột '{column_name}': ").strip())
            if min_possible <= value <= max_possible:
                # Lọc dữ liệu
                filtered_data = data[data[column_name] == value]
                if filtered_data.empty:
                    print("Không có dữ liệu thỏa mãn điều kiện lọc.")
                else:
                    print("\nKết quả lọc dữ liệu:")
                    paginate(filtered_data)
                break
            else:
                print("Giá trị nằm ngoài phạm vi hợp lệ. Vui lòng thử lại.")
        except ValueError:
            print("Vui lòng nhập một giá trị số hợp lệ.")

def filter_multiple_values():
    """Lọc nhiều giá trị."""
    
    # Xác định các cột có kiểu dữ liệu số
    numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns

    # Hiển thị các cột số để người dùng lựa chọn
    print("Các cột có sẵn để lọc theo phạm vi:")
    for idx, col in enumerate(numeric_columns, start=1):
        print(f"{idx}. {col}")

    # Người dùng nhập chỉ số cột muốn lọc
    while True:
        try:
            column_index = int(input("Nhập chỉ số cột muốn lọc: ").strip()) - 1
            if 0 <= column_index < len(numeric_columns):
                column_name = numeric_columns[column_index]
                break
            else:
                print("Chỉ số không hợp lệ. Vui lòng thử lại.")
        except ValueError:
            print("Vui lòng nhập một số nguyên hợp lệ.")
    
    # Lấy phạm vi giá trị hợp lệ trong cột đã chọn
    min_possible = data[column_name].min()
    max_possible = data[column_name].max()
    print(f"Phạm vi giá trị hợp lệ cho cột '{column_name}': {min_possible} đến {max_possible}")
    
    # Nhập các giá trị cần lọc
    while True:
        try:
            values_input = input(f"Nhập các giá trị cần lọc trong cột '{column_name}' (cách nhau bởi dấu phẩy): ").split(',')
            values = [float(value.strip()) for value in values_input]  # Chuyển đổi thành kiểu số
            # Kiểm tra xem các giá trị có nằm trong phạm vi hợp lệ
            if all(min_possible <= value <= max_possible for value in values):
                break
            else:
                print(f"Giá trị phải nằm trong phạm vi từ {min_possible} đến {max_possible}. Vui lòng thử lại.")
        except ValueError:
            print("Vui lòng nhập các giá trị số hợp lệ, cách nhau bởi dấu phẩy.")

    # Lọc dữ liệu theo các giá trị nhập vào
    filtered_data = data[data[column_name].isin(values)]
    
    # Hiển thị kết quả lọc
    if filtered_data.empty:
        print("Không có dữ liệu thỏa mãn điều kiện lọc.")
    else:
        print("\nKết quả lọc dữ liệu:")
        paginate(filtered_data)

def numeric_filter_menu():
    """Hiển thị menu lọc dữ liệu theo cột số."""
    while True:
        print("\nChọn một chức năng lọc:")
        print("1. Lọc một giá trị duy nhất.")
        print("2. Lọc nhiều giá trị.")
        print("3. Lọc giá trị trong phạm vi.")
        print("4. Quay lại menu chính.")
        
        sub_choice = input("Nhập lựa chọn của bạn (1-4): ").strip()
        if sub_choice == '1':
            filter_unique_value()
        elif sub_choice == '2':
            filter_multiple_values()
        elif sub_choice == '3':
            filter_numeric_columns()
        elif sub_choice == '4':
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

if __name__ == "__main__":
    while True:
        print()
        print("╔══════════════════════════════════════════╗")
        print("║  CHƯƠNG TRÌNH QUẢN LÝ DỮ LIỆU KHẢO SÁT   ║")
        print("╠══════════════════════════════════════════╣")
        print("║ Vui lòng chọn một tùy chọn:              ║")
        print("║──────────────────────────────────────────║")
        print("║ 1. Thêm dữ liệu khảo sát mới             ║")
        print("║ 2. Hiển thị toàn bộ dữ liệu              ║")
        print("║ 3. Hiển thị n dòng đầu tiên              ║")
        print("║ 4. Hiển thị n cột đầu tiên               ║")
        print("║ 5. Hiển thị các cột cụ thể               ║")
        print("║ 6. Hiển thị các cột với số hàng cụ thể   ║")
        print("║ 7. Hiển thị các dòng trong khoảng cụ thể ║")
        print("║ 8. Lọc theo thuộc tính có giá trị số     ║")
        print("║ 9. Lọc theo thuộc tính có giá trị chữ    ║")
        print("║ 10.Cập nhật dữ liệu mới                  ║")
        print("║ 11.Xóa dữ liệu theo hàng                 ║")
        print("║ 12.Sắp xếp giá trị tăng dần của một cột  ║")
        print("║ 13.Sắp xếp giá trị giảm dần của một cột  ║")
        print("║ 14.THOÁT CHƯƠNG TRÌNH                    ║")
        print("╚══════════════════════════════════════════╝")
        
        choice = input("Nhập lựa chọn của bạn (1-14): ")

        def input_int(prompt, min_value=0, max_value=100):
            while True:
                try:
                    value = int(input(prompt))
                    if min_value <= value <= max_value:
                        return value 
                    else:
                        print(f"Giá trị không hợp lệ. Vui lòng nhập số trong khoảng {min_value}-{max_value}.")
                except ValueError:
                    print("Giá trị không hợp lệ. Vui lòng nhập một số nguyên.")

        if choice == '1':
            add_student_record()
        elif choice == '2':
            read_full_data()
        elif choice == '3':
            n = input_int("Nhập số dòng muốn hiển thị: ", 1, len(data))
            read_n_rows(n)
        elif choice == '4':
            n = input_int("Nhập số cột muốn hiển thị: ", 1, 20)
            print_n_columns(n)
        elif choice == '5':
            user_select_columns()
        elif choice == '6':
            user_select_columns_and_rows()
        elif choice == '7':
            display_valid_row_range()
            while True:
                start = input_int("Nhập chỉ số dòng bắt đầu: ", 0, len(data)-1)
                end = input_int("Nhập chỉ số dòng kết thúc: ", 0, len(data)-1)
                if start <= end:
                    break
                else:
                    print("Chỉ số dòng bắt đầu phải bé hơn hoặc bằng chỉ số dòng kết thúc")
            print_rows_range(start, end)
        elif choice == '8':
            numeric_filter_menu()    
        elif choice == '9':
            search_by_attribute(data)          
        elif choice == '10':
            update_student_record(data)          
        elif choice == '11':
            delete_student_record()
        elif choice == '12':
            sort_numeric_column()
        elif choice == '13':
            sort_numeric_column_desc()
        elif choice == '14':
            print("Cảm ơn bạn đã sử dụng chương trình! Hẹn gặp lại.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")
            print("──────────────────────────────────────────")

    


