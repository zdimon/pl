from django.forms import ModelForm
from cabinet.models import UserProfile
from course.models import Comments, Course



class ProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['publicname', 'phone', 'telegram', 'skype']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['publicname'].required = False
        self.fields['phone'].required = False
        self.fields['telegram'].required = False
        self.fields['skype'].required = False

class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['content']