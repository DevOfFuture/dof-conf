from django.shortcuts import render

from dof_conf.conference.models import Speaker, ScheduleItem


def home(request):
    speakers = Speaker.objects.filter(is_active=True)
    schedule = ScheduleItem.objects.filter(is_active=True)

    return render(
        request,
        'pages/home.html',
        {'speakers': speakers, 'schedule': schedule}
    )
