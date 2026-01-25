from django.urls import path
from .views import vote_view, results_list_view, results_detail_view

urlpatterns = [
    path('', vote_view, name='vote'),
    path('results/', results_list_view, name='results'),
    path('results/<int:election_id>/', results_detail_view, name='results_detail'),
]
