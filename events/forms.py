from django import forms
from events.models import Event

class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ('event_title','description', 'location', 'date', 'posted_by')

        widgets = {
          
            'event_title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(format='%m/%d/%Y'),
        

        }