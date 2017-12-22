from django import forms
from polls.models import Question, Choice
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# POLL FORMS #
class QuestionForm(forms.ModelForm):
    # question_text = forms.CharField(max_length=200, help_text="Please enter the question.")
    #pub_date = forms.DateTimeField(help_text="Please enter Date.",initial = timezone.now)
    class Meta:
        model = Question
        #fields = "__all__"
        fields = ('question_text','pub_date')
