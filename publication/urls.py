from django.urls import path
from .views import PublicationIndexView

urlpatterns = [
	path('publication_index/', PublicationIndexView.as_view(), name='publication_index'),
]