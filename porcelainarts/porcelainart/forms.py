from django import forms

# our new form
class ContactForm(forms.Form):
    subject = forms.CharField(required=True)
    from_email = forms.EmailField(required=True)
    contact_number = forms.CharField(required=True)
    message = forms.CharField(required=True, widget=forms.Textarea)




    # the new bit we're adding
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['subject'].label = "Subjekti:"
        self.fields['from_email'].label = "E-mail:"
        self.fields['message'].label = "Permbajtje"
        self.fields['contact_number'].label = "Numer kontakti"