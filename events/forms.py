from django import forms
from events.models import Event

class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ('event_title', 'posted_by','description', 'location', 'date')

        widgets = {
          
            'event_title': forms.TextInput(attrs={'class': 'form-control'}),
            'posted_by': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(format='%m/%d/%Y'),
        

        }