import tkinter as tk
from tkinter import ttk, messagebox
import csv

questions = [
    {"name": "Hours_Studied", "label": "1. Number of hours spent studying per week.", "type": "entry", "validation": "0-168"},
    {"name": "Attendance", "label": "2. Percentage of classes attended.", "type": "entry", "validation": "0-100"},
    {"name": "Parental_Involvement", "label": "3. Level of parental involvement.", "type": "dropdown", "options": ["Low", "Medium", "High"]},
    {"name": "Access_to_Resources", "label": "4. Availability of educational resources.", "type": "dropdown", "options": ["Low", "Medium", "High"]},
    {"name": "Extracurricular_Activities", "label": "5. Participation in extracurricular activities.", "type": "dropdown", "options": ["Yes", "No"]},
    {"name": "Sleep_Hours", "label": "6. Average number of hours of sleep per night.", "type": "entry", "validation": "0-24"},
    {"name": "Previous_Scores", "label": "7. Scores from previous exams.", "type": "entry", "validation": "0-100"},
    {"name": "Motivation_Level", "label": "8. Student's level of motivation.", "type": "dropdown", "options": ["Low", "Medium", "High"]},
    {"name": "Internet_Access", "label": "9. Availability of internet access.", "type": "dropdown", "options": ["Yes", "No"]},
    {"name": "Tutoring_Sessions", "label": "10. Number of tutoring sessions attended per month.", "type": "entry", "validation": "0-10"},
    {"name": "Family_Income", "label": "11. Family income level.", "type": "dropdown", "options": ["Low", "Medium", "High"]},
    {"name": "Teacher_Quality", "label": "12. Quality of the teachers.", "type": "dropdown", "options": ["Low", "Medium", "High"]},
    {"name": "School_Type", "label": "13. Type of school attended.", "type": "dropdown", "options": ["Public", "Private"]},
    {"name": "Peer_Influence", "label": "14. Influence of peers.", "type": "dropdown", "options": ["Positive", "Neutral", "Negative"]},
    {"name": "Physical_Activity", "label": "15. Average hours of physical activity per week.", "type": "entry", "validation": "0-168"},
    {"name": "Learning_Disabilities", "label": "16. Presence of learning disabilities.", "type": "dropdown", "options": ["Yes", "No"]},
    {"name": "Parental_Education_Level", "label": "17. Highest education level of parents.", "type": "dropdown", "options": ["High School", "College", "Postgraduate"]},
    {"name": "Distance_from_Home", "label": "18. Distance from home to school.", "type": "dropdown", "options": ["Near", "Moderate", "Far"]},
    {"name": "Gender", "label": "19. Gender of the student.", "type": "dropdown", "options": ["Male", "Female"]},
    {"name": "Exam_Score", "label": "20. Final exam score.", "type": "entry", "validation": "0-100"},
]

def makecenter(root):
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

# Hàm kiểm tra dữ liệu nhập
def validate_data(data):
    errors = []
    for question in questions:
        name = question["name"]
        value = data.get(name, "").strip()

        # Kiểm tra nếu dữ liệu trống
        if not value:
            errors.append(f"'{question['label']}' cannot be empty.")
            continue

        # Kiểm tra định dạng số
        if question.get("validation") == "number":
            try:
                float(value)
            except ValueError:
                errors.append(f"'{question['label']}' must be a valid number.")

        # Kiểm tra giá trị trong dropdown
        if question["type"] == "dropdown" and "options" in question:
            if value not in question["options"]:
                errors.append(f"'{question['label']}' must be one of {', '.join(question['options'])}.")

        if question.get("validation") == "0-168":
            try:
                num = float(value)
                if num < 0 or num > 168:
                    errors.append(f"'{question['label']}' must be a number between 0 and 168.")
            except ValueError:
                errors.append(f"'{question['label']}' must be a valid number.")
        
        if question.get("validation") == "0-100":
            try:
                num = float(value)
                if num < 0 or num > 100:
                    errors.append(f"'{question['label']}' must be a number between 0 and 100.")
            except ValueError:
                errors.append(f"'{question['label']}' must be a valid number.")

        if question.get("validation") == "0-24":
            try:
                num = float(value)
                if num < 0 or num > 24:
                    errors.append(f"'{question['label']}' must be a number between 0 and 24.")
            except ValueError:
                errors.append(f"'{question['label']}' must be a valid number.")

        if question.get("validation") == "0-10":
            try:
                num = int(value)
                if num < 0 or num > 10:
                    errors.append(f"'{question['label']}' must be a number between 0 and 10.")
            except ValueError:
                errors.append(f"'{question['label']}' must be a valid number.")


    return errors

# Hàm lưu dữ liệu vào file CSV
def save_to_csv(data):
    file_name = "data_source\\cleaned_data.csv"
    try:
        # Kiểm tra file có tồn tại không, nếu không thì tạo file mới
        with open(file_name, 
                  mode="a", 
                  newline="", 
                  encoding="utf-8") as file:
            writer = csv.DictWriter(file, 
                                    fieldnames=[q["name"] for q in questions])
            # Nếu file mới, ghi header
            if file.tell() == 0:
                writer.writeheader()
            # Ghi dữ liệu
            writer.writerow(data)
        messagebox.showinfo("Success", "Survey saved successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save survey: {e}")

# Tạo giao diện
def create_survey():
    def submit():
        answers = {}
        for question in questions:
            name = question["name"]
            if question["type"] == "entry":
                answers[name] = entries[name].get()
            elif question["type"] == "dropdown":
                answers[name] = dropdowns[name].get()

         # Kiểm tra dữ liệu nhập
        errors = validate_data(answers)

        if errors:
            messagebox.showerror("Validation Error", "\n".join(errors))
            return

        save_to_csv(answers)

    # Tạo cửa sổ chính
    root = tk.Tk()
    root.title("Survey Form")
    root.geometry("600x600")

    # Frame cuộn cho giao diện
    canvas = tk.Canvas(root)
    scrollbar = ttk.Scrollbar(root, 
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

    # Danh sách các widget nhập liệu và lỗi
    entries = {}
    dropdowns = {}

    for i, question in enumerate(questions):
        label = ttk.Label(scrollable_frame, 
                          text=question["label"])
        label.grid(row=i*2, 
                   column=0, 
                   sticky="w", 
                   padx=10, 
                   pady=5)

        if question["type"] == "entry":
            entry = ttk.Entry(scrollable_frame, 
                              width=25)
            entry.grid(row=i*2, 
                       column=1, 
                       padx=10, 
                       pady=5)
            entries[question["name"]] = entry
        
        elif question["type"] == "dropdown":
            dropdown = ttk.Combobox(scrollable_frame, 
                                    width=22, 
                                    values=question["options"], 
                                    state="readonly")
            dropdown.grid(row=i*2, 
                          column=1, 
                          padx=10, 
                          pady=5)
            dropdowns[question["name"]] = dropdown

    # Nút Submit
    submit_button = ttk.Button(scrollable_frame, 
                               text="Submit", 
                               command=submit)
    submit_button.grid(row=len(questions)*2, 
                       column=0, 
                       columnspan=2, 
                       pady=10)

    makecenter(root)
    root.mainloop()

# Chạy giao diện
create_survey()
