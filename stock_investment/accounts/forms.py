from django.contrib.auth import get_user_model  # returns currently active user model
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    class Meta:
        fields = ('username', 'email', 'password1', 'password2')
        help_texts = {
            'username': None,
            'email': None,
        }
        model = get_user_model()

        def __init__(self, *args, **kwargs):  # initializing the form and customizing form labels
            super().__init__(*args, **kwargs)
            self.fields['username'].labels = 'Account handle'
            self.fields['email'].labels = "Email"
            help_texts = {
                'username': None,
                'email': None,
            }
