from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils import timezone

from voting.models import Election, Vote


@login_required
def dashboard_view(request):
    user = request.user

    active_election = Election.objects.filter(
        is_active=True,
        start_date__lte=timezone.now(),
        end_date__gte=timezone.now()
    ).first()

    has_voted = False
    if active_election:
        has_voted = Vote.objects.filter(
            voter=user,
            election=active_election
        ).exists()

    context = {
        'full_name': user.full_name,
        'cnic': user.cnic,
        'constituency': user.constituency,
        'has_voted': has_voted,
        'active_election': active_election
    }

    return render(request, 'dashboard/dashboard.html', context)
