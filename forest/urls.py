from django.urls import path
from .views import ForestIndexView, ForestDetailView

urlpatterns = [
	path('forest_index/', ForestIndexView.as_view(), name='forest_index'),
	path('forest_detail/<int:pk>', ForestDetailView.as_view(), name='forest_detail'),
]