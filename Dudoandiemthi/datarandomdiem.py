import random

# Tạo danh sách chứa dữ liệu cho 100 sinh viên
data = []

for _ in range(100):
    # Sinh ngẫu nhiên số giờ đi học từ 1 đến 40 giờ
    hours_studied = random.randint(1, 40)

    # Sinh ngẫu nhiên điểm thi giữa kì từ 0 đến 100
    mid_term_score = random.randint(0.0, 10.0)

    # Sinh ngẫu nhiên điểm thi cuối kì từ 0 đến 100
    final_exam_score = random.randint(0.0, 10.0)

    # Thêm thông tin của sinh viên vào danh sách
    student_data = {
        'Số giờ đi học': hours_studied,
        'Điểm thi giữa kì': mid_term_score,
        'Điểm thi cuối kì': final_exam_score
    }
    data.append(student_data)

# In ra dữ liệu của 100 sinh viên
for i, student in enumerate(data, start=1):
    print(student['Số giờ đi học'],student['Điểm thi giữa kì'],student['Điểm thi cuối kì'],sep=",")

