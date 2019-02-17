from django import forms
from django.utils.translation import ugettext_lazy as _

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import Reservation


class ReservationForm(forms.ModelForm):
    subscribed = forms.BooleanField(
        label=_('Send me updates about the event and future events from Dev of '
                'Future'),
        initial=True,
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super(ReservationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_action = 'core:reservations'
        self.helper.add_input(Submit('submit', _('Save my spot')))

    class Meta:
        model = Reservation
        fields = ('name', 'email', 'number_of_tees', 'number_of_stickers',
                  'subscribed')
