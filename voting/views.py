from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.db.models import Count

from .models import Election, Candidate, Vote, VoteAudit


@login_required
def vote_view(request):
    user = request.user

    election = Election.objects.filter(
        is_active=True,
        start_date__lte=timezone.now(),
        end_date__gte=timezone.now()
    ).first()

    if not election:
        return render(request, 'voting/no_election.html')

    # 🔒 CHECK IF USER ALREADY VOTED IN THIS ELECTION
    if Vote.objects.filter(voter=user, election=election).exists():
        return redirect('dashboard')

    candidates = Candidate.objects.filter(election=election)

    if request.method == 'POST':
        candidate_id = request.POST.get('candidate')

        Vote.objects.create(
            voter=user,
            election=election,
            candidate_id=candidate_id
        )

        VoteAudit.objects.create(
            voter=user,
            election=election,
            ip_address=request.META.get('REMOTE_ADDR')
        )

        return redirect('dashboard')

    return render(request, 'voting/vote.html', {
        'election': election,
        'candidates': candidates
    })


from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from .models import Election, Candidate


def results_list_view(request):
    elections = Election.objects.filter(results_published=True).order_by('-end_date')

    return render(request, 'voting/results_list.html', {
        'elections': elections
    })


def results_detail_view(request, election_id):
    election = get_object_or_404(
        Election,
        id=election_id,
        results_published=True
    )

    results = (
        Candidate.objects
        .filter(election=election)
        .annotate(vote_count=Count('vote'))
        .order_by('-vote_count')
    )

    labels = [c.name for c in results]
    votes = [c.vote_count for c in results]

    return render(request, 'voting/results.html', {
        'election': election,
        'results': results,
        'labels': labels,
        'votes': votes
    })
