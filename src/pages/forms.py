from django import forms

from .models import Email



# class EmailCreateForm(forms.Form):
#     email_name = forms.CharField(max_length=100, null=True, blank=True)
#     from_email = forms.EmailField(max_length=100, null=True, blank=True)
#     subject = forms.CharField(max_length=100, null=True, blank=True)
#     message = forms.CharField(max_length=100, null=True, blank=True)

#
# def clean_email_name(self):
#         email_name = self.cleaned_data.get("email_name")
#         if email_name == "Hello":
#             raise forms.ValidationError("Not a valid name")
#         return email_name


class EmailCreateForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = [
            'email_name',
            'from_email',
            'phone',
            'message',
            'document',
        ]

    def clean_email_name(self):
        email_name = self.cleaned_data.get("email_name")
        if email_name == "Hello":
            raise forms.ValidationError("Not a valid name")


        return email_name






