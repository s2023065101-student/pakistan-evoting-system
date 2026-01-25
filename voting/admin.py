from django.contrib import admin
from .models import Election, Candidate, Vote
from .models import VoteAudit

admin.site.register(Election)
admin.site.register(Candidate)
admin.site.register(Vote)
admin.site.register(VoteAudit)