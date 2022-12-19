from django import forms
from captcha.fields import CaptchaField
class UploadFileForm(forms.Form):
    file = forms.FileField()

class MyForm(forms.Form):
    captcha=CaptchaField()