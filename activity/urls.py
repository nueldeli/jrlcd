from django.urls import path
from .views import ActivityIndexView, ActivityDetailView, planting_index, corporate_index, wilding_index, nursery_index 

urlpatterns = [
	path('activity_index/', ActivityIndexView.as_view(), name='activity_index'),
	path('planting_index/', planting_index, name='planting_index'),
	path('corporate_index/', corporate_index, name='corporate_index'),
	path('wilding_index/', wilding_index, name='wilding_index'),
	path('nursery_activity_index/', nursery_index, name='nursery_activity_index'),
	path('activity_detail/<int:pk>', ActivityDetailView.as_view(), name='activity_detail'),
]