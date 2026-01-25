from django.db import models
from accounts.models import User


class Election(models.Model):
    title = models.CharField(max_length=200)
    is_active = models.BooleanField(default=False)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    results_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Candidate(models.Model):
    election = models.ForeignKey(Election, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    party = models.CharField(max_length=150)
    symbol = models.ImageField(upload_to='symbols/')

    def __str__(self):
        return f"{self.name} ({self.party})"


class Vote(models.Model):
    voter = models.ForeignKey(User, on_delete=models.CASCADE)
    election = models.ForeignKey(Election, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    cast_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('voter', 'election')

    def __str__(self):
        return f"{self.voter.cnic} voted in {self.election.title}"



class VoteAudit(models.Model):
    voter = models.ForeignKey(User, on_delete=models.CASCADE)
    election = models.ForeignKey(Election, on_delete=models.CASCADE)
    voted_at = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)

    def __str__(self):
        return f"Audit: {self.voter.cnic} - {self.election.title}"
