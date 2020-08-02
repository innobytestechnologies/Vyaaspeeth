from django import forms
from .models import book_live

class BookLiveForm(forms.ModelForm):
	class Meta:
		model = book_live
		fields = '__all__'
	def clean_mobile_no(self):
		mobile_no = self.cleaned_data['mobile_no']
		if len(str(mobile_no)) != 10:
		    raise forms.ValidationError('enter  a 10 digit number')
		return self.cleaned_data['mobile_no']


