from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from manager.models import Worker, Task, Position


class WorkerCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Worker
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "position",
            "bio",
        )


class PositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = ("name",)

    def clean_name(self):
        return validate_position_name(self.cleaned_data["name"])


def validate_position_name(position_name):
    if not all(char.isalpha() or char.isspace() for char in position_name):
        raise ValidationError(
            "Characters in the position name can be only alphabetic or spaces."
        )
    if len(position_name) < 2:
        raise ValidationError(
            "The position name should have at least two letters."
        )

    return position_name


class TaskForm(forms.ModelForm):
    assignees = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Task
        fields = "__all__"


class PositionSearchForm(forms.Form):
    name = forms.CharField(
        max_length=63,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by name...",
            }
        ),
    )


class WorkerSearchForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by username...",
            }
        ),
    )


class TaskTypeSearchForm(forms.Form):
    name = forms.CharField(
        max_length=63,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by name...",
            }
        ),
    )


class TaskSearchForm(forms.Form):
    name = forms.CharField(
        max_length=63,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by name...",
            }
        ),
    )
