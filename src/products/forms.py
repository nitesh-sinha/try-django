from django import forms

from .models import Product

# Form is needed only if we want to create product objects from the UI
class ProductForm(forms.ModelForm):
    title = forms.CharField(label='Your_title', widget=forms.TextInput(attrs={
        "placeholder": "Add a title with \"Tesla\""
    }))
    # email = forms.EmailField()
    description = forms.CharField(required=False, widget=forms.Textarea)  # by default required=True for all form fields
    price = forms.DecimalField(initial=100.99)

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if "Tesla" in title:
            return title
        else:
            raise forms.ValidationError("This is not a valid title")

    # def clean_email(self, *args, **kwargs):
    #     email = self.cleaned_data.get("email")
    #     if not email.endswith("edu"):
    #         raise forms.ValidationError("This is not a valid email")
    #     return email


class RawProductForm(forms.Form):
    title = forms.CharField(label='Your_title', widget=forms.TextInput(attrs={
                                                                            "placeholder": "Your title"
                                                                        }))
    description = forms.CharField(required=False, widget=forms.Textarea) # by default required=True for all form fields
    price = forms.DecimalField(initial=100.99)