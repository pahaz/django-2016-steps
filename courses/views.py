import subprocess

from courses.models import Lesson
from django.shortcuts import render
from django import forms

# def lesson_step_view(request, lesson_id, lesson_step_id):
#     return render(request, 'index.html', {})


class CodeForm(forms.Form):
    code = forms.CharField(max_length=5000, widget=forms.Textarea)

    def clean_code(self):
        value = self.cleaned_data['code']
        if 'import' in value:
            raise forms.ValidationError('Please don`t use imports!')
        return value


class CreateLessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ('title',)


def run_code(request):
    form = CreateLessonForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
    return render(request, 'index.html', {'form': form})
