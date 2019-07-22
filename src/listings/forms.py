# from django import forms
# from .models import Listing
#
# class StatusForm(forms.ModelForm):
#     class Meta:
#         model = Listing
#         fields = [
#             'realtor',
#             'title',
#             'address',
#             'city',
#             'state',
#             'zipcode',
#             'description',
#             'price',
#             'bedrooms',
#             'bathrooms',
#             'garage',
#             'sqft',
#             'lot_size',
#             'photo_main',
#             'photo_1',
#             'photo_2',
#             'photo_3',
#             'photo_4',
#             'photo_5',
#             'photo_6',
#             'is_published',
#             'list_date',
#         ]
#
#     def clean_content(self, *args, **kwargs):
#         content = self.cleaned_data.get('content')
#         if len(content) > 240:
#             raise forms.ValidationError("Content is too long")
#         return content
#
#     def clean(self, *args, **kwargs):
#         data = self.cleaned_data
#         content = data.get('content', None)
#         if content == "":
#             content = None
#         image = data.get("image", None)
#         if content is None and image is None:
#             raise forms.ValidationError('Content or image is required.')
#         return super().clean(*args, **kwargs)