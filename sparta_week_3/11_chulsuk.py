# all_students = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]
# present_students = ["정연", "모모", "채영", "쯔위", "사나", "나연", "미나", "다현"]


# def get_absent_student(all_array, present_array):
#     all_array = set(all_array)
#     for name in present_students:
#         if name in all_array:
#             return name

# print(get_absent_student(all_students, present_students))

all_students = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]
present_students = ["정연", "모모", "채영", "쯔위", "사나", "나연", "미나", "다현"]


def get_absent_student(all_array, present_array):
    students_dict = {}
    for key in all_array:
        students_dict[key] = True
    
    for key in present_array:
        del students_dict[key]
    return students_dict.keys()

print(get_absent_student(all_students, present_students))