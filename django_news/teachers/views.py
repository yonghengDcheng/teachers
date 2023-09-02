from django.shortcuts import render
import csv

# 访问地址：http://127.0.0.1:8000/teachers/search_teacher_by_name/
def find_teacher_info_by_name(teacher_name):
    teacher_info = None
    with open('teacher.csv', 'r') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            if teacher_name == row['Name']:
                teacher_info = row
                break

    return teacher_info


def find_teacher_info_by_department(selected_departments):
    teacher_info_List = []
    with open('teacher.csv', 'r') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            if row['Department'] in selected_departments:
                teacher_info_List.append(row)
    return teacher_info_List


def search_teacher_by_name(request):
    if request.method == 'POST':
        teacher_name = request.POST['teacher_name']
        teacher_info = find_teacher_info_by_name(teacher_name)
        return render(request, 'search_result_by_name.html', context={'teacher_info': teacher_info})
    return render(request, 'search_form.html')


def search_teacher_by_department(request):
    if request.method == 'POST':
        selected_departments = request.POST.getlist('department')
        # 从CSV文件中查找对应系的老师信息
        teacher_info_List = find_teacher_info_by_department(selected_departments)
        return render(request, 'search_result_by_department.html', context={'teacher_info_List': teacher_info_List})
    return render(request, 'search_form.html')







# 获取所有院系
# def add_departments(request):
#     departments = []
#     with open('teacher.csv', 'r', ) as csv_file:
#         csv_reader = csv.DictReader(csv_file)
#         for row in csv_reader:
#             departments.append(row['Department'])
#     unique_departments = list(set(departments))
#     return render(request, 'search_form.html', context={'departments': unique_departments})
