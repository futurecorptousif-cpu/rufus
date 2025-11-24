# Student ID Card Generator

def generate_id_card():
    print("--- Student ID Card Generator ---")
    name = input("Enter student name: ")
    student_class = input("Enter class: ")
    roll_no = input("Enter roll number: ")
    section = input("Enter section: ")
    print("\n--- Student ID Card ---")
    print(f"Name      : {name}")
    print(f"Class     : {student_class}")
    print(f"Roll No.  : {roll_no}")
    print(f"Section   : {section}")
    print("------------------------")

if __name__ == "__main__":
    generate_id_card()
