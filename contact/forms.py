from django import forms


class ContactForm(forms.Form):
    # Label trabaja similar a verbose_name
    name = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "Escribe tu nombre"}))
    email = forms.EmailField(label="Email", required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    content = forms.CharField(label="Mensaje", required=True, widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': 3}))
