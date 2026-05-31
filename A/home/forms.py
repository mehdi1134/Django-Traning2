from django import forms

class TodoCreateForm(forms.Form):

    title = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        })
    )

    body = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control'
        })
    )

    created = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={
                'type': 'datetime-local',
                'class': 'form-control'
            },
            format='%Y-%m-%dT%H:%M'
        ),
        input_formats=['%Y-%m-%dT%H:%M']
    )