from django import forms
from .models import *
from django.forms import ModelForm
 

class SearchForm(forms.Form):
   query=forms.CharField(max_length = 100)

class SubscriptionForm(ModelForm):
   class Meta:
      model=Subscription
      fields=['email','name','age','gender','frequency']

   def clean(self):
      super(SubscriptionForm,self).clean()
      email = self.cleaned_data.get('email')
      name = self.cleaned_data.get('name')
      age = self.cleaned_data.get('age')
      gender = self.cleaned_data.get('gender')
      frequency = self.cleaned_data.get('frequency')
      if len(name)<10:
         self._errors['name']=self.error_class(['Atleast 10 characters required'])
      if (age)<13:
         self._errors['age']=self.error_class(['You are too young. Minimum age limit is 13'])
      return self.cleaned_data
      