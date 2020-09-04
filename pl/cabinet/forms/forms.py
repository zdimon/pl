from django import forms
from django.core.exceptions import ValidationError
from .widgets import ShowHidePasswordWidget


from course.models import  Course
from django.forms import ModelForm
    
class MyCourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'desc']


class MyCommentForm(forms.Form):
    title = forms.CharField(help_text="Enter a title.")
    #date = forms.DateField(help_text="Enter a date.")
    #password = forms.CharField(widget=ShowHidePasswordWidget())

    def save(self):
        title = self.cleaned_data['title']


    def clean_title(self):
        data = self.cleaned_data['title']
        #Проверка того, что заголовок больше 3-х символов 
        if len(data)<4:
            raise ValidationError('Title too small!!!')
        # Помните, что всегда надо возвращать "очищенные" данные.
        return data

    def as_div(self):
        "Return this form rendered as HTML <p>s."
        return self._html_output(
            normal_row='''
            <div class="col-md-12 px-1">
                <div class="form-group">
                    <label>%(label)s</label> 
                    %(field)s%(help_text)s
                </div>
            </div>''',
            error_row='<div style="color: red">%s</div>',
            row_ender='</p>',
            help_text_html=' <span class="helptext">%s</span>',
            errors_on_separate_row=True,
        )   
