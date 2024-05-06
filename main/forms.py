from django import forms
from .models import Course
from .models import Lesson
class CourseEditForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('title', 'description', 'thumbnail', 'featured_video', 'level', 'duration', 'category', 'requirements', 'content', 'lesson_title', 'lesson_video')

class LessonUploadForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ('lesson_title','lesson_no','lesson_video', 'paragraph1','paragraph2','paragraph3'   )