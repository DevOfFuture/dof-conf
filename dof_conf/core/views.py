from django.contrib import messages
from django.shortcuts import redirect, render
from django.utils.translation import ugettext_lazy as _

from dof_conf.conference.models import Speaker, ScheduleItem
from dof_conf.reservations.forms import ReservationForm


def home(request):
    speakers = Speaker.objects.filter(is_active=True)
    schedule = ScheduleItem.objects.filter(is_active=True)
    form = ReservationForm()

    return render(
        request,
        'pages/home.html',
        {'speakers': speakers, 'schedule': schedule, 'reservation_form': form}
    )


def reservations(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _('Thank you. Your reservation was '
                                        'successfully recorded!'))
            return redirect('core:home')
    else:
        form = ReservationForm()

    return render(
        request,
        'pages/reservations.html',
        {'form': form}
    )
