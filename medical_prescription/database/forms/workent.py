# django
from django import forms

# local django
from database.models import WorkEnt


class CreateWorkEntForm(forms.ModelForm):
    """
    Define fields in user form.
    """
    class Meta:
        # Define model to Work.
        model = WorkEnt
        fields = [
            'work_ent_uri', 'uniform_title',
        ]
