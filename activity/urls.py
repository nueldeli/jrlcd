from django.urls import path
from .views import ActivityIndexView, ActivityDetailView 

urlpatterns = [
	path('activity_index/', ActivityIndexView.as_view(), name='activity_index'),
	path('activity_detail/<int:pk>', ActivityDetailView.as_view(), name='activity_detail'),
]