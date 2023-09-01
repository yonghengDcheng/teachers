from django import forms

class TeacherNameForm(forms.Form):
    teacher_name = forms.CharField(label='老师姓名', max_length=100)

class DepartmentForm(forms.Form):
    departments = forms.MultipleChoiceField(
        label='选择系',
        choices=[('数字媒体系', '数字媒体系'), ('其他系', '其他系')],
        widget=forms.CheckboxSelectMultiple,
    )
