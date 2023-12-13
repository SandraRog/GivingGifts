from django import forms
from .models import Donation, Category, Institution

class DonationForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
    )

    class Meta:
        model = Donation
        fields = ['quantity', 'categories', 'institution', 'address', 'phone_number', 'city', 'zip_code',
                  'pick_up_date', 'pick_up_time', 'pick_up_comment', 'user']
