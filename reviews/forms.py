from django import forms
from django.core.validators import MinLengthValidator
from django.core.validators import RegexValidator

class MyForm(forms.Form):
    alphabetic_validator = RegexValidator(
        r'^[a-zA-Z]+$',
        'This field should contain alphabetic characters only.'
    )


    YEAR_CHOICES = [
        ('KS3', 'KS3'),
        ('10', 'Year 10'),
        ('11', 'Year 11'),
        ('AS', 'AS'),
        ('A2', 'A2'),
    ]

    GRADE_CHOICES = [
        ('E', 'E'),
        ('D', 'D'),
        ('C', 'C'),
        ('B', 'B'),
        ('A', 'A'),
        ('A*', 'A*'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
    ]

    first_name = forms.CharField(
        max_length=100,
        required=False,
        validators=[alphabetic_validator],
        label='First name (optional, leave blank)',
        error_messages={
            'max_length': 'The first name should not exceed 100 characters.',
        }
    )

    school = forms.CharField(
        max_length=100,
        required=False,
        validators=[alphabetic_validator],
        label='Last name (optional, leave blank)',
        error_messages={
            'max_length': 'The first name should not exceed 100 characters.',
        }
    )

    year_group = forms.ChoiceField(
        choices=YEAR_CHOICES,
        widget=forms.Select(attrs={'placeholder': 'Select Year Group'}),
        error_messages={
            'required': 'Year group not selected',
        }
    )

    predicted_grade = forms.ChoiceField(
        choices=GRADE_CHOICES,
        widget=forms.Select(attrs={'placeholder': 'Select Predicted Grade'}),
        error_messages={
            'required': 'Predicted grade not selected',
        }
    )

    grade_achieved = forms.ChoiceField(
        choices=GRADE_CHOICES,
        widget=forms.Select(attrs={'placeholder': 'Select Grade Achieved'}),
        error_messages={
            'required': 'Grade achieved not selected',
        }
    )

    comments = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Enter your comment here'}),
        validators=[MinLengthValidator(10)],
        error_messages={
            'min_length': 'Feedback should be at least 10 characters long.'
        }
    )