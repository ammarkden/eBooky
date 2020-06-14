from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class newForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2','email')
    def save(self):
        user = super().save()
        user.email = self.cleaned_data['email']
        user.save()
