from django import forms
from django.core.validators import RegexValidator
# from django.core.validators import MinLengthValidator
# from django.core.validators import RegexValidator
from .models import reviews

class leaveAReviewForm(forms.ModelForm):

    alpha_only = RegexValidator(r'^[a-zA-Z]*$', 'Only alphabetic characters are allowed.')

    class Meta:
        model = reviews
        # fields = '__all__'
        exclude = ['id', 'timestamp']
        # can specify only fields to use on the FE here
        labels = {
            'first_name' : 'First name (optional, leave blank)',
            'school_name' : 'School (optional, leave blank)',
            'year_group' : 'Year group',
            'predicted_grade' : 'Predicted Grade',
            'achieved_grade' : 'Grade Achieved',
            'star_rating' : 'Rating',
            'feedback_comments' : 'comments',
        }

        # help_texts = {
        #     'first_name' : 'Please enter students first name.',
        # }


    #field validation goes here
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if first_name and not first_name.isalpha():
            raise forms.ValidationError('First name should only contain alphabetic characters.')
        return first_name

    def clean_school_name(self):
        school_name = self.cleaned_data.get('school_name')
        if school_name and not school_name.isalpha():
            raise forms.ValidationError('School name should only contain alphabetic characters.')
        return school_name

    def clean_year_group(self):
        year_group = self.cleaned_data.get('year_group')
        if not year_group:
            raise forms.ValidationError('Year group not selected.')
        return year_group

    def clean_predicted_grade(self):
        predicted_grade = self.cleaned_data.get('predicted_grade')
        if not predicted_grade:
            raise forms.ValidationError('Predicted grade not selected.')
        return predicted_grade

    def clean_achieved_grade(self):
        achieved_grade = self.cleaned_data.get('achieved_grade')
        if not achieved_grade:
            raise forms.ValidationError('Achieved grade not selected.')
        return achieved_grade

    def clean_star_rating(self):
        star_rating = self.cleaned_data.get('star_rating')
        if not star_rating:
            raise forms.ValidationError('Star rating not selected.')
        return star_rating

    def clean_feedback_comments(self):
        feedback_comments = self.cleaned_data.get('feedback_comments')
        if len(feedback_comments) < 10:
            raise forms.ValidationError('Feedback must be more than 10 characters.')
        return feedback_comments

    def clean_passcode(self):
        passcode = self.cleaned_data.get('passcode')
        if passcode.lower().strip() != 'testing123':
            raise forms.ValidationError('Passcode incorrect.')
        return passcode



    # alphabetic_validator = RegexValidator(
    #     r'^[a-zA-Z]+$',
    #     'This field should contain alphabetic characters only.'
    # )


    # YEAR_CHOICES = [
    #     ('KS3', 'KS3'),
    #     ('10', 'Year 10'),
    #     ('11', 'Year 11'),
    #     ('AS', 'AS'),
    #     ('A2', 'A2'),
    # ]

    # GRADE_CHOICES = [
    #     ('E', 'E'),
    #     ('D', 'D'),
    #     ('C', 'C'),
    #     ('B', 'B'),
    #     ('A', 'A'),
    #     ('A*', 'A*'),
    #     ('1', '1'),
    #     ('2', '2'),
    #     ('3', '3'),
    #     ('4', '4'),
    #     ('5', '5'),
    #     ('6', '6'),
    #     ('7', '7'),
    #     ('8', '8'),
    #     ('9', '9'),
    # ]

    # first_name = forms.CharField(
    #     max_length=100,
    #     required=False,
    #     validators=[alphabetic_validator],
    #     label='First name (optional, leave blank)',
    #     error_messages={
    #         'max_length': 'The first name should not exceed 100 characters.',
    #     }
    # )

    # school = forms.CharField(
    #     max_length=100,
    #     required=False,
    #     validators=[alphabetic_validator],
    #     label='Last name (optional, leave blank)',
    #     error_messages={
    #         'max_length': 'The first name should not exceed 100 characters.',
    #     }
    # )

    # year_group = forms.ChoiceField(
    #     choices=YEAR_CHOICES,
    #     widget=forms.Select(attrs={'placeholder': 'Select Year Group'}),
    #     error_messages={
    #         'required': 'Year group not selected',
    #     }
    # )

    # predicted_grade = forms.ChoiceField(
    #     choices=GRADE_CHOICES,
    #     widget=forms.Select(attrs={'placeholder': 'Select Predicted Grade'}),
    #     error_messages={
    #         'required': 'Predicted grade not selected',
    #     }
    # )

    # grade_achieved = forms.ChoiceField(
    #     choices=GRADE_CHOICES,
    #     widget=forms.Select(attrs={'placeholder': 'Select Grade Achieved'}),
    #     error_messages={
    #         'required': 'Grade achieved not selected',
    #     }
    # )

    # comments = forms.CharField(
    #     widget=forms.Textarea(attrs={'placeholder': 'Enter your comment here'}),
    #     validators=[MinLengthValidator(10)],
    #     error_messages={
    #         'min_length': 'Feedback should be at least 10 characters long.'
    #     }
    # )