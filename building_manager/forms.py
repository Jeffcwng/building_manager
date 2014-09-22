from django import forms
from django.contrib.auth.forms import UserCreationForm
from models import *
from django.forms import ModelForm
from django.contrib.auth.models import User


class EmailUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Player
        fields = ("username", "first_name", "last_name", "phone", "email", "password1", "password2")

    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            Player.objects.get(username=username)
        except Player.DoesNotExist:
            return username
        raise forms.ValidationError(
            self.error_messages['duplicate_username'],
            code='duplicate_username',
        )
#
class BuildingForm(ModelForm):
    class Meta:
        model = Building

# class BuildingForm(forms.Form):
#     building_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
#     address = forms.CharField()
#     city = forms.CharField()
#     zip_code = forms.IntegerField()

class ApartmentForm(ModelForm):
    class Meta:
        model = Apartment
#
# class ApartmentForm(forms.Form):
#     buildingnum = forms.ModelChoiceField(queryset=Building.objects.all())
#     floor = forms.CharField(label='floor', max_length=20)
#     unit_number = forms.CharField(max_length=10)
#     bedroom = forms.IntegerField()
#     bathroom = forms.IntegerField()
#     sq_ft = forms.IntegerField()
#     rent_amount = forms.CharField()

class RenterForm(ModelForm):
    class Meta:
        model = Renter

