from django import forms


def widget_attrs(placeholder):
    return {'class': 'u-full-width', 'placeholder': placeholder}


def form_kwargs(widget, label='', max_length=128):
    return {'widget': widget, 'label': label, 'max_length': max_length}


class TodoForm(forms.Form):
    description = forms.CharField(
        **form_kwargs(
            widget=forms.TextInput(attrs=widget_attrs('Enter your todo'))
        )
    )

class LoginForm(forms.Form):

    username = forms.CharField(
        **form_kwargs(widget=forms.TextInput(attrs=widget_attrs('Username')))
    )
    password = forms.CharField(
        **form_kwargs(
            widget=forms.PasswordInput(attrs=widget_attrs('Password'))
        )
    )

    def clean(self):
        # Don't check if we already have errors.
        if self.errors:
            return self.cleaned_data

        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = User.objects.filter(username=username).first()

        if not user or not user.check_password(password):
            raise forms.ValidationError('Incorrect username and/or password.')

        return self.cleaned_data


class TodoListForm(forms.Form):
    title = forms.CharField(
        **form_kwargs(
            widget=forms.TextInput(
                attrs=widget_attrs('Enter a title to start a new todolist')
            )
        )
    )
