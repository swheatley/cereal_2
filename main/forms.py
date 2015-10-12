from main.models import Manufacturer


class ManufacturerForm(forms.ModelForm):  
    class Meta:
        model = Manufacturer
        fields = '__all__'

# #class SpeedModelForm2(forms.Form):  
#     title = forms.CharField(required=True)
#     info = forms.CharField(required=True, widget=forms.Textarea)
#     image = forms.ImageField(required=True)

class ManufacturerForm2 (form.Form):
    title = forms.CharField(required=True)
    info = forms.CharField(required=True, widget=forms.Textarea)
    image = forms.ImageField(required=True)


#class SpeedModelUpdateForm(forms.Form):  
    title = forms.CharField(required=False)
    info = forms.CharField(required=False, widget=forms.Textarea)
    image = forms.ImageField(required=False)

# #class UserSignUp(forms.Form):  
#     email = forms.EmailField(required=True)
#     password = forms.CharField(widget=forms.PasswordInput(), required=True)

# #class UserLogin(forms.Form):  
#     username = forms.CharField(required=True)
#     password = forms.CharField(required=True, widget=forms.PasswordInput())
