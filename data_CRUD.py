import pandas as pd
from tabulate import tabulate

# Đọc dữ liệu từ file CSV
data = pd.read_csv('data_source\\cleaned_data.csv')
pd.set_option('display.max_columns', None)  # Hiển thị tất cả các cột
pd.set_option('display.expand_frame_repr', False)

def add_student_record():
    """Thêm một thông tin sinh viên mới vào tập dữ liệu."""
    print("Nhập thông tin sinh viên mới:")
    
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

    def input_int(prompt):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Giá trị không hợp lệ. Vui lòng nhập một số nguyên.")

    def input_str(prompt, valid_options=None):
        if valid_options:
            print(f"Các giá trị hợp lệ: {', '.join(valid_options)}")  # In ra các giá trị hợp lệ
        while True:
            value = input(prompt).strip()
            if valid_options:
                if value not in valid_options:
                    print(f"Giá trị không hợp lệ. Vui lòng chọn từ {valid_options}.")
                else:
                    return value  # Trả về giá trị nhập nếu hợp lệ
            else:
                return value

    new_record = {
        'Hours_Studied': input_float("Hours Studied (Số giờ học): ", 0, 100),
        'Attendance': input_float("Attendance (Điểm danh, 0-100): ", 0, 100),
        'Parental_Involvement': input_str("Parental Involvement (Sự tham gia của phụ huynh): ", valid_options=['Low', 'Medium', 'High']),
        'Access_to_Resources': input_str("Access to Resources (Tiếp cận tài nguyên): ", valid_options=['Low', 'Medium', 'High']),
        'Extracurricular_Activities': input_str("Extracurricular Activities (Hoạt động ngoại khóa): ", valid_options=['Yes', 'No']),
        'Sleep_Hours': input_float("Sleep Hours (Số giờ ngủ): ", 0, 24),  # Giả định số giờ ngủ tối đa là 24
        'Previous_Scores': input_float("Previous Scores (Điểm số trước đó): ", 0, 100),
        'Motivation_Level': input_str("Motivation Level (Mức độ động lực): ", valid_options=['Low', 'Medium', 'High']),
        'Internet_Access': input_str("Internet Access (Tiếp cận Internet): ", valid_options=['Yes', 'No']),
        'Tutoring_Sessions': input_int("Number of Tutoring Sessions (Số buổi học thêm): "),
        'Family_Income': input_str("Family Income (Thu nhập gia đình): ", valid_options=['Low', 'Medium', 'High']),
        'Teacher_Quality': input_str("Teacher Quality (Chất lượng giáo viên): ", valid_options=['Low', 'Medium', 'High']),
        'School_Type': input_str("School Type (Loại trường, Public/Private): ", valid_options=['Public', 'Private']),
        'Peer_Influence': input_str("Peer Influence (Ảnh hưởng từ bạn bè): ", valid_options=['Positive', 'Negative', 'Neutral']),
        'Physical_Activity': input_int("Physical Activity (Hoạt động thể chất): "),
        'Learning_Disabilities': input_str("Learning Disabilities (Khuyết tật học tập, Yes/No): ", valid_options=['Yes', 'No']),
        'Parental_Education_Level': input_str("Parental Education Level (Trình độ học vấn của phụ huynh): ", valid_options=['High School', 'College', 'Postgraduate']),
        'Distance_from_Home': input_str("Distance from Home (Khoảng cách từ nhà, km): ", valid_options=['Near', 'Moderate', 'Far']),
        'Gender': input_str("Gender (Giới tính, Male/Female): ", valid_options=['Male', 'Female']),
        'Exam_Score': input_float("Exam Score (Điểm thi, 0-100): ", 0, 100)
    }
    
    global data  # Cập nhật biến toàn cục
    new_record_df = pd.DataFrame([new_record])  # Chuyển đổi dictionary thành DataFrame
    data = pd.concat([data, new_record_df], ignore_index=True)
    data.to_csv('data_source\\cleaned_data.csv', index=False)  # Lưu lại vào file CSV
    print("Thêm thành công dữ liệu sinh viên mới!")

def read_full_data():
    """Hiển thị toàn bộ tập dữ liệu."""
    print(tabulate(data, headers='keys', tablefmt='pretty'))

def read_n_rows(n):
    """Hiển thị n dòng đầu tiên của dữ liệu."""
    print(tabulate(data.head(n), headers='keys', tablefmt='pretty'))

def print_n_columns(n):
    """In ra n cột đầu tiên của dữ liệu."""
    print(tabulate(data.iloc[:, :n], headers='keys', tablefmt='pretty'))

def print_specific_columns(columns):
    """In ra các cột cụ thể và số hàng."""
    data_with_index = data[columns].reset_index()
    data_with_index.rename(columns={'index': 'Row Number'}, inplace=True)
    print(tabulate(data_with_index, headers='keys', tablefmt='pretty'))

def user_select_columns():
    """Cho phép người dùng nhập chỉ số cột để in ra."""
    print("Các cột có sẵn:")
    for idx, col in enumerate(data.columns):
        print(f"{idx + 1}. {col}")  # In ra từng cột theo thứ tự

    columns_to_display = input("Nhập chỉ số các cột cần in ra, cách nhau bằng dấu phẩy: ").split(',')
    columns_to_display = [int(col.strip()) - 1 for col in columns_to_display]  # Chuyển chỉ số thành 0-indexed

    # Kiểm tra tính hợp lệ của chỉ số cột
    for index in columns_to_display:
        if index < 0 or index >= len(data.columns):
            print(f"Chỉ số cột '{index + 1}' không hợp lệ.")  # In chỉ số gốc
            return

    # Hiển thị các cột người dùng chọn
    print_specific_columns(data.columns[columns_to_display])  # Gọi hàm để hiển thị cột

def print_selected_columns_with_index(columns, n_rows):
    """In ra các cột cụ thể và số hàng với chỉ định số dòng."""
    
    data_subset = data[columns].head(n_rows).reset_index()
    data_subset.rename(columns={'index': 'Row Number'}, inplace=True)

    print(tabulate(data_subset, headers='keys', tablefmt='pretty'))

def user_select_columns_and_rows():
    """Cho phép người dùng nhập chỉ số cột và số hàng để in ra."""
    print("Các cột có sẵn:")
    # In ra danh sách các cột với chỉ số
    for idx, col in enumerate(data.columns):
        print(f"{idx + 1}. {col}")
    
    # Nhập chỉ số cột cần in
    columns_to_display = input("Nhập chỉ số các cột cần in ra, cách nhau bằng dấu phẩy: ").split(',')
    columns_to_display = [int(col.strip()) - 1 for col in columns_to_display]  # Chuyển chỉ số thành 0-indexed
    
    # Kiểm tra tính hợp lệ của chỉ số cột
    for index in columns_to_display:
        if index < 0 or index >= len(data.columns):
            print(f"Chỉ số cột '{index + 1}' không hợp lệ.")  # In chỉ số gốc
            return

    # Nhập số hàng muốn hiển thị
    while True:
        try:
            n_rows = int(input("Nhập số hàng muốn hiển thị: "))
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
    print(f"Bạn có thể nhập từ dòng 1 đến dòng {total_rows}.")

def print_rows_range(start, end):
    """In ra các dòng từ start đến end."""
    if start < 0 or end >= len(data) or start > end:
        print("Giá trị dòng không hợp lệ.")
        return
    
    # Lấy các dòng từ start đến end
    data_subset = data.iloc[start:end+1].reset_index()
    data_subset.rename(columns={'index': 'Row Number'}, inplace=True)

    print(tabulate(data_subset, headers='keys', tablefmt='pretty'))

def update_student_record():
    """Cập nhật thông tin sinh viên theo chỉ số dòng và chỉ số cột."""
    global data
    try:
        # Nhập chỉ số dòng cần cập nhật với kiểm tra lỗi
        while True:
            try:
                row_index = int(input("Nhập chỉ số dòng cần cập nhật: ")) - 1  # Trừ 1 để tương ứng với chỉ số trong DataFrame
                if 0 <= row_index < len(data):
                    break
                else:
                    print("Chỉ số dòng không hợp lệ. Vui lòng thử lại.")
            except ValueError:
                print("Giá trị không hợp lệ. Vui lòng nhập một số nguyên.")
        
        # Hỏi người dùng muốn cập nhật một cột hay toàn bộ hàng
        update_all = input("Bạn có muốn cập nhật toàn bộ dữ liệu trong hàng này? (y/n): ").strip().lower()
        
        if update_all == 'y':
            # Cập nhật tất cả dữ liệu trong hàng
            for col in data.columns:
                current_value = data.at[row_index, col]
                while True:
                    new_value = input(f"{col} (hiện tại: {current_value}): ").strip()
                    try:
                        # Kiểm tra và ép kiểu dữ liệu cho giá trị mới
                        if pd.api.types.is_numeric_dtype(data[col]):
                            new_value = pd.to_numeric(new_value, errors='coerce')
                        elif pd.api.types.is_bool_dtype(data[col]):
                            new_value = new_value.lower() in ['true', '1', 't', 'yes']
                        
                        data.at[row_index, col] = new_value
                        break
                    except ValueError:
                        print(f"Giá trị cho {col} không hợp lệ. Vui lòng nhập lại.")

            print("Toàn bộ hàng đã được cập nhật thành công!")
        
        else:
            # Cập nhật một cột cụ thể với kiểm tra lỗi
            print("Các cột có sẵn:")
            for idx, col in enumerate(data.columns):
                print(f"{idx + 1}. {col}")

            while True:
                try:
                    column_index = int(input("Nhập chỉ số cột cần cập nhật: ")) - 1
                    if 0 <= column_index < len(data.columns):
                        actual_column_name = data.columns[column_index]
                        break
                    else:
                        print("Chỉ số cột không hợp lệ. Vui lòng thử lại.")
                except ValueError:
                    print("Giá trị không hợp lệ. Vui lòng nhập một số nguyên.")

            current_value = data.at[row_index, actual_column_name]
            while True:
                new_value = input(f"{actual_column_name} (hiện tại: {current_value}): ").strip()
                try:
                    # Kiểm tra và ép kiểu dữ liệu cho giá trị mới
                    if pd.api.types.is_numeric_dtype(data[actual_column_name]):
                        new_value = pd.to_numeric(new_value, errors='coerce')
                    elif pd.api.types.is_bool_dtype(data[actual_column_name]):
                        new_value = new_value.lower() in ['true', '1', 't', 'yes']
                    
                    data.at[row_index, actual_column_name] = new_value
                    print("Cập nhật thành công cho cột đã chọn!")
                    break
                except ValueError:
                    print(f"Giá trị cho {actual_column_name} không hợp lệ. Vui lòng nhập lại.")

        # Lưu lại dữ liệu vào file CSV
        data.to_csv('data_source\\cleaned_data.csv', index=False)
        print("Dữ liệu đã được lưu thành công vào file CSV!")

    except ValueError:
        print("Giá trị không hợp lệ.")

def delete_student_record():
    """Xóa một cột cụ thể trong hàng hoặc toàn bộ một hàng."""
    global data
    try:
        # Yêu cầu người dùng chọn tùy chọn và cho phép nhập lại nếu nhập sai
        while True:
            delete_option = input("Bạn muốn xóa:\n1. Một cột cụ thể trong hàng\n2. Toàn bộ một hàng\nNhập lựa chọn (1 hoặc 2): ").strip()
            if delete_option in ['1', '2']:
                break
            else:
                print("Lựa chọn không hợp lệ. Vui lòng chọn 1 hoặc 2.")

        # Xóa một cột cụ thể trong một hàng
        if delete_option == '1':
            # Nhập chỉ số dòng cần xóa và kiểm tra lỗi
            while True:
                try:
                    row_index = int(input("Nhập chỉ số dòng cần xóa thông tin: ")) - 1
                    if 0 <= row_index < len(data):
                        break
                    else:
                        print("Chỉ số dòng không hợp lệ. Vui lòng thử lại.")
                except ValueError:
                    print("Giá trị không hợp lệ. Vui lòng nhập một số nguyên.")

            # Hiển thị các cột và yêu cầu người dùng chọn cột cần xóa
            print("Các cột có sẵn:")
            for idx, col in enumerate(data.columns):
                print(f"{idx + 1}. {col}")

            # Nhập chỉ số cột và kiểm tra lỗi
            while True:
                try:
                    column_index = int(input("Nhập chỉ số cột cần xóa thông tin: ")) - 1
                    if 0 <= column_index < len(data.columns):
                        actual_column_name = data.columns[column_index]
                        break
                    else:
                        print("Chỉ số cột không hợp lệ. Vui lòng thử lại.")
                except ValueError:
                    print("Giá trị không hợp lệ. Vui lòng nhập một số nguyên.")

            # Đặt NaN cho cột đó tại dòng chỉ định
            data.at[row_index, actual_column_name] = None
            print(f"Đã xóa thông tin trong cột '{actual_column_name}' cho dòng {row_index + 1}.")

        # Xóa toàn bộ một hàng
        elif delete_option == '2':
            # Nhập chỉ số dòng cần xóa và kiểm tra lỗi
            while True:
                try:
                    row_index = int(input("Nhập chỉ số dòng cần xóa: ")) - 1
                    if 0 <= row_index < len(data):
                        break
                    else:
                        print("Chỉ số dòng không hợp lệ. Vui lòng thử lại.")
                except ValueError:
                    print("Giá trị không hợp lệ. Vui lòng nhập một số nguyên.")

            # Xóa dòng và đặt lại chỉ số
            data = data.drop(index=row_index).reset_index(drop=True)
            print(f"Đã xóa thành công dòng {row_index + 1}.")

        # Lưu lại dữ liệu vào file CSV
        data.to_csv('data_source\\cleaned_data.csv', index=False)
        print("Dữ liệu đã được lưu thành công vào file CSV!")

    except ValueError:
        print("Giá trị không hợp lệ.")


# Cập nhật menu chính
if __name__ == "__main__":
    while True:
        print("\nChọn một tùy chọn:")
        print("1. Thêm thông tin sinh viên mới")
        print("2. Hiển thị toàn bộ dữ liệu")
        print("3. Hiển thị n dòng đầu tiên")
        print("4. In ra n cột đầu tiên")
        print("5. In ra các cột cụ thể")
        print("6. In ra các cột cụ thể với số hàng mong muốn")
        print("7. In ra các dòng mong muốn")
        print("8. Cập nhật dữ liệu")
        print("9. Xóa dữ liệu")
        print("10. Thoát")

        choice = input("Nhập lựa chọn của bạn (1-10): ")

        if choice == '1':
            add_student_record()
        elif choice == '2':
            read_full_data()
        elif choice == '3':
            n = int(input("Nhập số dòng muốn hiển thị: "))
            read_n_rows(n)
        elif choice == '4':
            n = int(input("Nhập số cột muốn in ra: "))
            print_n_columns(n)
        elif choice == '5':
            user_select_columns()
        elif choice == '6':
            user_select_columns_and_rows()
        elif choice == '7':
            display_valid_row_range()
            start = int(input("Nhập chỉ số dòng bắt đầu: ")) - 1  # Giảm đi 1 để phù hợp với chỉ số
            end = int(input("Nhập chỉ số dòng kết thúc: ")) - 1  # Giảm đi 1 để phù hợp với chỉ số
            print_rows_range(start, end)
        elif choice == '8':
            update_student_record()
        elif choice == '9':
            delete_student_record()
        elif choice == '10':
            print("Cảm ơn bạn đã sử dụng chương trình!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")


